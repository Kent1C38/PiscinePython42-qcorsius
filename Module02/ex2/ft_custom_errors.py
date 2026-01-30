class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    try:
        print("\nTesting PlantError...")
        raise PlantError("This plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("\nTesting WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("This plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
