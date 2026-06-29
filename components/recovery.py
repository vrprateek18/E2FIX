import streamlit as st

from components.cards import (
    carbon_card,
    projected_score_card,
    ai_card
)

# ==========================================================
# RECOVERY BONUS
# ==========================================================

def calculate_recovery_bonus(carbon_saved):

    """
    Every 50 kg carbon saved
    gives +1 score

    Maximum Bonus = 20
    """

    bonus = carbon_saved / 50

    return min(round(bonus,1),20)

# ==========================================================
# PROJECTED SCORE
# ==========================================================

def projected_score(current_score, bonus):

    return min(

        round(current_score + bonus,1),

        100

    )

# ==========================================================
# RECOVERY %
# ==========================================================

def recovery_percentage(current, projected):

    improvement = projected-current

    return round(

        (improvement/100)*100,

        1

    )

# ==========================================================
# RECOVERY TIMELINE
# ==========================================================

def recovery_timeline(carbon_saved):

    if carbon_saved < 50:

        return "1-2 Months"

    elif carbon_saved < 150:

        return "2-4 Weeks"

    elif carbon_saved < 300:

        return "1-2 Weeks"

    else:

        return "Less than 1 Week"


# ==========================================================
# AI RECOVERY
# ==========================================================

def recovery_insight(projected):

    if projected >= 90:

        return (

            "Excellent recovery potential. "

            "Maintain recycling and green initiatives."

        )

    elif projected >= 75:

        return (

            "Recovery is progressing well. "

            "Continue carbon reduction."

        )

    elif projected >= 60:

        return (

            "Moderate recovery. "

            "Increase plantation and recycling."

        )

    else:

        return (

            "Recovery is slow. "

            "Immediate environmental action is required."

        )

# ==========================================================
# SHOW RECOVERY
# ==========================================================

def show_recovery_dashboard(

    current_score,

    carbon_saved,

    credits

):

    bonus = calculate_recovery_bonus(

        carbon_saved

    )

    projected = projected_score(

        current_score,

        bonus

    )

    timeline = recovery_timeline(

        carbon_saved

    )

    recovery = recovery_percentage(

        current_score,

        projected

    )

    st.subheader(

        "🌱 Environmental Recovery Dashboard"

    )

    c1,c2 = st.columns(2)

    with c1:

        carbon_card(

            carbon_saved,

            credits

        )

    with c2:

        projected_score_card(

            current_score,

            bonus

        )

    st.markdown("---")

    st.metric(

        "Recovery Timeline",

        timeline

    )

    st.metric(

        "Recovery Progress",

        f"{recovery}%"

    )

    ai_card(

        "Recovery Insight",

        recovery_insight(projected)

    )

show_recovery_dashboard(

    current_score=72,

    carbon_saved=125,

    credits=0.125

)
