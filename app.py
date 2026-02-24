import streamlit as st
import pandas as pd

# Load your data (adjust filename!)
df = pd.read_csv("Spellenhuis Bordspellen Library - Library.csv")

df['Type'] = df['Type'].str.split(',').str[-1].str.strip()

st.title("🎲 Boardgame Filter")

amount_player = st.number_input("Amount of Players", min_value=1, step=1)
# amount_player = st.text_input("Amount of Players")
# min_player = st.text_input("Min Players")
# max_player = st.text_input("Max Players")
language = st.text_input("Language")
game_type = st.text_input("Game Type")

if st.button("Filter Games"):
    amount_player = int(amount_player) if amount_player else None
    # min_player = int(min_player) if min_player else None
    # max_player = int(max_player) if max_player else None
    language = language if language else None
    game_type = game_type if game_type else None

    filtered = df.copy()

    # if min_player is not None:
    #     filtered = filtered[filtered['Min. Players'] == min_player]

    # if max_player is not None:
    #     filtered = filtered[filtered['Max. Players'] == max_player]

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
