import streamlit as st
from deep_translator import GoogleTranslator  # Using deep-translator for translation

# Set page configuration
st.set_page_config(page_title="Culture - Kerala", layout="wide")

# Title
st.title("Explore Kerala's Rich Culture")

# Brief on Kerala's Culture
st.subheader("About Kerala's Culture")
st.write("Kerala, known as ‘God’s Own Country,’ boasts a rich cultural heritage blending traditions, art, and festivals. It is famous for classical dance forms like Kathakali and Mohiniyattam, vibrant festivals like Onam and Thrissur Pooram, and unique rituals like Theyyam. The cuisine, music, and literature reflect a deep-rooted history and diversity.")

# English-to-Malayalam Translator
st.subheader("🌍 English-to-Malayalam Translator")
text_to_translate = st.text_input("Enter text in English:")

if text_to_translate:
    translation = GoogleTranslator(source='en', target='ml').translate(text_to_translate)
    st.write("**Malayalam Translation:**", translation)
