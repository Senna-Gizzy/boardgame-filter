import streamlit as st
import pandas as pd


st.markdown("""
<style>
/* ------------------ App Background ------------------ */
.stApp {
    background-color: #4F8A8B;
}

/* ------------------ Titles ------------------ */
h1 {
    text-align: left;
    color: white !important;
    font-weight: 700;
    font-size: 40px;
    margin-bottom: 20px;
}
h2, h3, h4, h5, h6 {
    color: white !important;
}

/* ------------------ Buttons ------------------ */
.stButton > button {
    background-color: #654f41;
    color: white;
    border-radius: 12px;
    height: 48px;
    width: 100%;
    border: none;
    font-weight: 600;
    transition: all 0.2s ease;
}
.stButton > button:hover {
    background-color: #c29e8e;
    transform: translateY(-2px);
}

/* ------------------ Selectboxes ------------------ */
/* Selectbox label (above the box) */
div[data-testid="stTextinput"] label p {
    color: white !important;
}

/* Placeholder text inside the text input */
.stTextInput input::placeholder {
    color: white !important;
    opacity: 1 !important;  /* Ensure full opacity */
}

/* Selected value inside the selectbox */
div[data-testid="stTextinput"] div[data-baseweb="select"] span {
    color: black !important;
}

/* Dropdown menu background and options */
div[role="listbox"] {
    background-color: white !important;
}
div[role="listbox"] div span {
    color: black !important;
}
div[role="listbox"] div:hover {
    background-color: #f0f0f0 !important;
    color: black !important;
}
</style>
""", unsafe_allow_html=True)
#____________________________________________________________
sheet_url = "https://docs.google.com/spreadsheets/d/1Lf9Rs121pEpCPjAhEC7pk00ffvmOim51vLmrUePJP5A/export?format=csv&gid=0"
df = pd.read_csv(sheet_url)
# df = pd.read_csv("Spellenhuis Bordspellen Library - Library.csv")

if st.button("⬅ Terug"):
    st.switch_page("app.py")

st.write("")
st.title("Zoek Specifiek Spel")
st.write("")

search_term = st.text_input("Type een bordspelnaam")

filtered = df.copy()



if search_term:
            filtered = filtered[filtered['Boardgame'].str.contains(search_term, case=False, na=False)]
            filtered['Locatie'] = filtered['Letter'] + filtered['Number'].astype(str)
            st.dataframe(
                filtered[['Boardgame', 'Locatie']],
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Boardgame": "Bordspel",
                    "Locatie": "📍 Locatie"
                }
            )    

