import streamlit as st
import folium
from streamlit_folium import folium_static
from weather import get_weather  # Import weather function

# Set page configuration
st.set_page_config(page_title="Tourism - Kerala", layout="wide")

# Dictionary of tourist destinations with details
destinations = {
    "Munnar": {
        "location": [10.0889, 77.0595],
        "info": "Munnar is a hill station famous for tea plantations and beautiful landscapes.",
        "best_time": "September to March"
    },
    "Alleppey": {
        "location": [9.4981, 76.3388],
        "info": "Known as the 'Venice of the East,' Alleppey is famous for its backwaters and houseboats.",
        "best_time": "November to February"
    },
    "Kumarakom": {
        "location": [9.6062, 76.4305],
        "info": "A serene backwater destination known for bird sanctuaries and houseboat cruises.",
        "best_time": "September to March"
    },
    "Kovalam": {
        "location": [8.4021, 76.9787],
        "info": "A popular beach destination known for its crescent-shaped coastline.",
        "best_time": "October to February"
    },
    "Thekkady": {
        "location": [9.6061, 77.1515],
        "info": "Home to Periyar Wildlife Sanctuary, famous for elephants and spice plantations.",
        "best_time": "September to May"
    },
    "Wayanad": {
        "location": [11.6854, 76.1320],
        "info": "A nature lover's paradise with waterfalls, caves, and wildlife.",
        "best_time": "October to May"
    },
    "Varkala": {
        "location": [8.7379, 76.7163],
        "info": "Famous for cliffs, beaches, and the Janardhana Swamy Temple.",
        "best_time": "November to February"
    }
}

# Default location (center of Kerala)
default_location = [10.8505, 76.2711] 

# Sidebar: Select a destination
st.sidebar.title("Tourist Destinations")
selected_place = st.sidebar.radio("Click to View on Map", list(destinations.keys()))

# Get details for the selected place
place_data = destinations[selected_place]
map_center = place_data["location"]

# Create a folium map centered at the selected location
m = folium.Map(location=map_center, zoom_start=10)

# Add marker for the selected place
folium.Marker(location=map_center, popup=selected_place, icon=folium.Icon(color="blue")).add_to(m)

# Display the map
st.write(f"## Explore {selected_place}")
folium_static(m)

# Display tourist information
st.write("### About the Place")
st.write(place_data["info"])

# Display best time to visit
st.write(f"**Best Time to Visit:** {place_data['best_time']}")

# Fetch and display live weather
st.write("### Current Weather")
weather_data = get_weather(selected_place)
if weather_data:
    st.write(f"🌡️ Temperature: {weather_data['temperature']}°C")
    st.write(f"☁️ Condition: {weather_data['description']}")
    st.write(f"💧 Humidity: {weather_data['humidity']}%")
    st.write(f"💨 Wind Speed: {weather_data['wind_speed']} m/s")
else:
    st.write("⚠️ Weather data not available.")
