def water_index(temp, humidity):
    if temp > 35 and humidity < 40:
        return "High"
    elif humidity > 70:
        return "Low"
    else:
        return "Moderate"