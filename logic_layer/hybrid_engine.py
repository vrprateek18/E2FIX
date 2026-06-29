def green_index(temp, humidity, aqi):
    if temp > 38 and humidity < 40:
        return "High"
    elif aqi and aqi > 120:
        return "High"
    elif 20 <= temp <= 32 and 40 <= humidity <= 70:
        return "Low"
    else:
        return "Moderate"


def noise_index(aqi, wind):
    if aqi and aqi > 150:
        return "High"
    elif wind < 1:
        return "Moderate"
    else:
        return "Low"


def water_index(temp, humidity):
    if temp > 35 and humidity < 40:
        return "High"
    elif humidity > 70:
        return "Low"
    else:
        return "Moderate"


def waste_index(aqi, temp):
    if aqi and aqi > 120:
        return "High"
    elif temp > 35:
        return "Moderate"
    else:
        return "Low"