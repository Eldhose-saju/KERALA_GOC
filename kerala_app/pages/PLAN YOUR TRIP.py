import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Kerala Tour Planner", layout="wide")

st.title("Plan Your Kerala Trip 🏝️")

# Function to fetch locations from OpenStreetMap (Overpass API)
def get_places(category, lat, lon, radius=5000):
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    (node["tourism"="{category}"](around:{radius},{lat},{lon});
     node["amenity"="{category}"](around:{radius},{lat},{lon});
    );
    out body;
    """
    response = requests.get(overpass_url, params={'data': query})
    data = response.json()
    places = []
    if "elements" in data:
        for element in data["elements"]:
            name = element["tags"].get("name", "Unnamed")
            places.append(name)
    return places

# User Inputs
start_location = st.text_input("Enter Starting Point (Kerala)")
destination = st.text_input("Enter Destination (Kerala)")

if start_location and destination:
    st.subheader("Trip Details")
    
    # Fetch and display popular places
    st.write("### Popular Places to Visit")
    places_to_visit = get_places("attraction", 10.8505, 76.2711)  # Approximate Kerala center
    st.write(places_to_visit if places_to_visit else "No tourist spots found.")
    
    # Fetch and display best-rated food spots
    st.write("### Best Rated Food Spots")
    food_spots = get_places("restaurant", 10.8505, 76.2711)
    st.write(food_spots if food_spots else "No food spots found.")
    
    # Fetch and display hospitals
    st.write("### Hospitals on the Way")
    hospitals = get_places("hospital", 10.8505, 76.2711)
    st.write(hospitals if hospitals else "No hospitals found.")
    
    # Fetch and display petrol pumps
    st.write("### Petrol Pumps on the Way")
    petrol_pumps = get_places("fuel", 10.8505, 76.2711)
    st.write(petrol_pumps if petrol_pumps else "No petrol pumps found.")
    
    # Show on Map Button
    if st.button("Show on Map"):
        st.session_state["map_data"] = {
            "start": start_location,
            "end": destination,
            "places_to_visit": places_to_visit,
            "food_spots": food_spots,
            "hospitals": hospitals,
            "petrol_pumps": petrol_pumps
        }
        st.switch_page("MAP.py")  # Redirect to map page

