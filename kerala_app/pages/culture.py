import streamlit as st
import datetime
from googletrans import Translator

# Set page configuration
st.set_page_config(page_title="Culture - Kerala", layout="wide")

# Title
st.title("Explore Kerala's Rich Culture")

# Festival Calendar
st.subheader("🎉 Festival Calendar")

festivals = {
    "Onam": {"date": "August - September", "info": "Onam is Kerala's biggest festival, celebrated with pookalam, sadya, and Vallamkali (boat race)."},
    "Vishu": {"date": "April 14", "info": "Vishu marks Kerala's New Year with Vishukkani, firecrackers, and feasts."},
    "Thrissur Pooram": {"date": "April - May", "info": "A grand temple festival in Thrissur, famous for elephant processions and fireworks."},
    "Attukal Pongala": {"date": "February - March", "info": "A women's only festival where devotees prepare pongala (sweet offering) for the goddess."},
    "Theyyam": {"date": "December - April", "info": "A ritualistic performance art featuring colorful costumes and spiritual significance."}
}

selected_festival = st.selectbox("Select a festival to learn more:", list(festivals.keys()))

st.write(f"**Date:** {festivals[selected_festival]['date']}")
st.write(f"**About:** {festivals[selected_festival]['info']}")

# English-to-Malayalam Translator
st.subheader("🌍 English-to-Malayalam Translator")
translator = Translator()

text_to_translate = st.text_input("Enter text in English:")
if text_to_translate:
    translation = translator.translate(text_to_translate, src='en', dest='ml')
    st.write("**Malayalam Translation:**", translation.text)
