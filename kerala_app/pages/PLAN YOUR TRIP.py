import streamlit as st
from geopy.geocoders import Nominatim
import requests

# Set page configuration
st.set_page_config(page_title="Kerala Tour Planner", layout="wide")

st.title("Plan Your Kerala Trip 🏝️")

# Function to get location coordinates
def get_coordinates(place):
    geolocator = Nominatim(user_agent="kerala_trip_planner")
    location = geolocator.geocode(place)
    if location:
        return (location.latitude, location.longitude)
    return None

# Destination selection
st.subheader("Choose Your Destinations")
start_location = st.text_input("Enter Starting Point")
end_location = st.text_input("Enter Destination")

if start_location and end_location:
    start_coords = get_coordinates(start_location)
    end_coords = get_coordinates(end_location)
    
    if start_coords and end_coords:
        st.write(f"**Start Location:** {start_location} ({start_coords})")
        st.write(f"**Destination:** {end_location} ({end_coords})")
        
        # Get travel time estimate (approximate by road speed of 40 km/h)
        distance_api = f"https://router.project-osrm.org/route/v1/driving/{start_coords[1]},{start_coords[0]};{end_coords[1]},{end_coords[0]}?overview=false"
        response = requests.get(distance_api).json()
        if "routes" in response and response["routes"]:
            distance = response["routes"][0]["distance"] / 1000  # Convert meters to km
            travel_time = distance / 40  # Assuming avg speed of 40 km/h
            st.write(f"**Distance:** {distance:.2f} km")
            st.write(f"**Estimated Travel Time:** {travel_time:.2f} hours")
        else:
            st.write("Could not fetch travel distance.")
        
        # Fetch nearby attractions using OpenStreetMap Overpass API
        overpass_url = "http://overpass-api.de/api/interpreter"
        query = f"""
        [out:json];
        (node["tourism"="attraction"](around:50000,{(start_coords[0] + end_coords[0]) / 2},{(start_coords[1] + end_coords[1]) / 2});
        );
out body;
        """
        response = requests.get(overpass_url, params={"data": query}).json()
        attractions = [node["tags"].get("name", "Unknown Attraction") for node in response.get("elements", [])]
        
        if attractions:
            st.subheader("Popular Places to Visit on the Way")
            for attraction in attractions[:5]:  # Show top 5 attractions
                st.write(f"- {attraction}")
        else:
            st.write("No attractions found on the route.")
        
        # Fetch food spots using Overpass API
        query_food = f"""
        [out:json];
        (node["amenity"="restaurant"](around:50000,{(start_coords[0] + end_coords[0]) / 2},{(start_coords[1] + end_coords[1]) / 2});
        );
out body;
        """
        response = requests.get(overpass_url, params={"data": query_food}).json()
        food_spots = [node["tags"].get("name", "Unnamed Restaurant") for node in response.get("elements", [])]
        
        if food_spots:
            st.subheader("Best Rated Food Spots on the Way")
            for food in food_spots[:5]:  # Show top 5 food spots
                st.write(f"- {food}")
        else:
            st.write("No food spots found on the route.")
        
        # Fetch hospitals using Overpass API
        query_hospitals = f"""
        [out:json];
        (node["amenity"="hospital"](around:50000,{(start_coords[0] + end_coords[0]) / 2},{(start_coords[1] + end_coords[1]) / 2});
        );
out body;
        """
        response = requests.get(overpass_url, params={"data": query_hospitals}).json()
        hospitals = [node["tags"].get("name", "Unnamed Hospital") for node in response.get("elements", [])]
        
        if hospitals:
            st.subheader("Hospitals on the Way")
            for hospital in hospitals[:5]:  # Show top 5 hospitals
                st.write(f"- {hospital}")
        else:
            st.write("No hospitals found on the route.")
    else:
        st.write("Could not find location coordinates. Please enter valid Kerala places.")
