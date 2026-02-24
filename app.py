import streamlit as st
import pandas as pd

# TO DO
# Search balk toevoegen
# Talen er goed in zetten
# Spel Mechanism Toevoegen
# Spelduur toevoegen
# Misschien toggle bar om aan te geven of je op iets wilt filteren
# Complexity toevoegen
# Plek in de kast aangeven
# Zodra je op het spel klikt je een overzicht krijgt van hoe het eruit ziet en waar in de kast het ligt


# Load your data (adjust filename!)
df = pd.read_csv("Spellenhuis Bordspellen Library - Library.csv")

df['Type'] = df['Type'].str.split(',').str[-1].str.strip()
df['Playing Time'] = df['Playing Time'].str[:-3].str.strip()
df[['Min Playing Time', 'Max Playing Time']] = (df['Playing Time'].str.split('-', expand=True))
df['Max Playing Time'] = df['Max Playing Time'].fillna(df['Min Playing Time'])

st.title("Boardgame Filter")

if st.button("Search for a Specific Game"):
    st.switch_page("pages/Search_Game.py")
    
amount_player = st.number_input("Amount of Players", min_value=1, step=1)
language = st.selectbox('Language', [None, 'Dutch', 'English'])
game_type = st.selectbox('Game Type', [None,"Children's", 'Family', 'Party', 'Strategy', 'Thematic'])
playing_time = st.number_input("Maximum Playing Time", min_value=10, step=5)

# game_type = st.text_input("Game Type")

if st.button("Filter Games"):
    amount_player = int(amount_player) if amount_player else None
    language = language if language else None
    game_type = game_type if game_type else None

    filtered = df.copy()

    if amount_player is not None:
        filtered = filtered[(filtered['Min. Players'] <= amount_player) & (filtered['Max. Players'] >= amount_player)]

    if language is not None:
        filtered = filtered[filtered['Language'] == language]

    if game_type is not None:
        filtered = filtered[filtered['Type'] == game_type]

    if playing_time is not None:
        filtered = filtered[filtered['Max Playing Time'] <= playing_time]

    if filtered.empty:
        st.warning("No game can be found")
    else:
        st.write(filtered['Boardgame'])
