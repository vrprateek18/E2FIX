# ==========================================================
# E2FIX
# SMART MAP
# ==========================================================

import streamlit as st
import folium
from streamlit_folium import st_folium

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
    get_latest_record
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Smart Map",

    page_icon="🗺",

    layout="wide"

)

load_css()

page_header(

    "🗺 Smart Environmental Map",

    "Live Environmental Monitoring"

)


# ==========================================================
# LOAD DATA
# ==========================================================

latest = get_latest_record()

if latest is None:

    st.warning(

        "No Environmental Analysis Found."

    )

    st.stop()


# ==========================================================
# MARKER COLOR
# ==========================================================

score = latest["environmental_score"]

if score >= 85:

    color = "green"

elif score >= 70:

    color = "blue"

elif score >= 50:

    color = "orange"

else:

    color = "red"


# ==========================================================
# CREATE MAP
# ==========================================================

m = folium.Map(

    location=[

        latest["latitude"],

        latest["longitude"]

    ],

    zoom_start=13,

    control_scale=True

)


# ==========================================================
# POPUP
# ==========================================================

popup = f"""
<b>🌍 Location:</b> {latest["location"]}<br><br>

<b>📈 Environmental Score:</b> {latest["environmental_score"]}<br>

<b>🌫 AQI:</b> {latest["aqi"]}<br>

<b>♻ Carbon Saved:</b> {latest["carbon_saved"]} kg<br>

<b>💳 Carbon Credits:</b> {latest["carbon_credits"]}<br>

<b>🚀 Projected Score:</b> {latest["projected_score"]}<br>

<b>📅 Last Updated:</b> {latest["created_at"]}
"""


# ==========================================================
# SMART MARKER
# ==========================================================

folium.Marker(

    location=[

        latest["latitude"],

        latest["longitude"]

    ],

    popup=folium.Popup(

        popup,

        max_width=320

    ),

    tooltip=latest["location"],

    icon=folium.Icon(

        color=color,

        icon="leaf",

        prefix="fa"

    )

).add_to(m)


# ==========================================================
# ENVIRONMENT ZONE
# ==========================================================

folium.Circle(

    location=[

        latest["latitude"],

        latest["longitude"]

    ],

    radius=500,

    color=color,

    fill=True,

    fill_opacity=0.25

).add_to(m)


# ==========================================================
# SHOW MAP
# ==========================================================

st.subheader("🌍 Live Environmental Map")

st_folium(

    m,

    width=None,

    height=600
)


# ==========================================================
# MAP SUMMARY
# ==========================================================

st.subheader("📊 Location Summary")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(

        "📈 Environmental Score",

        latest["environmental_score"]

    )

    st.metric(

        "🌫 AQI",

        latest["aqi"]

    )

with col2:

    st.metric(

        "♻ Carbon Saved",

        f'{latest["carbon_saved"]} kg'

    )

    st.metric(

        "💳 Carbon Credits",

        latest["carbon_credits"]

    )

with col3:

    st.metric(

        "🚀 Projected Score",

        latest["projected_score"]

    )

    st.metric(

        "📍 Location",

        latest["location"]

    )


footer()