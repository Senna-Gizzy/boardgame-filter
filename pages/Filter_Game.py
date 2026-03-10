# Hier komt uiteindelijk echt het filteren
# Load your data (adjust filename!)
import streamlit as st
import pandas as pd
import random

# blueish: #4F8A8B
# darkbrown: #654f41
# lightbrown: #c29e8e

st.markdown("""
<style>
/* Background color */
.stApp {
    background-color: #4F8A8B;
}

/* Title styling */
h1 {
    text-align: left;
    color: white !important;
    font-weight: 700;
    font-size: 40px;
    margin-bottom: 20px;
}

/* Button */
.stButton > button {
    background-color: #654f41;
    color: white;
    border-radius: 12px;
    height: 48px;
    width: 100%;
    border: none;
    font-weight: 600;
    transition: all 0.2s ease;
}

/* Hover effect */
.stButton > button:hover {
    background-color: #c29e8e;
    transform: translateY(-2px);
}

/* Toggle label text (Filter op aantal spelers etc.) */
div[data-testid="stToggle"] p {
    color: white !important;
}

/* Other input labels */
div[data-testid="stNumberInput"] label p {
    color: black !important;
}

div[data-testid="stSelectbox"] label p {
    color: white !important;
}


/* Expander header */
.streamlit-expanderHeader {
    background-color: white;
    border-radius: 8px;
    padding: 6px;
}

/* Expander content */
.streamlit-expanderContent {
    background-color: white;
    border-radius: 8px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

#_______________________________________________________________________
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
if st.button("⬅ Terug"):
    st.switch_page("app.py")

st.write("")
st.title("Filter Opties")
st.write("")

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

st.write("")
st.write("")
#st.divider()

# Add the two buttons for filtering
col1, col2 = st.columns(2)

with col1:
    if st.button("Laat 10 spellen zien", use_container_width = True):
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
        
                game_name = game['Boardgame']
                letter = game['Letter']
                number = game['Number']
                min_players = game['Min. Players']
                max_players = game['Max. Players']
                play_time = game['Playing Time']
                game_type = game['Type']
                mechanism = game['Mechanisms']
        
                with st.expander(f"{game_name}"):
        
                    st.write(f"📍 Locatie: {letter}{number}")
                    st.write(f"👥 Spelers: {min_players} - {max_players}")
                    st.write(f"⏱️ Speeltijd: {play_time}")
                    st.write(f"🎯 Type: {game_type}")
                    st.write(f"⚙️ Mechanisme: {mechanism}")
        
        else:
            st.warning("Geen spellen gevonden")

    if st.button("Zoek Alle spellen", use_container_width = True):
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
            

    
