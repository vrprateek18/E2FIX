def waste_index(aqi, temp):
    if aqi and aqi > 120:
        return "High"
    elif temp > 35:
        return "Moderate"
    else:
        return "Low"