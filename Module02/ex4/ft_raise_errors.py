class Plant():

    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


def check_plant_health(plant: Plant):
    if plant.name == "" or plant.name is None:
        raise ValueError("Plant name cannot be empty!")
    if plant.water_level < 1:
        raise ValueError(f"Water level {plant.water_level} is too low (min 1)")
    if plant.water_level > 10:
        raise ValueError(
            f"Water level {plant.water_level} is too high (max 10)")
    if plant.sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {plant.sunlight_hours} is too low (min 2)")
    if plant.sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {plant.sunlight_hours} is too high (max 12)")
    print(f"Plant '{plant.name}' is healthy!")


def test_plant_checks():
    print("=== Garden Plant Check Demo ===")

    print("\nTesting with good values...")
    try:
        check_plant_health(Plant("tomato", 5, 6))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting with empty plant name...")
    try:
        check_plant_health(Plant("", 5, 6))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health(Plant("tomato", 50, 6))
    except ValueError as e:
        print(f"Error: {e}")
    try:
        check_plant_health(Plant("tomato", 0, 6))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting with bad sunlight hours...")
    try:
        check_plant_health(Plant("tomato", 5, -9))
    except ValueError as e:
        print(f"Error: {e}")
    try:
        check_plant_health(Plant("tomato", 5, 20))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
