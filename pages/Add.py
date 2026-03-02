import streamlit as st
import pandas as pd

# Load your live sheet
sheet_url = "https://docs.google.com/spreadsheets/d/1Lf9Rs121pEpCPjAhEC7pk00ffvmOim51vLmrUePJP5A/export?format=csv&gid=0"
df = pd.read_csv(sheet_url)

def format_playing_time(playtime):
    """
    Ensure playing time ends with 'Min'.
    """
    playtime = playtime.strip()
    if playtime.lower().endswith("Min"):
        return playtime

    return playtime + " Min"
    
st.title("Voeg nieuw spel toe")
st.info("""
Met deze form kun je bordspellen die geopend zijn voor onze gamelibrary toevoegen aan onze database. Het is belangrijk dat de informatie wordt overgenomen van Board Game Geek. 
Daarnaast is het belangrijk dat iedereen hetzelfde format gebruikt zodat onze database gelijk blijft. Hieronder een voorbeeld van het juist invoeren van een nieuw borspel.

**Instructions:**
- `Plaats` = B 
- `Plank` = 2 
- `Aantal` = 1
- `Naam` = Secret Hitler (2016)
- `Minimum Spelers` = 5
- `Maximum Spelers` = 10
- `Tijdsduur` = 30-45 Min
- `Moeilijkheidsgraad` = 1.74
- `Taal` = English
- `Type` = Party
- `Categorie` = Bluffing, Card Game, Deduction, Humor, Party Game, Political, Print & Play, Spies / Secret Agents
- `Mechanisme` = Hidden Roles, Player Elimination, Team-Based Game, Traitor Game, Voting
""")

with st.form("add_game_form"):
    letter = st.selectbox("Plaats (A-G)", ["A","B","C","D","E","F","G"])
    number = st.number_input("Plank (1-5)", min_value=1, max_value=5, step=1)
    quantity = st.number_input("Aantal", min_value=1, step=1, value=1)
    name = st.text_input("Naam (bv. Monsters of Loch Lomond (2023))")
    min_players = st.number_input("Minimum Spelers", min_value=1, step=1)
    max_players = st.number_input("Maximum Spelers", min_value=min_players, step=1)
    playing_time = st.text_input("Tijdsduur (e.g. 30 Min or 15-30 Min)")
    complexity = st.number_input("Moelijkheidsgraad (BGG)", min_value=1.0, max_value=5.0, step=0.01)
    language = st.selectbox("Taal", ["Dutch","English"])
    game_type = st.selectbox("Type", ["Abstract","Children","Family","Narrative","Party","Strategy","Two-Player"])
    category = st.text_input("Categorie (bv. Card Game, Party Game, Real-time)")
    mechanism = st.text_input("Mechanisme (bv. Hot Potato, Pattern Recognition, Speed Matching)")

    submitted = st.form_submit_button("Create Row")

    if submitted:
        # Build a dictionary of the new row
        new_row = {
            "Letter": letter,
            "Number": number,
            "#": quantity,
            "Boardgame": name,
            "Min. Players": min_players,
            "Max. Players": max_players,
            "Playing Time": format_playing_time(playing_time),
            "Complexity (BGG)": complexity,
            "Language": language,
            "Type": game_type,
            "Categories": category,
            "Mechanisms": mechanism
        }

        # Convert to dataframe for display/download
        new_row_df = pd.DataFrame([new_row])

        st.success("Row created! You can copy it into your Google Sheet or download as CSV.")
        st.dataframe(new_row_df)

        # Option to download
        csv = new_row_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", data=csv, file_name="new_boardgame.csv", mime="text/csv")
