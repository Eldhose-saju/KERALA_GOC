import requests
import streamlit as st

# Function to fetch weather data using OpenWeatherMap API
def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            weather_info = {
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].capitalize(),
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            return weather_info
        else:
            return None
    except Exception as e:
        return None
