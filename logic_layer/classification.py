# ---------------------------------------------
# CLASSIFICATION LOGIC (IMPACT BASED)
# ---------------------------------------------
# Meaning of classes (SAME for all parameters):
# Low      = Low negative impact (GOOD)
# Moderate = Medium impact
# High     = High negative impact (BAD)
# ---------------------------------------------


def classify_aqi(aqi):
    """
    Safe AQI classification
    """
    if aqi is None:
        return "Moderate"   # neutral fallback

    if aqi <= 50:
        return "Low"
    elif aqi <= 100:
        return "Moderate"
    else:
        return "High"

def classify_temperature(temp):
    """
    IMD heat stress classification
    """
    if temp >= 40:
        return "High"
    elif temp >= 35:
        return "Moderate"
    else:
        return "Low"


def classify_green(temperature, land_type="urban"):
    """
    Green cover impact classification
    """

    # Dry / arid region override
    if temperature >= 38:
        return "High"   # very low greenery → high impact

    if land_type == "forest":
        return "Low"    # good greenery
    elif land_type == "urban":
        return "Moderate"
    else:
        return "High"


def classify_noise(area_type="residential"):
    """
    Noise exposure classification (CPCB zones)
    """
    if area_type == "industrial":
        return "High"
    elif area_type == "commercial":
        return "Moderate"
    else:
        return "Low"


def classify_water(region="plains"):
    """
    Water stress classification (CGWB / NITI logic)
    """
    if region == "arid":
        return "High"
    elif region == "plains":
        return "Moderate"
    else:
        return "Low"


def classify_waste(area_type="urban"):
    """
    Waste pressure classification
    """
    if area_type == "urban":
        return "High"
    elif area_type == "semi-urban":
        return "Moderate"
    else:
        return "Low"


# ---------------------------------------------
# SCORE MAPPING (FINAL)
# ---------------------------------------------

INDEX_SCORE = {
    "Low": 80,        # good condition
    "Moderate": 50,
    "High": 20        # bad condition
}
