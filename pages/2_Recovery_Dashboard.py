# ==========================================================
# E2FIX
# Recovery Dashboard
# ==========================================================

import streamlit as st

# -----------------------------
# UI
# -----------------------------
from utils.ui import (
    load_css,
    page_header,
    footer
)

#-------------------------------
#Database connected-------
#-------------------------------


from database.environment_history import (
    get_latest_record,
    update_recovery
)

# -----------------------------
# Components
# -----------------------------
from components.recovery import (
    show_recovery_dashboard
)

from components.analytics import (
    show_analytics
)

# -----------------------------
# Engine
# -----------------------------
from logic_layer.recovery_engine import (
    generate_recovery_data
)
# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Recovery Dashboard",
    page_icon="♻",
    layout="wide"
)

load_css()

page_header(

    "♻ Environmental Recovery Dashboard",

    "Carbon Credits • Recovery Bonus • Projected Environmental Score"

)

# ==========================================================
# USER INPUT
# ==========================================================

st.subheader("♻ Recovery Input")

col1, col2, col3 = st.columns(3)

with col1:

    current_score = st.number_input(

        "Current Environmental Score",

        min_value=0.0,

        max_value=100.0,

        value=65.0

    )

with col2:

    quantity = st.number_input(

        "Waste Quantity (kg)",

        min_value=0.0,

        value=10.0

    )

with col3:

    waste_type = st.selectbox(

        "Waste Type",

        [

            "Plastic",

            "Paper",

            "Metal",

            "Glass",

            "Organic",

            "E-Waste"

        ]

    )

st.markdown("")

recover = st.button(

    "🌱 Calculate Recovery",

    use_container_width=True,

    type="primary"

)

if recover:

    latest = get_latest_record()

    if latest is None:

        st.error("Please run Environmental Analysis first.")

        st.stop()

    current_score = latest["environmental_score"]

    recovery = generate_recovery_data(

        current_score,

        quantity,

        waste_type

    )
    update_recovery(

    record_id=latest["id"],

    carbon_saved=recovery["carbon_saved"],

    carbon_credits=recovery["credits"],

    recovery_bonus=recovery["bonus"],

    projected_score=recovery["projected_score"]

)
    show_recovery_dashboard(

        current_score=recovery["current_score"],

        carbon_saved=recovery["carbon_saved"],

        credits=recovery["credits"]

    )

    st.subheader("📋 Recovery Summary")

    st.success(

        f"""

Current Score : {recovery['current_score']}

Projected Score : {recovery['projected_score']}

Recovery Bonus : +{recovery['bonus']}

Recovery Progress : {recovery['progress']}%

Carbon Saved : {recovery['carbon_saved']} kg

Carbon Credits : {recovery['credits']}

Estimated Revenue : ₹{recovery['revenue']}

Timeline : {recovery['timeline']}

Status : {recovery['status']}

"""
    )

    st.info(

        f"🤖 {recovery['insight']}"

    )

    analytics_data = {

        "score": recovery["projected_score"],

        "aqi": 70,

        "temperature": 30,

        "humidity": 60,

        "wind": 10,

        "green": "Low",

        "noise": "Moderate",

        "water": "Low",

        "waste": "Moderate",

        "heat": "Low"

    }

    show_analytics(

        analytics_data

    )

footer()

