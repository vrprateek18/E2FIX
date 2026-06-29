# ==========================================================
# E2FIX
# Improvement Analytics
# ==========================================================

import streamlit as st
import pandas as pd

# -----------------------------
# UI
# -----------------------------
from utils.ui import (
    load_css,
    page_header,
    footer
)

# -----------------------------
# Database
# -----------------------------
from database.environment_history import (
    get_environment_history
)

# -----------------------------
# Charts
# -----------------------------
from utils.charts import (
    score_trend_chart,
    aqi_trend_chart,
    carbon_trend_chart,
    credits_trend_chart,
    recovery_progress_chart,
    environment_status_pie
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Improvement Analytics",

    page_icon="📈",

    layout="wide"

)

load_css()

page_header(

    "📈 Improvement Analytics",

    "Historical Environmental Analysis & Recovery Trends"

)

# ==========================================================
# LOAD HISTORY
# ==========================================================

rows = get_environment_history()

if len(rows) == 0:

    st.warning(

        "No Environmental Analysis Found."

    )

    st.stop()

history = pd.DataFrame([dict(row) for row in rows])


# ==========================================================
# FORMAT DATE
# ==========================================================

history["created_at"] = pd.to_datetime(

    history["created_at"]

)


st.subheader("📊 Environmental Summary")


# ==========================================================
# SUMMARY METRICS
# ==========================================================

latest_score = history.iloc[0]["environmental_score"]

best_score = history["environmental_score"].max()

average_aqi = round(history["aqi"].mean(), 1)

total_carbon = round(history["carbon_saved"].sum(), 2)

total_credits = round(history["carbon_credits"].sum(), 3)

total_analysis = len(history)


col1, col2, col3 = st.columns(3)

with col1:

    st.metric(

        "🌍 Latest Score",

        latest_score

    )

    st.metric(

        "🌫 Average AQI",

        average_aqi

    )

with col2:

    st.metric(

        "🏆 Best Score",

        best_score

    )

    st.metric(

        "♻ Carbon Saved",

        f"{total_carbon} kg"

    )

with col3:

    st.metric(

        "📊 Total Analysis",

        total_analysis

    )

    st.metric(

        "💳 Carbon Credits",

        total_credits

    )


st.divider()


# ==========================================================
# SCORE & AQI TREND
# ==========================================================

st.subheader("📈 Environmental Trends")

col1, col2 = st.columns(2)

with col1:

    fig = score_trend_chart(history)

    st.plotly_chart(

        fig,

        use_container_width=True,

        key="score_trend"

    )

with col2:

    fig = aqi_trend_chart(history)

    st.plotly_chart(

        fig,

        use_container_width=True,

        key="aqi_trend"

    )

# ==========================================================
# CARBON ANALYTICS
# ==========================================================

st.subheader("♻ Carbon Recovery Trends")

col1, col2 = st.columns(2)

with col1:

    fig = carbon_trend_chart(history)

    st.plotly_chart(

        fig,

        use_container_width=True,

        key="carbon_trend"

    )

with col2:

    fig = credits_trend_chart(history)

    st.plotly_chart(

        fig,

        use_container_width=True,

        key="credits_trend"

    )

# ==========================================================
# RECOVERY PROGRESS
# ==========================================================

st.subheader("🌱 Recovery Progress")

col1, col2 = st.columns(2)

with col1:

    fig = recovery_progress_chart(history)

    st.plotly_chart(

        fig,

        use_container_width=True,

        key="recovery_progress"

    )

with col2:

    fig = environment_status_pie(history)

    st.plotly_chart(

        fig,

        use_container_width=True,

        key="environment_status"

    )

# ==========================================================
# AI INSIGHT
# ==========================================================

st.subheader("🤖 AI Insight")

if latest_score >= 85:

    insight = "Excellent environmental performance. Maintain the current sustainability practices."

elif latest_score >= 70:

    insight = "Good environmental condition. Increasing green initiatives can further improve the score."

elif latest_score >= 50:

    insight = "Moderate environmental health. Focus on waste management and plantation drives."

else:

    insight = "Environmental health is poor. Immediate recovery measures are recommended."

st.info(insight)


# ==========================================================
# HISTORY TABLE
# ==========================================================

st.subheader("📋 Environmental History")

st.dataframe(

    history,

    use_container_width=True,

    hide_index=True

)

footer()