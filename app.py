{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2946d7b1-f9e5-498d-844d-c76aad9c7ad2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Load your data (adjust filename!)\n",
    "df = pd.read_csv(\"Spellenhuis Bordspellen Library - Library.csv\")\n",
    "\n",
    "st.title(\"🎲 Boardgame Filter\")\n",
    "\n",
    "min_player = st.text_input(\"Min Players\")\n",
    "max_player = st.text_input(\"Max Players\")\n",
    "language = st.text_input(\"Language\")\n",
    "game_type = st.text_input(\"Game Type\")\n",
    "\n",
    "if st.button(\"Filter Games\"):\n",
    "\n",
    "    min_player = int(min_player) if min_player else None\n",
    "    max_player = int(max_player) if max_player else None\n",
    "    language = language if language else None\n",
    "    game_type = game_type if game_type else None\n",
    "\n",
    "    filtered = df.copy()\n",
    "\n",
    "    if min_player is not None:\n",
    "        filtered = filtered[filtered['Min. Players'] == min_player]\n",
    "\n",
    "    if max_player is not None:\n",
    "        filtered = filtered[filtered['Max. Players'] == max_player]\n",
    "\n",
    "    if language is not None:\n",
    "        filtered = filtered[filtered['Language'] == language]\n",
    "\n",
    "    if game_type is not None:\n",
    "        filtered = filtered[filtered['Type'] == game_type]\n",
    "\n",
    "    if filtered.empty:\n",
    "        st.warning(\"No game can be found\")\n",
    "    else:\n",
    "        st.write(filtered['Boardgame'])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
