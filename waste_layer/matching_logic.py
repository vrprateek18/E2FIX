def match_agency(waste_type):
    agencies = {
        "plastic": "GreenRecycle Pvt Ltd",
        "organic": "BioCompost India",
        "industrial": "CarbonFix Solutions"
    }

    return agencies.get(waste_type.lower(), "No Agency Found")