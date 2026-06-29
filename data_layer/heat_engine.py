def heat_stress_index(temperature):
    if temperature >= 40:
        return "High"
    elif temperature >= 35:
        return "Moderate"
    else:
        return "Low"
