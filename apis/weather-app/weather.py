"""
Weather App - Get current weather for any city
Uses OpenWeatherMap API
"""

import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

print("WEATHER APP")

if not API_KEY:
    print("Error: API key not found. Make sure you have a .env file with OPENWEATHER_API_KEY")
    exit()

print("API key loaded successfully")
print("")
print("TESTING API CONNECTION")
print("")

# Test with a default city
city = "London"
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    print(f"Making request for: {city}")
    response = requests.get(BASE_URL, params=params)
    
    print(f"Status code: {response.status_code}")
    
    if response.status_code == 200:
        print("Connection successful!")
        
        data = response.json()
        print("")
        print("WEATHER DATA")
        print("")
        
        # Extract data from JSON
        city_name = data.get("name", "Unknown")
        country = data.get("sys", {}).get("country", "")
        temperature = data.get("main", {}).get("temp", "N/A")
        feels_like = data.get("main", {}).get("feels_like", "N/A")
        humidity = data.get("main", {}).get("humidity", "N/A")
        pressure = data.get("main", {}).get("pressure", "N/A")
        description = data.get("weather", [{}])[0].get("description", "N/A").capitalize()
        wind_speed = data.get("wind", {}).get("speed", "N/A")
        
        # Display formatted data
        print(f"Location: {city_name}, {country}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Conditions: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind speed: {wind_speed} m/s")
        
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        
except requests.exceptions.RequestException as e:
    print(f"Connection error: {e}")