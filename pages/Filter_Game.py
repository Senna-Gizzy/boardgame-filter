# Hier komt uiteindelijk echt het filteren
# Load your data (adjust filename!)
import streamlit as st
import pandas as pd
import random

sheet_url = "https://docs.google.com/spreadsheets/d/1Lf9Rs121pEpCPjAhEC7pk00ffvmOim51vLmrUePJP5A/export?format=csv&gid=0"
df = pd.read_csv(sheet_url)

# df = pd.read_csv("Spellenhuis Bordspellen Library - Library.csv")
#_____________________________________________________________________________________________
# Prepare dataframe
df['Type'] = df['Type'].str.split(',').str[-1].str.strip()
df['Playing Time'] = df['Playing Time'].str[:-3].str.strip()
df[['Min Playing Time', 'Max Playing Time']] = (df['Playing Time'].str.split('-', expand=True))
df['Max Playing Time'] = df['Max Playing Time'].fillna(df['Min Playing Time'])
df['Max Playing Time'] = pd.to_numeric(df['Max Playing Time'], errors='coerce')

# Main Page
st.subheader("Filter Opties")
if st.button("⬅ Terug"):
    st.switch_page("app.py")

# Players
use_players = st.toggle("Filter op aantal spelers")
if use_players:
    amount_player = st.number_input("Aantal spelers", min_value=1, step=1)

# Language
use_language = st.toggle("Filter op taal")
if use_language:
    language = st.selectbox("Taal", ['Dutch', 'English'])

# Type
use_type = st.toggle("Filter op type spel")
if use_type:
    game_type = st.selectbox("Spel type",["Abstract","Children", 'Family', 'Party', 'Strategy', 'Narrative'])

# Playing Time
use_playing_time = st.toggle("Filter op maximum spelduur")
if use_playing_time:
    playing_time = st.number_input("Maximum spelduur (minuten)", min_value=10, step=5)

st.divider()

# Add the two buttons for filtering
col1, col2 = st.columns(2)

with col1:
    if st.button("Laat 10 spellen zien"):
        filtered = df.copy()
        if use_players:
            filtered = filtered[(filtered['Min. Players'] <= amount_player) & (filtered['Max. Players'] >= amount_player)]
        if use_language:
            filtered = filtered[filtered['Language'] == language]
        if use_type:
            filtered = filtered[filtered['Type'] == game_type]
        if use_playing_time:
            filtered = filtered[filtered['Max Playing Time'] <= playing_time]

        # Show up to 10 random games as cards
        if not filtered.empty:
            games = filtered.sample(min(10, len(filtered)))
            for idx, game in games.iterrows():
                game_name = game[['Boardgame','Letter','Number']]

                # Display the card (you can customize it with a game image URL if available)
                st.markdown(f"""
                <div style="background-color:#c29e8e; padding: 15px; border-radius: 10px; margin-bottom: 10px;">
                    <h5 style="font-size: 16px; color: #333;">{game_name}</h5>
                    
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Geen spellen gevonden")

    if st.button("Zoek Alle spellen"):
        # Show all games
        filtered = df.copy()
        if use_players:
            filtered = filtered[(filtered['Min. Players'] <= amount_player) & (filtered['Max. Players'] >= amount_player)]
        if use_language:
            filtered = filtered[filtered['Language'] == language]
        if use_type:
            filtered = filtered[filtered['Type'] == game_type]
        if use_playing_time:
            filtered = filtered[filtered['Max Playing Time'] <= playing_time]

        # Show all games if filtered
        if not filtered.empty:
            st.write(filtered[['Boardgame', 'Letter', 'Number']])
        else:
            st.warning("Geen spellen gevonden")


#<p style="font-size: 14px;">Klik om naar de [BoardGameGeek pagina](https://boardgamegeek.com/boardgame/{random.randint(1000, 9999)})</p>
            

    
