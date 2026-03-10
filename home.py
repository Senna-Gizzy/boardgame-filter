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

#________________________________________________________________________________
# Opmaak
st.markdown("""
<style>
/* Background color */
.stApp {
    background-color: #4F8A8B;
}

/* Title styling */
h1 {
    text-align: center;
    color: white !important;
    font-weight: 700;
    font-size: 40px;
    margin-bottom: 20px;
}

/* Buttons */
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

/* Hover effect */
.stButton > button:hover {
    background-color: #c29e8e;
    transform: translateY(-2px);
}

/* Link buttons */
.stLinkButton a {
    display: block !important;
    width: 100% !important;
    text-align: center !important;
    background-color: #654f41 !important;
    color: white !important;
    border-radius: 12px;
    padding: 14px 16px;
    font-weight: 600;
    transition: all 0.2s ease;
}

/* Link button hover */
.stLinkButton a:hover {
    background-color: #c29e8e !important;
    transform: translateY(-2px);
}

/* Center images inside container */
.stContainer {
    display: flex;
    justify-content: center;
    align-items: center;
}

[data-testid="stImage"] {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
</style>
""", unsafe_allow_html=True)
#_____________________________________________________________________________________________
# # Load your data (adjust filename!)
# df = pd.read_csv("Spellenhuis Bordspellen Library - Library.csv")
# #_____________________________________________________________________________________________
# # Prepare dataframe
# df['Type'] = df['Type'].str.split(',').str[-1].str.strip()
# df['Playing Time'] = df['Playing Time'].str[:-3].str.strip()
# df[['Min Playing Time', 'Max Playing Time']] = (df['Playing Time'].str.split('-', expand=True))
# df['Max Playing Time'] = df['Max Playing Time'].fillna(df['Min Playing Time'])
# df['Max Playing Time'] = pd.to_numeric(df['Max Playing Time'], errors='coerce')

#_____________________________________________________________________________________________
# Main Page

left, center, right = st.columns([1, 2, 1])

with center:
    st.image("https://www.spellenhuis.nl/media/8a/65/ae/1634638327/spellenhuislogo.png", use_column_width=True)

    st.write("")  # add some vertical space
    st.title("Spellenhuis Game Library")
    st.write("") 

    if st.button("Zoek Specifiek Spel"):
        st.switch_page("pages/Search_Game.py")
    
    # Suggestion button
    if st.button("Vind Spelsuggestie"):
        st.switch_page("pages/Filter_Game.py")
    
    # # Recommendation button
    # if st.button("Zoek Vergelijkbare Spellen"):
    #     st.switch_page("pages/Recommend_Game.py")



#_____________________________________________________________________________________________
# Search button


# # Guru button
# if st.button("Guru's Only"):
#     st.switch_page("pages/Gurus.py")
# st.divider()

# #_____________________________________________________________________________________________
# # Main page
# st.subheader("Filter Options")

# # Players
# use_players = st.toggle("Filter by Amount of Players")
# if use_players:
#     amount_player = st.number_input("Amount of Players", min_value=1, step=1)

# # Language
# use_language = st.toggle("Filter by Language")
# if use_language:
#     language = st.selectbox("Language", ['Dutch', 'English'])

# # Type
# use_type = st.toggle("Filter by Game Type")
# if use_type:
#     game_type = st.selectbox("Game Type",["Abstract","Children's", 'Family', 'Party', 'Strategy', 'Thematic'])

# # Playing Time
# use_playing_time = st.toggle("Filter by Maximum Playing Time")
# if use_playing_time:
#     playing_time = st.number_input("Maximum Playing Time (minutes)", min_value=10, step=5)

# st.divider()

# if st.button("Filter Games"):
#     filtered = df.copy()

#     if use_players:
#         filtered = filtered[(filtered['Min. Players'] <= amount_player) & (filtered['Max. Players'] >= amount_player)]

#     if use_language:
#         filtered = filtered[filtered['Language'] == language]

#     if use_type:
#         filtered = filtered[filtered['Type'] == game_type]

#     if use_playing_time:
#         filtered = filtered[filtered['Max Playing Time'] <= playing_time]

#     if filtered.empty:
#         st.warning("No game can be found")
#     else:
#         st.write(filtered['Boardgame'])
