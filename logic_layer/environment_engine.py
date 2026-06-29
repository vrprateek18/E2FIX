# ==========================================================
# ENVIRONMENT ENGINE
# ==========================================================

from data_layer.aqi_service import get_aqi
from data_layer.weather_service import get_weather

from logic_layer.hybrid_engine import (
    green_index,
    noise_index,
    water_index,
    waste_index
)

from logic_layer.scoring_engine import (
    calculate_environment_score
)


# ==========================================================
# ANALYZE ENVIRONMENT
# ==========================================================

def analyze_environment(location):

    """
    location = {
        "latitude": float,
        "longitude": float,
        "location": str
    }
    """

    if location is None:
        return None

    if location["latitude"] is None:
        return None


    # ----------------------------
    # Live AQI
    # ----------------------------

    aqi = get_aqi(

        location["latitude"],

        location["longitude"]

    )

    # ----------------------------
    # Weather
    # ----------------------------

    weather = get_weather(

        location["latitude"],

        location["longitude"]

    )

    if weather is None:

        return None


    temperature = weather["temperature"]

    humidity = weather["humidity"]

    wind = weather["wind_speed"]


    green = green_index(

        temperature,

        humidity,

        aqi

    )

    noise = noise_index(

        aqi,

        wind

    )

    water = water_index(

        temperature,

        humidity

    )

    waste = waste_index(

        aqi,

        temperature

    )

    if temperature >= 42:

        heat = "High"

    elif temperature >= 35:

        heat = "Moderate"

    else:

        heat = "Low"


    proxies = {

        "green": green,

        "noise": noise,

        "water": water,

        "waste": waste

    }

    score = calculate_environment_score(

        {

            "aqi": aqi

        },

        proxies

    )


    return {

        "location": location["location"],

        "latitude": location["latitude"],

        "longitude": location["longitude"],

        "aqi": aqi,

        "temperature": temperature,

        "humidity": humidity,

        "wind": wind,

        "green": green,

        "noise": noise,

        "water": water,

        "waste": waste,

        "heat": heat,

        "score": score

    }


