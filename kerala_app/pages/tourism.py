import streamlit as st
import folium
from streamlit_folium import folium_static

# Set page configuration
st.set_page_config(page_title="Tourism - Kerala", layout="wide")

# Dictionary of tourist destinations with coordinates
destinations = {
    "Munnar": [10.0889, 77.0595],
    "Alleppey": [9.4981, 76.3388],
    "Kumarakom": [9.6062, 76.4305],
    "Kovalam": [8.4021, 76.9787],
    "Thekkady": [9.6061, 77.1515],
    "Wayanad": [11.6854, 76.1320],
    "Varkala": [8.7379, 76.7163]
}

# Default location (center of Kerala)
default_location = [10.8505, 76.2711] 

# Sidebar to select a destination
st.sidebar.title("Tourist Destinations")
selected_place = st.sidebar.radio("Click to View on Map", list(destinations.keys()))

# Create a folium map centered at the selected location
map_center = destinations.get(selected_place, default_location)
m = folium.Map(location=map_center, zoom_start=8)

# Add marker for the selected place
folium.Marker(location=map_center, popup=selected_place, icon=folium.Icon(color="blue")).add_to(m)

# Display the map
st.write(f"### Explore {selected_place}")
folium_static(m)
