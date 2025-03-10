import streamlit as st

# Set page configuration
st.set_page_config(page_title="Kerala: God's Own Country", layout="wide")

# Background image CSS
def set_background(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_path}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call function with the correct image path
set_background("images/keralabkg.jpg")  # Ensure the image is inside the 'images' folder

# Main Content
st.markdown("<h1 style='text-align: center; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.6);'>Welcome to Kerala: God's Own Country</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.6);'>Explore the beauty, culture, and flavors of Kerala</h2>", unsafe_allow_html=True)

st.write("### About the App")
st.write("This interactive web app takes you on a journey through Kerala, showcasing its breathtaking tourist spots, vibrant culture, and mouthwatering food. Engage with interactive maps, quizzes, and authentic experiences.")

# Sidebar Navigation
st.sidebar.header("Explore More")  # Only keep the header, as Streamlit auto-lists pages
