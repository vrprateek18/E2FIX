# ==========================================================
# E2FIX
# Environmental Analysis
# ==========================================================

import streamlit as st



# -----------------------------
# Database
# -----------------------------
from database.environment_history import (
    save_environment_record
)



# -----------------------------
# UI
# -----------------------------

from utils.ui import (
    load_css,
    page_header,
    footer
)

# -----------------------------
# Components
# -----------------------------

from components.location import (
    select_location
)

from components.dashboard import (
    show_environment_dashboard
)

from components.analytics import (
    show_analytics
)

from components.recommendation import (
    show_recommendations
)

# -----------------------------
# Data Layer
# -----------------------------

from data_layer.aqi_service import get_aqi
from data_layer.weather_service import get_weather

# -----------------------------
# Logic Layer
# -----------------------------

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
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Environmental Analysis",

    page_icon="🌍",

    layout="wide"

)

load_css()

page_header(

    "🌍 Environmental Analysis",

    "AI Powered Environmental Decision Support System"

)


# ==========================================================
# ANALYSIS ENGINE
# ==========================================================

def analyze_environment(location):

    if location["latitude"] is None:

        return None

    aqi = get_aqi(

        location["latitude"],

        location["longitude"]

    )

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

        "green":green,

        "noise":noise,

        "water":water,

        "waste":waste

    }

    score = calculate_environment_score(

        {

            "aqi":aqi

        },

        proxies

    )

    return {

        "aqi":aqi,

        "temperature":temperature,

        "humidity":humidity,

        "wind":wind,

        "green":green,

        "noise":noise,

        "water":water,

        "waste":waste,

        "heat":heat,

        "score":score

    }


# ==========================================================
# MAIN
# ==========================================================

def main():

    location = select_location()

    st.markdown("")

    analyze = st.button(
        "🔍 Analyze Environment",
        use_container_width=True,
        type="primary"
    )

    if analyze:

        with st.spinner("Analyzing Environment..."):

            analysis = analyze_environment(location)

            if analysis is None:

                st.error(
                    "Unable to analyze the selected location."
                )

                return

            # ==========================================================
            # SAVE ENVIRONMENT HISTORY
            # ==========================================================

            history_data = {

                "location": location["location"],

                "latitude": location["latitude"],

                "longitude": location["longitude"],

                "aqi": analysis["aqi"],
                
                "temperature": analysis["temperature"],

                "humidity": analysis["humidity"],

                "wind": analysis["wind"],

                "green": analysis["green"],

                "noise": analysis["noise"],

                "water": analysis["water"],

                "waste": analysis["waste"],

                "heat": analysis["heat"],

                "environmental_score": analysis["score"],

                "projected_score": analysis["score"],

                "carbon_saved": 0,

                "carbon_credits": 0,

                "recovery_bonus": 0

            }

            save_environment_record(history_data)

            st.toast(
                "✅ Environmental Analysis saved successfully.",
                icon="🌍"
            )

            show_environment_dashboard(
                analysis
            )

            show_analytics(
                analysis
            )

            show_recommendations(
                analysis
            )

    footer()


if __name__ == "__main__":
    main()




