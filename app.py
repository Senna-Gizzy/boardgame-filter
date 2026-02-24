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

st.title("🎲 Boardgame Filter")

amount_player = st.number_input("Amount of Players", min_value=1, step=1)
language = st.selectbox('Language', [None, 'Dutch', 'English'])
game_type = st.selectbox('Game Type', ["Children's", 'Family', 'Party', 'Strategy', 'Thematic'])

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

    if filtered.empty:
        st.warning("No game can be found")
    else:
        st.write(filtered['Boardgame'])
