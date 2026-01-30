def check_instance(obj: object, cls: type) -> bool:
    return cls in obj.__class__.__mro__


class Plant:
    def __init__(self, name: str):
        self.name = name


def water_plants(plant_list: list[Plant]):
    try:
        print("Openning watering system")
        for plant in plant_list:
            if check_instance(plant, Plant):
                print(f"Watering {plant.name}")
            else:
                raise Exception(f"Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    valid_list = {Plant("tomato"), Plant("lettuce"), Plant("carrot")}
    invalid_list = {Plant("tomato"), None, Plant("carrot")}

    print("=== Garden Watering System ===")

    try:
        print("\nTesting normal watering...")
        water_plants(valid_list)
    except Exception as e:
        print(f"Error: {e}")

    try:
        print("\nTesting with errors...")
        water_plants(invalid_list)
    except Exception as e:
        print(f"Error: {e}")

    print("\nCleanup always happen, even  with errors!")


if __name__ == "__main__":
    test_watering_system()
