import os
from dotenv import load_dotenv
import requests

load_dotenv()

AQI_API_TOKEN = os.getenv("AQI_API_TOKEN")


def get_aqi(lat, lon):

    try:

        url = f"https://api.waqi.info/feed/geo:{lat};{lon}/?token={AQI_API_TOKEN}"

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        if data.get("status") == "ok":

            aqi = data["data"].get("aqi")

            # Ensure AQI is always numeric
            if aqi is None or aqi == "-":
                return 0

            return int(aqi)

        print("AQI ERROR:", data)
        return 0

    except Exception as e:

        print("AQI FETCH ERROR:", e)
        return 0