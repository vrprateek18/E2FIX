def noise_index(aqi, wind):
    if aqi and aqi > 150:
        return "High"
    elif wind < 1:
        return "Moderate"
    else:
        return "Low"