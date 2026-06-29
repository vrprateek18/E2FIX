import os
from dotenv import load_dotenv
import requests

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(lat, lon):

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "lat": float(lat),
            "lon": float(lon),
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params, timeout=10)

        print("STATUS:", response.status_code)
        print("DATA:", response.text)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }

    except Exception as e:
        print("ERROR:", e)
        return None