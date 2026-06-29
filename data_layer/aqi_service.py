import os
from dotenv import load_dotenv
import requests

load_dotenv()

AQI_API_TOKEN = os.getenv("AQI_API_TOKEN")

def get_aqi(lat, lon):

    try:

        url = f"https://api.waqi.info/feed/geo:{lat};{lon}/?token={AQI_API_TOKEN}"

        response = requests.get(url, timeout=10)

        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)

        data = response.json()

        if data.get("status") == "ok":

            aqi = data["data"].get("aqi")

            print("AQI =", aqi)

            return aqi

        print("AQI ERROR:", data)

        return None

    except Exception as e:

        print("AQI FETCH ERROR:", e)

        return None