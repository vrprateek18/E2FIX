import streamlit as st

from components.cards import ai_card


# ==========================================================
# IMMEDIATE ACTIONS
# ==========================================================

def immediate_actions(score):

    if score >= 80:

        return [
            "Maintain current environmental practices.",
            "Monitor AQI weekly.",
            "Promote community awareness."
        ]

    elif score >= 60:

        return [
            "Increase waste segregation.",
            "Reduce traffic emissions.",
            "Plant more trees."
        ]

    else:

        return [
            "Immediate waste cleanup required.",
            "Control industrial pollution.",
            "Launch emergency plantation drive."
        ]


# ==========================================================
# MEDIUM TERM
# ==========================================================

def medium_actions(score):

    if score >= 80:

        return [
            "Install additional air-quality sensors.",
            "Expand green belts."
        ]

    elif score >= 60:

        return [
            "Improve waste recycling system.",
            "Rainwater harvesting."
        ]

    else:

        return [
            "Develop smart waste collection.",
            "Increase green infrastructure."
        ]

# ==========================================================
# LONG TERM
# ==========================================================

def long_actions(score):

    if score >= 80:

        return [
            "Maintain sustainable city planning.",
            "Expand renewable energy."
        ]

    elif score >= 60:

        return [
            "Smart environmental monitoring.",
            "Carbon neutrality programs."
        ]

    else:

        return [
            "City-wide environmental restoration.",
            "Carbon offset projects.",
            "Green transportation initiatives."
        ]


# ==========================================================
# AI INSIGHT
# ==========================================================

def ai_insight(data):

    aqi = data.get("aqi")
    temp = data.get("temperature")

    # Default values if API fails
    if aqi is None:
        aqi = 50

    if temp is None:
        temp = 25

    if aqi > 200:

        return (
            "Air pollution is the biggest contributor to the "
            "low environmental score."
        )

    elif temp > 40:

        return (
            "High temperature indicates heat stress. "
            "Urban greening is recommended."
        )

    else:

        return (
            "Environmental indicators are relatively balanced. "
            "Maintain current sustainability efforts."
        )

# ==========================================================
# RECOVERY PREDICTION
# ==========================================================

def recovery_prediction(score):

    if score >= 80:

        return "Expected Improvement: +2 to +5 points"

    elif score >= 60:

        return "Expected Improvement: +8 to +12 points"

    return "Expected Improvement: +15 to +25 points"


# ==========================================================
# SHOW RECOMMENDATIONS
# ==========================================================

def show_recommendations(data):

    score = data["score"]

    st.subheader("🤖 AI Environmental Recommendation")

    c1, c2, c3 = st.columns(3)

    with c1:

        ai_card(

            "Immediate Actions",

            "• " + "\n\n• ".join(immediate_actions(score))

        )

    with c2:

        ai_card(

            "Medium Term",

            "• " + "\n\n• ".join(medium_actions(score))

        )

    with c3:

        ai_card(

            "Long Term",

            "• " + "\n\n• ".join(long_actions(score))

        )

    st.markdown("---")

    ai_card(

        "AI Environmental Insight",

        ai_insight(data)

    )

    ai_card(

        "Recovery Prediction",

        recovery_prediction(score)

    )
