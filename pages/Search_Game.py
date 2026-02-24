import streamlit as st
import pandas as pd

df = pd.read_csv("Spellenhuis Bordspellen Library - Library.csv")

st.title("Search for a Specific Game")

# Back button
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

search_term = st.text_input("Type a game name")

filtered = df.copy()

if search_term:
    filtered = filtered[
        filtered['Boardgame'].str.contains(search_term, case=False, na=False)
    ]

st.dataframe(filtered)
