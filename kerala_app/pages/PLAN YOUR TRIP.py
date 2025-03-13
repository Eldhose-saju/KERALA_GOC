import streamlit as st
from geopy.geocoders import Nominatim
import requests

# Set page configuration
st.set_page_config(page_title="Kerala Tour Planner", layout="wide")

st.title("Plan Your Kerala Trip 🏝️")

# Input fields for start and end locations
start_location = st.text_input("Enter Starting Point")
end_location = st.text_input("Enter Destination")

def get_location_info(place):
    geolocator = Nominatim(user_agent="kerala_trip_planner")
    location = geolocator.geocode(place + ", Kerala, India")
    if location:
        return (location.latitude, location.longitude)
    return None

def fetch_places(category, lat, lon):
    api_url = f"https://api.example.com/places?category={category}&lat={lat}&lon={lon}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return []

if start_location and end_location:
    start_coords = get_location_info(start_location)
    end_coords = get_location_info(end_location)
    
    if start_coords and end_coords:
        st.write(f"**Starting Point:** {start_location}")
        st.write(f"**Destination:** {end_location}")
        
        # Fetch details along the route
        attractions = fetch_places("tourist_attractions", *end_coords)
        food_spots = fetch_places("restaurants", *end_coords)
        hospitals = fetch_places("hospitals", *end_coords)
        petrol_pumps = fetch_places("petrol_pumps", *end_coords)
        
        # Display information
        st.subheader("Popular Attractions")
        for place in attractions:
            st.write(f"- {place['name']}")
        
        st.subheader("Best-Rated Food Spots")
        for food in food_spots:
            st.write(f"- {food['name']}")
        
        st.subheader("Hospitals Along the Way")
        for hospital in hospitals:
            st.write(f"- {hospital['name']}")
        
        st.subheader("Petrol Pumps on the Route")
        for pump in petrol_pumps:
            st.write(f"- {pump['name']}")
        
        # Show on map button
        if st.button("Show on Map 🗺️"):
            st.session_state["map_data"] = {
                "start": start_coords,
                "end": end_coords,
                "attractions": attractions,
                "food": food_spots,
                "hospitals": hospitals,
                "petrol_pumps": petrol_pumps
            }
            st.switch_page("pages/MAP.py")