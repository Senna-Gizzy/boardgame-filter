import streamlit as st
import pandas as pd

st.title("Guru's Only")

# Back button
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

CORRECT_PASSWORD = st.secrets["guru_password"]

password = st.text_input("Enter Password", type="password")
if st.login("Login"):
    if password == CORRECT_PASSWORD:
        st.session_state.authenticated = True
        st.success("Access granted!")
        st.switch_page("app.py")
    else:
        st.error("Incorrect password")

st.stop()  
