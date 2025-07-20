# garden.py

# Dictionary storing gardening advice based on season and plant type
GARDENING_ADVICE = {
    "summer": {
        "flower": "Water your plants regularly and provide some shade."
                  "\nUse fertiliser to encourage blooms.",
        "vegetable": "Water your plants regularly and provide some shade."
                     "\nKeep an eye out for pests!"
    },
    "winter": {
        "flower": "Protect your plants from frost with covers."
                  "\nUse fertiliser to encourage blooms.",
        "vegetable": "Protect your plants from frost with covers."
                     "\nKeep an eye out for pests!"
    }
}

# Dictionary to recommend plants based on season
RECOMMENDED_PLANTS = {
    "summer": ["sunflowers", "tomatoes", "zinnias"],
    "winter": ["kale", "pansies", "broccoli"]
}


def get_user_input():
    """
    Prompts the user for season and plant type.
    Returns:
        tuple: season (str), plant_type (str)
    """
    season = input("Enter the season (e.g. summer, winter): ").strip().lower()
    plant_type = input(
        "Enter the plant type (e.g. flower, vegetable): "
    ).strip().lower()
    return season, plant_type


def provide_advice(season, plant_type):
    """
    Retrieves gardening advice based on season and plant type.
    Args:
        season (str): The current season
        plant_type (str): Type of plant
    Returns:
        str: Gardening advice
    """
    if season in GARDENING_ADVICE and plant_type in GARDENING_ADVICE[season]:
        return GARDENING_ADVICE[season][plant_type]
    else:
        return "No advice available for the given inputs."


def suggest_plants(season):
    """
    Suggests plants suitable for the given season.
    Args:
        season (str): The current season
    Returns:
        str: Suggested plants
    """
    if season in RECOMMENDED_PLANTS:
        plants = ', '.join(RECOMMENDED_PLANTS[season])
        return f"Recommended plants for {season}: {plants}."
    return "No plant recommendations for this season."


def main():
    """
    Main function to run the gardening advice application.
    """
    season, plant_type = get_user_input()
    print("\n--- Gardening Advice ---")
    print(provide_advice(season, plant_type))
    print("\n--- Suggested Plants ---")
    print(suggest_plants(season))


# Entry point
if __name__ == "__main__":
    main()
