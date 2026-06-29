# ==========================================================
# REPORT ENGINE
# ==========================================================

from datetime import datetime

from database.environment_history import (
    get_latest_record,
    get_environment_history
)

from logic_layer.recommendation_engine import (
    generate_ai_recommendations
)


# ==========================================================
# ENVIRONMENT GRADE
# ==========================================================

def environmental_grade(score):

    if score >= 85:

        return "Excellent", "🟢"

    elif score >= 70:

        return "Good", "🟡"

    elif score >= 50:

        return "Moderate", "🟠"

    else:

        return "Poor", "🔴"


# ==========================================================
# ANALYTICS SUMMARY
# ==========================================================

def analytics_summary(history):

    if len(history) == 0:

        return {

            "total_analysis":0,

            "best_score":0,

            "average_aqi":0,

            "total_carbon":0,

            "total_credits":0

        }

    scores = []

    aqi = []

    carbon = []

    credits = []

    for row in history:

        scores.append(row["environmental_score"])

        aqi.append(row["aqi"])

        carbon.append(row["carbon_saved"])

        credits.append(row["carbon_credits"])

    return {

        "total_analysis":len(history),

        "best_score":max(scores),

        "average_aqi":round(sum(aqi)/len(aqi),1),

        "total_carbon":round(sum(carbon),2),

        "total_credits":round(sum(credits),3)

    }


# ==========================================================
# REPORT DATA
# ==========================================================

def generate_report_data():

    latest = get_latest_record()

    history = get_environment_history()

    if latest is None:

        return None


# ==========================================================
# REPORT ID
# ==========================================================

report_id = datetime.now().strftime(

    "E2FIX-%Y%m%d-%H%M%S"

)



analysis = {

    "score": latest["environmental_score"],

    "aqi": latest["aqi"],

    "green": "Moderate",

    "noise": "Moderate",

    "water": "Moderate",

    "waste": "Moderate",

    "heat": "Moderate"

}

recommendation = generate_ai_recommendations(

    analysis

)

summary = analytics_summary(

    history

)

grade, badge = environmental_grade(

    latest["environmental_score"]

)


report = {

    "report_id": report_id,

    "generated_at": datetime.now(),

    "location": latest["location"],

    "latitude": latest["latitude"],

    "longitude": latest["longitude"],

    "aqi": latest["aqi"],

    "environmental_score": latest["environmental_score"],

    "projected_score": latest["projected_score"],

    "carbon_saved": latest["carbon_saved"],

    "carbon_credits": latest["carbon_credits"],

    "grade": grade,

    "badge": badge,

    "analytics": summary,

    "recommendation": recommendation

}

return report

