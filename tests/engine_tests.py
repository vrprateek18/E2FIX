import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logic_layer.classification import (
    classify_aqi,
    classify_temperature,
    classify_green,
    classify_noise,
    classify_water,
    classify_waste
)
from logic_layer.scoring_engine import calculate_environment_score

# ---- SAMPLE TEST CASES ----

test_cases = [
    {"name": "Forest Area", "aqi": 35, "temp": 28},
    {"name": "Urban City", "aqi": 85, "temp": 33},
    {"name": "Industrial Zone", "aqi": 180, "temp": 39}
]

for case in test_cases:
    classes = {
        "aqi": classify_aqi(case["aqi"]),
        "green": classify_green(case["temp"], "forest" if case["name"]=="Forest Area" else "urban"),
        "noise": classify_noise("industrial" if case["name"]=="Industrial Zone" else "residential"),
        "heat": classify_temperature(case["temp"]),
        "water": classify_water("arid" if case["temp"]>38 else "plains"),
        "waste": classify_waste("urban")
    }

    score = calculate_environment_score(classes)

    print("\nLocation:", case["name"])
    print("Classes:", classes)
    print("Score:", score)
