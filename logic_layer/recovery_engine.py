# ==========================================================
# RECOVERY ENGINE
# ==========================================================

from datetime import datetime


# ==========================================================
# CARBON CALCULATOR
# ==========================================================

def calculate_carbon(quantity, waste_type):
    """
    Returns:
        carbon_saved (kg)
        carbon_credits
        estimated_revenue
    """

    factors = {

        "Plastic": 6.0,

        "Paper": 3.5,

        "Metal": 8.0,

        "Glass": 2.0,

        "Organic": 1.5,

        "E-Waste": 10.0

    }

    factor = factors.get(waste_type, 2.0)

    carbon_saved = quantity * factor

    credits = carbon_saved / 1000

    revenue = credits * 25

    return (

        round(carbon_saved,2),

        round(credits,3),

        round(revenue,2)

    )


# ==========================================================
# BONUS CALCULATOR
# ==========================================================

def calculate_recovery_bonus(carbon_saved):

    """
    50 kg carbon saved

    =

    +1 Environmental Score
    """

    bonus = carbon_saved / 50

    return min(

        round(bonus,1),

        20

    )

# ==========================================================
# PROJECTED SCORE
# ==========================================================

def calculate_projected_score(

    current_score,

    bonus

):

    return min(

        round(current_score + bonus,1),

        100

    )

# ==========================================================
# RECOVERY %
# ==========================================================

def calculate_progress(

    current,

    projected

):

    improvement = projected-current

    return round(

        (improvement/100)*100,

        1

    )

# ==========================================================
# TIMELINE
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
# RECOVERY STATUS
# ==========================================================

def recovery_status(projected):

    if projected >= 90:

        return "Excellent"

    elif projected >= 75:

        return "Good"

    elif projected >= 60:

        return "Moderate"

    else:

        return "Poor"

# ==========================================================
# AI INSIGHT
# ==========================================================

def recovery_insight(projected):

    if projected >= 90:

        return (

            "Environmental recovery is progressing exceptionally well."

        )

    elif projected >= 75:

        return (

            "Recovery is stable. Continue recycling and plantation."

        )

    elif projected >= 60:

        return (

            "Moderate improvement detected. Increase recovery activities."

        )

    else:

        return (

            "Recovery progress is slow. Immediate action is recommended."

        )

# ==========================================================
# GENERATE RECOVERY DATA
# ==========================================================

def generate_recovery_data(

    current_score,

    quantity,

    waste_type

):

    carbon_saved, credits, revenue = calculate_carbon(

        quantity,

        waste_type

    )

    bonus = calculate_recovery_bonus(

        carbon_saved

    )

    projected = calculate_projected_score(

        current_score,

        bonus

    )

    progress = calculate_progress(

        current_score,

        projected

    )

    return {

        "current_score": current_score,

        "carbon_saved": carbon_saved,

        "credits": credits,

        "revenue": revenue,

        "bonus": bonus,

        "projected_score": projected,

        "progress": progress,

        "timeline": recovery_timeline(carbon_saved),

        "status": recovery_status(projected),

        "insight": recovery_insight(projected),

        "generated_at": datetime.now()

    }

