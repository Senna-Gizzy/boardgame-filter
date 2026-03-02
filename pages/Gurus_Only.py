import streamlit as st
import pandas as pd
#_____________________________________________________________________________________________
# Add button
st.title("Guru's Only Page")

if st.button("Nieuw Spel Toevoegen"):
    st.switch_page("pages/Add.py")

# Delete button
if st.button("Spel Verwijderen"):
    st.switch_page("pages/Delete.py")

# Changes
if st.button("Spel Opmerkingen"):
    st.switch_page("pages/Changes.py")

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")
st.divider()
