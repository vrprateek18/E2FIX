def green_index(temp, humidity, aqi):
    if temp > 38 and humidity < 40:
        return "High"   # high negative impact (low greenery)
    elif aqi and aqi > 120:
        return "High"
    elif 20 <= temp <= 32 and 40 <= humidity <= 70:
        return "Low"
    else:
        return "Moderate"