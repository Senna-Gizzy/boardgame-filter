import streamlit as st
import pandas as pd
#_____________________________________________________________________________________________
# Add button
if st.button("Nieuw Spel Toevoegen"):
    st.switch_page("pages/Gurus_Only/Add.py")

# Delete button
if st.button("Spel Verwijderen"):
    st.switch_page("pages/Gurus_Only/Delete.py")

# Changes
if st.button("Spel Opmerkingen"):
    st.switch_page("pages/Gurus_Only/Changes.py")

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")
st.divider()
