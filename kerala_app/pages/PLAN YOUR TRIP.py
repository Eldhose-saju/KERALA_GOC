import streamlit as st
import datetime
import folium
from streamlit_folium import folium_static
from geopy.distance import geodesic

# Set page configuration
st.set_page_config(page_title="Kerala Tour Planner", layout="wide")

st.title("Plan Your Kerala Trip 🏝️")

# Date Picker for trip planning
st.subheader("Select Your Travel Dates")
start_date = st.date_input("Start Date", datetime.date.today())
end_date = st.date_input("End Date", datetime.date.today())

if start_date > end_date:
    st.error("End date should be after start date")

# Destination selection
st.subheader("Choose Your Destinations")

# Allow users to input any place in Kerala
start_location = st.text_input("Enter Starting Point (Any location in Kerala)")
end_location = st.text_input("Enter Destination (Any location in Kerala)")

if start_location and end_location:
    st.write(f"**Distance and Route Information for {start_location} to {end_location}:**")
    
    # Placeholder for distance and travel time (actual calculation needs API integration)
    st.write("📍 Distance: Approximate calculation required.")
    st.write("🚗 Estimated Travel Time: To be determined.")
    
    # Map View
    st.subheader("View Route on Map")
    if st.button("Show Route Map"):
        route_map = folium.Map(location=[10.8505, 76.2711], zoom_start=7)  # Centered on Kerala
        folium.Marker([10.8505, 76.2711], tooltip=start_location, icon=folium.Icon(color="blue")).add_to(route_map)
        folium.Marker([10.8505, 76.2711], tooltip=end_location, icon=folium.Icon(color="red")).add_to(route_map)
        folium.PolyLine([[10.8505, 76.2711], [10.8505, 76.2711]], color="green", weight=5).add_to(route_map)
        folium_static(route_map)
