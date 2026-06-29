CARBON_FACTORS = {
    "Plastic": 2.5,
    "Metal": 3.0,
    "Paper": 1.5,
    "Organic": 0.5,
    "Other": 1.0
}

def calculate_carbon(waste_type, quantity):

    factor = CARBON_FACTORS[waste_type]

    carbon_saved = quantity * factor

    credits = carbon_saved / 1000

    revenue = credits * 1500

    return carbon_saved, credits, revenue