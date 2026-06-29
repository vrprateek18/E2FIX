# ==========================================================
# E2FIX
# Cards Component
# ==========================================================

import streamlit as st


# ==========================================================
# KPI CARD
# ==========================================================

def kpi_card(title, value, icon=""):

    st.metric(

        label=f"{icon} {title}",

        value=value

    )


# ==========================================================
# STATUS CARD
# ==========================================================

def status_card(title, value):

    if value == "Low":

        st.success(f"**{title}**\n\n{value}")

    elif value == "Moderate":

        st.warning(f"**{title}**\n\n{value}")

    elif value == "High":

        st.error(f"**{title}**\n\n{value}")

    elif value == "Critical":

        st.error(f"**{title}**\n\n{value}")

    else:

        st.info(f"**{title}**\n\n{value}")


# ==========================================================
# SCORE CARD
# ==========================================================

def score_card(score):

    if score >= 80:

        delta = "Excellent"

    elif score >= 60:

        delta = "Moderate"

    else:

        delta = "Poor"

    st.metric(

        label="🌍 Environmental Score",

        value=f"{score}/100",

        delta=delta

    )


# ==========================================================
# CARBON CARD
# ==========================================================

def carbon_card(saved, credits):

    col1, col2 = st.columns(2)

    with col1:

        st.metric(

            "🌱 Carbon Saved",

            f"{saved:.2f} kg"

        )

    with col2:

        st.metric(

            "💳 Carbon Credits",

            f"{credits:.3f}"

        )


# ==========================================================
# PROJECTED SCORE
# ==========================================================

def projected_score_card(current, bonus):

    projected = min(current + bonus, 100)

    st.metric(

        label="📈 Projected Score",

        value=f"{projected:.1f}",

        delta=f"+{bonus}"

    )


# ==========================================================
# AI CARD
# ==========================================================

def ai_card(title, message):

    st.info(

        f"### 🤖 {title}\n\n{message}"

    )