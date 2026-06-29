# ==========================================================
# ENVIRONMENT DASHBOARD
# ==========================================================

import streamlit as st

from components.cards import (
    kpi_card,
    status_card,
    score_card
)

from utils.charts import (
    environmental_gauge,
    environmental_bar_chart,
    environmental_radar_chart
)


# ==========================================================
# ENVIRONMENT DASHBOARD
# ==========================================================

def show_environment_dashboard(data):

    st.divider()

    st.subheader("🌍 Environmental Dashboard")

    # ======================================================
    # LIVE DATA
    # ======================================================

    st.markdown("### 📊 Live Environmental Data")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        kpi_card(
            "AQI",
            data["aqi"],
            "🌫"
        )

    with c2:
        kpi_card(
            "Temperature",
            f'{data["temperature"]} °C',
            "🌡"
        )

    with c3:
        kpi_card(
            "Humidity",
            f'{data["humidity"]}%',
            "💧"
        )

    with c4:
        kpi_card(
            "Wind",
            f'{data["wind"]} m/s',
            "🌬"
        )

    # ======================================================
    # ENVIRONMENT ENGINES
    # ======================================================

    st.markdown("### 🌿 Environmental Engines")

    e1, e2, e3, e4, e5 = st.columns(5)

    with e1:
        status_card("Green", data["green"])

    with e2:
        status_card("Noise", data["noise"])

    with e3:
        status_card("Water", data["water"])

    with e4:
        status_card("Waste", data["waste"])

    with e5:
        status_card("Heat", data["heat"])

    # ======================================================
    # SCORE
    # ======================================================

    st.markdown("### 🎯 Environmental Score")

    score_card(data["score"])

    # ======================================================
    # ANALYTICS
    # ======================================================

    st.markdown("### 📈 Environmental Analytics")

    left, right = st.columns(2)

    with left:

        gauge = environmental_gauge(
            data["score"]
        )

        st.plotly_chart(
            gauge,
            use_container_width=True,
            key="dashboard_gauge"
        )

    with right:

        radar_data = {

            "Green": 85 if data["green"] == "Low" else 60 if data["green"] == "Moderate" else 30,

            "Noise": 85 if data["noise"] == "Low" else 60 if data["noise"] == "Moderate" else 30,

            "Water": 85 if data["water"] == "Low" else 60 if data["water"] == "Moderate" else 30,

            "Waste": 85 if data["waste"] == "Low" else 60 if data["waste"] == "Moderate" else 30,

            "Heat": 85 if data["heat"] == "Low" else 60 if data["heat"] == "Moderate" else 30

        }

        radar = environmental_radar_chart(
            radar_data
        )

        st.plotly_chart(
            radar,
            use_container_width=True,
            key="dashboard_radar"
        )

    # ======================================================
    # BAR CHART
    # ======================================================

    st.markdown("### 📊 Environmental Parameters")

    bar = environmental_bar_chart(

        {

            "AQI": data["aqi"],

            "Temperature": data["temperature"],

            "Humidity": data["humidity"],

            "Wind": data["wind"]

        }

    )

    st.plotly_chart(

        bar,

        use_container_width=True,

        key="dashboard_bar"

    )

    # ======================================================
    # SUMMARY
    # ======================================================

    st.markdown("### 📋 Environmental Summary")

    score = data["score"]

    if score >= 80:

        st.success(
            "🟢 Excellent environmental condition. Continue maintaining sustainability."
        )

    elif score >= 60:

        st.warning(
            "🟡 Moderate environmental condition. Improvement is recommended."
        )

    else:

        st.error(
            "🔴 Poor environmental condition. Immediate recovery actions are required."
        )