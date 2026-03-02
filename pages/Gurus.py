import streamlit as st
import pandas as pd

st.title("Guru's Only")

# Back button
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

CORRECT_PASSWORD = st.secrets["guru_password"]

password = st.text_input("Enter Password", type="password")
if st.button("Login"):
    if password == CORRECT_PASSWORD:
        st.session_state.authenticated = True
        sheet_link = "https://docs.google.com/spreadsheets/d/1Lf9Rs121pEpCPjAhEC7pk00ffvmOim51vLmrUePJP5A/edit#gid=0"

        st.markdown(f"""
        <a href="{sheet_link}" target="_blank">
            <button style="padding:10px 20px; font-size:14px;">Spel Toevoegen of Verwijderen</button>
        </a>
        """, unsafe_allow_html=True)
        
        # # Changes
        # if st.button("Spel Opmerkingen"):
        #     st.switch_page("pages/Changes.py")
        
        if st.button("⬅ Back to Home"):
            st.switch_page("app.py")
        st.divider()
    else:
        st.error("Incorrect password")

st.stop()  
