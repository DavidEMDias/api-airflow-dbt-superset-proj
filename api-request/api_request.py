import requests
import os


API_KEY = os.getenv("API_KEY")
API_URL = f"http://api.weatherstack.com/current?access_key={API_KEY}&query=Lisbon"


def fetch_data():
    print("Fetching weather data from Weatherstack API...")
    #try - except block to be notified of the status (success or not)
    try:
        response = requests.get(API_URL)
        response.raise_for_status() #400/500 HTTP errors
        print("API response received successfully.")
        print(response)
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}.")
        raise

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Lisbon, Portugal', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Lisbon', 'country': 'Portugal', 'region': 'Lisboa', 'lat': '38.717', 'lon': '-9.133', 'timezone_id': 'Europe/Lisbon', 'localtime': '2025-12-30 12:12', 'localtime_epoch': 1767096720, 'utc_offset': '0.0'}, 'current': {'observation_time': '12:12 PM', 'temperature': 7, 'weather_code': 248, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0007_fog.png'], 'weather_descriptions': ['Fog'], 'astro': {'sunrise': '07:54 AM', 'sunset': '05:24 PM', 'moonrise': '01:36 PM', 'moonset': '03:25 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 74}, 'air_quality': {'co': '211.85', 'no2': '20.55', 'o3': '25', 'so2': '4.35', 'pm2_5': '17.75', 'pm10': '23.75', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 9, 'wind_degree': 81, 'wind_dir': 'E', 'pressure': 1022, 'precip': 0, 'humidity': 100, 'cloudcover': 75, 'feelslike': 6, 'uv_index': 2, 'visibility': 0, 'is_day': 'yes'}}