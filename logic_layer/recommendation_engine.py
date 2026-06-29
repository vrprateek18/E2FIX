# ==========================================================
# AI RECOMMENDATION ENGINE
# ==========================================================

from datetime import datetime


# ==========================================================
# AQI RECOMMENDATION
# ==========================================================

def aqi_recommendation(aqi):

    # API se AQI na mile to default value use karo
    if aqi is None:

        return (
            "AQI data unavailable.",
            "Unable to retrieve live AQI. Please check your internet connection or try again later."
        )

    if aqi <= 50:

        return (
            "Excellent air quality.",
            "Maintain green spaces and monitor pollution regularly."
        )

    elif aqi <= 100:

        return (
            "Moderate air quality.",
            "Increase tree plantation and reduce vehicle emissions."
        )

    elif aqi <= 200:

        return (
            "Poor air quality.",
            "Promote public transport and reduce industrial emissions."
        )

    else:

        return (
            "Very poor air quality.",
            "Immediate pollution control measures are recommended."
        )

# ==========================================================
# GREEN AREA
# ==========================================================

def green_recommendation(level):

    if level == "Low":

        return (
            "Increase tree plantation in the selected area."
        )

    elif level == "Moderate":

        return (
            "Maintain parks and plant additional native trees."
        )

    else:

        return (
            "Green coverage is good. Continue maintenance."
        )

# ==========================================================
# WASTE MANAGEMENT
# ==========================================================

def waste_recommendation(level):

    if level == "High":

        return (
            "Improve waste segregation and recycling immediately."
        )

    elif level == "Moderate":

        return (
            "Increase recycling awareness and waste collection."
        )

    else:

        return (
            "Waste management is under control."
        )


# ==========================================================
# WATER MANAGEMENT
# ==========================================================

def water_recommendation(level):

    if level == "High":

        return (
            "Critical water stress detected. Promote rainwater harvesting and reduce water wastage."
        )

    elif level == "Moderate":

        return (
            "Improve water conservation practices and monitor consumption."
        )

    else:

        return (
            "Water resources are stable. Continue sustainable usage."
        )


# ==========================================================
# NOISE POLLUTION
# ==========================================================

def noise_recommendation(level):

    if level == "High":

        return (
            "High noise pollution detected. Reduce traffic noise and control industrial sound."
        )

    elif level == "Moderate":

        return (
            "Monitor noise levels and increase green barriers."
        )

    else:

        return (
            "Noise pollution is under control."
        )


# ==========================================================
# HEAT MANAGEMENT
# ==========================================================

def heat_recommendation(level):

    if level == "High":

        return (
            "Urban heat island effect detected. Increase green roofs and tree plantation."
        )

    elif level == "Moderate":

        return (
            "Increase shaded areas and monitor temperature."
        )

    else:

        return (
            "Heat conditions are normal."
        )


# ==========================================================
# PRIORITY LEVEL
# ==========================================================

def priority(score):

    if score >= 85:

        return "Low"

    elif score >= 70:

        return "Medium"

    elif score >= 50:

        return "High"

    else:

        return "Critical"

# ==========================================================
# FUTURE PREDICTION
# ==========================================================

def future_prediction(score):

    if score >= 85:

        return (
            "Environmental conditions are expected to remain stable over the coming weeks."
        )

    elif score >= 70:

        return (
            "With continued recovery efforts, the environmental score is likely to improve."
        )

    elif score >= 50:

        return (
            "Recovery activities can significantly improve the environmental score in the next few weeks."
        )

    else:

        return (
            "Immediate environmental actions are required to prevent further deterioration."
        )


# ==========================================================
# GENERATE AI RECOMMENDATIONS
# ==========================================================

def generate_ai_recommendations(data):

    aqi_status, aqi_action = aqi_recommendation(data["aqi"])

    recommendations = {

        "aqi_status": aqi_status,

        "aqi_action": aqi_action,

        "green": green_recommendation(data["green"]),

        "waste": waste_recommendation(data["waste"]),

        "water": water_recommendation(data["water"]),

        "noise": noise_recommendation(data["noise"]),

        "heat": heat_recommendation(data["heat"]),

        "priority": priority(data["score"]),

        "prediction": future_prediction(data["score"]),

        "generated_at": datetime.now()

    }

    return recommendations