import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
import openrouteservice

# Set page configuration
st.set_page_config(page_title="Kerala Tour Planner", layout="wide")

st.title("Plan Your Kerala Trip 🏝️")

# Initialize geocoder and OpenRouteService client
geolocator = Nominatim(user_agent="kerala_tour_planner")
client = openrouteservice.Client(key="your_openrouteservice_api_key")

# Function to get coordinates from location name
def get_coordinates(place):
    location = geolocator.geocode(place, country_codes='IN')
    return (location.latitude, location.longitude) if location else None

# Destination selection
st.subheader("Choose Your Destinations")

start_location = st.text_input("Enter Starting Location in Kerala")
end_location = st.text_input("Enter Destination in Kerala")

if start_location and end_location:
    start_coords = get_coordinates(start_location)
    end_coords = get_coordinates(end_location)
    
    if start_coords and end_coords:
        try:
            route = client.directions(coordinates=[start_coords[::-1], end_coords[::-1]], profile='driving-car', format='geojson')
            distance = route['routes'][0]['summary']['distance'] / 1000  # Convert meters to km
            duration = route['routes'][0]['summary']['duration'] / 3600  # Convert seconds to hours
            
            st.write(f"**Distance between {start_location} and {end_location}:** {distance:.2f} km")
            st.write(f"**Estimated Travel Time (by road):** {duration:.2f} hours")
            
            # Map View
            st.subheader("View Route on Map")
            if st.button("Show Route Map"):
                route_map = folium.Map(location=start_coords, zoom_start=7)
                folium.Marker(start_coords, tooltip=start_location, icon=folium.Icon(color="blue")).add_to(route_map)
                folium.Marker(end_coords, tooltip=end_location, icon=folium.Icon(color="red")).add_to(route_map)
                folium.PolyLine([(point[1], point[0]) for point in route['routes'][0]['geometry']['coordinates']], color="blue", weight=5, opacity=0.7).add_to(route_map)
                folium_static(route_map)
        except Exception as e:
            st.error("Could not fetch route. Please check the locations and try again.")
    else:
        st.error("Could not find coordinates for one or both locations. Please check spelling.")