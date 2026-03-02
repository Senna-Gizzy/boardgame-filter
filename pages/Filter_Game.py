# Hier komt uiteindelijk echt het filteren
# Load your data (adjust filename!)
import streamlit as st
import pandas as pd

df = pd.read_csv("Spellenhuis Bordspellen Library - Library.csv")
#_____________________________________________________________________________________________
# Prepare dataframe
df['Type'] = df['Type'].str.split(',').str[-1].str.strip()
df['Playing Time'] = df['Playing Time'].str[:-3].str.strip()
df[['Min Playing Time', 'Max Playing Time']] = (df['Playing Time'].str.split('-', expand=True))
df['Max Playing Time'] = df['Max Playing Time'].fillna(df['Min Playing Time'])
df['Max Playing Time'] = pd.to_numeric(df['Max Playing Time'], errors='coerce')

# Main Page
st.subheader("Filter Options")
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

# Players
use_players = st.toggle("Filter by Amount of Players")
if use_players:
    amount_player = st.number_input("Amount of Players", min_value=1, step=1)

# Language
use_language = st.toggle("Filter by Language")
if use_language:
    language = st.selectbox("Language", ['Dutch', 'English'])

# Type
use_type = st.toggle("Filter by Game Type")
if use_type:
    game_type = st.selectbox("Game Type",["Abstract","Children's", 'Family', 'Party', 'Strategy', 'Thematic'])

# Playing Time
use_playing_time = st.toggle("Filter by Maximum Playing Time")
if use_playing_time:
    playing_time = st.number_input("Maximum Playing Time (minutes)", min_value=10, step=5)

st.divider()

if st.button("Filter Games"):
    filtered = df.copy()

    if use_players:
        filtered = filtered[(filtered['Min. Players'] <= amount_player) & (filtered['Max. Players'] >= amount_player)]

    if use_language:
        filtered = filtered[filtered['Language'] == language]

    if use_type:
        filtered = filtered[filtered['Type'] == game_type]

    if use_playing_time:
        filtered = filtered[filtered['Max Playing Time'] <= playing_time]

    if filtered.empty:
        st.warning("No game can be found")
    else:
        st.write(filtered['Boardgame'])
