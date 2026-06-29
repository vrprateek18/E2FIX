import streamlit as st

from utils.charts import (
    environmental_bar_chart,
    environmental_radar_chart
)

# ==========================================================
# ENGINE SCORE CONVERTER
# ==========================================================

def engine_score(level):

    scores = {

        "Low": 85,

        "Moderate": 60,

        "High": 30,

        "Critical": 10

    }

    return scores.get(level,50)


# ==========================================================
# ENVIRONMENT HEALTH
# ==========================================================

def environmental_health(score):

    if score >= 85:

        return (

            "Excellent",

            "🟢"

        )

    elif score >= 70:

        return (

            "Good",

            "🟢"

        )

    elif score >= 50:

        return (

            "Moderate",

            "🟡"

        )

    else:

        return (

            "Poor",

            "🔴"

        )


# ==========================================================
# SHOW ANALYTICS
# ==========================================================

def show_analytics(data):

    st.subheader("📈 Environmental Analytics")

    health, emoji = environmental_health(

        data["score"]

    )

    st.info(

        f"{emoji} Overall Environmental Health : {health}"

    )

    radar_data = {

        "Green": engine_score(

            data["green"]

        ),

        "Noise": engine_score(

            data["noise"]

        ),

        "Water": engine_score(

            data["water"]

        ),

        "Waste": engine_score(

            data["waste"]

        ),

        "Heat": engine_score(

            data["heat"]

        )

    }

    radar = environmental_radar_chart(

        radar_data

    )

    st.plotly_chart(

    radar,

    use_container_width=True,

    key="environment_radar"

    )

    parameter_data = {

        "AQI": data["aqi"],

        "Temperature": data["temperature"],

        "Humidity": data["humidity"],

        "Wind": data["wind"]

    }

    bar = environmental_bar_chart(

        parameter_data

    )

    st.plotly_chart(

    bar,

    use_container_width=True,

    key="environment_bar"

    )

    st.markdown("### 📋 Analytics Summary")

    st.write(

        f"""

• Environmental Score : **{data['score']}**

• AQI : **{data['aqi']}**

• Green Status : **{data['green']}**

• Noise Status : **{data['noise']}**

• Water Status : **{data['water']}**

• Waste Status : **{data['waste']}**

• Heat Status : **{data['heat']}**

"""
    )


