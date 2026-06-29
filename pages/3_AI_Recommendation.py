# ==========================================================
# E2FIX
# AI Recommendation
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

# -----------------------------
# Database
# -----------------------------
from database.environment_history import (
    get_latest_record
)

# -----------------------------
# AI Engine
# -----------------------------
from logic_layer.recommendation_engine import (
    generate_ai_recommendations
)


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="AI Recommendation",

    page_icon="🤖",

    layout="wide"

)

load_css()

page_header(

    "🤖 AI Environmental Recommendation",

    "AI Powered Environmental Decision Support System"

)


# ==========================================================
# LOAD LATEST ANALYSIS
# ==========================================================

latest = get_latest_record()

if latest is None:

    st.warning(

        "Please complete an Environmental Analysis first."

    )

    st.stop()


analysis = {

    "score": latest["environmental_score"],

    "aqi": latest["aqi"],

    "green": "Moderate",

    "noise": "Moderate",

    "water": "Moderate",

    "waste": "Moderate",

    "heat": "Moderate"

}


recommendations = generate_ai_recommendations(

    analysis

)


# ==========================================================
# AI PRIORITY
# ==========================================================

st.subheader("🚨 AI Environmental Assessment")

priority = recommendations["priority"]

if priority == "Critical":

    st.error(f"🔴 Priority Level : {priority}")

elif priority == "High":

    st.warning(f"🟠 Priority Level : {priority}")

elif priority == "Medium":

    st.info(f"🟡 Priority Level : {priority}")

else:

    st.success(f"🟢 Priority Level : {priority}")


# ==========================================================
# AI RECOMMENDATIONS
# ==========================================================

st.subheader("🤖 Smart Environmental Recommendations")

col1, col2 = st.columns(2)

with col1:

    st.info(
        f"""
### 🌫 Air Quality

**Status**

{recommendations["aqi_status"]}

**Recommendation**

{recommendations["aqi_action"]}
"""
    )

    st.success(
        f"""
### 🌳 Green Area

{recommendations["green"]}
"""
    )

    st.warning(
        f"""
### ♻ Waste Management

{recommendations["waste"]}
"""
    )

with col2:

    st.info(
        f"""
### 💧 Water Resources

{recommendations["water"]}
"""
    )

    st.warning(
        f"""
### 🔊 Noise Pollution

{recommendations["noise"]}
"""
    )

    st.error(
        f"""
### 🌡 Heat Management

{recommendations["heat"]}
"""
    )


# ==========================================================
# AI FUTURE PREDICTION
# ==========================================================

st.subheader("🔮 AI Future Prediction")

st.info(

    recommendations["prediction"]

)


# ==========================================================
# ACTION PLAN
# ==========================================================

st.subheader("📋 Recommended Action Plan")

actions = [

    "🌳 Increase tree plantation in low green-cover areas.",

    "♻ Improve waste segregation and recycling.",

    "💧 Promote rainwater harvesting and water conservation.",

    "🚲 Encourage public transport and cycling.",

    "🏭 Monitor industrial emissions regularly.",

    "📊 Perform environmental analysis every week."

]

for action in actions:

    st.markdown(f"- {action}")


footer()