IMPACT_SCORE = {
    "Low": 85,
    "Moderate": 60,
    "High": 30
}


def score_aqi(aqi):
    if aqi is None:
        return 60

    if aqi <= 50:
        return 90
    elif aqi <= 100:
        return 70
    elif aqi <= 200:
        return 40
    else:
        return 10


def calculate_environment_score(data, proxies, carbon_saved=0):

    aqi_score = score_aqi(data["aqi"])

    green_score = IMPACT_SCORE[proxies["green"]]
    noise_score = IMPACT_SCORE[proxies["noise"]]
    water_score = IMPACT_SCORE[proxies["water"]]
    waste_score = IMPACT_SCORE[proxies["waste"]]

    base_score = (
        aqi_score * 0.40 +
        green_score * 0.15 +
        noise_score * 0.10 +
        water_score * 0.15 +
        waste_score * 0.20
    )

    # Carbon Recovery Bonus
    bonus = min(carbon_saved / 50, 5)

    final_score = min(base_score + bonus, 100)

    return round(final_score, 1)