import streamlit as st
import pandas as pd

sheet_url = "https://docs.google.com/spreadsheets/d/1Lf9Rs121pEpCPjAhEC7pk00ffvmOim51vLmrUePJP5A/export?format=csv&gid=0"
df = pd.read_csv(sheet_url)
# df = pd.read_csv("Spellenhuis Bordspellen Library - Library.csv")

st.title("Zoek Specifiek Spel")

# Back button
if st.button("⬅ Terug"):
    st.switch_page("app.py")

search_term = st.text_input("Type een bordspelnaam")

filtered = df.copy()

if search_term:
    filtered = filtered[
        filtered['Boardgame'].str.contains(search_term, case=False, na=False)
    ]

st.dataframe(filtered)
