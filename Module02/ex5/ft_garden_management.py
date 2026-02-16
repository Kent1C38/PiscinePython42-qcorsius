def print_error(err: Exception):
    print(f"Error: {err}")


class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


class Plant:
    def __init__(self, name: str, water_level: int, sun_level: int):
        self.name = name
        self.water_level = water_level
        self.sun_level = sun_level


class Garden:
    def __init__(self, water_in_tank: int = 15):
        self.plants = []
        self.water_in_tank = water_in_tank

    def add_plant(self, name: str, water_level: int, sun_level: int):
        if name == "" or name is None:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(Plant(name, water_level, sun_level))
        print(f"Successfully added {name} to garden!")

    def water_plants(self):
        try:
            print("Opening watering system")
            for plant in self.plants:
                if self.water_in_tank <= 0:
                    raise WaterError("Not enough water in tank!")
                if isinstance(plant, Plant):
                    print(f"Watering {plant.name}")
                    plant.water_level += 1
                    self.water_in_tank -= 1
                else:
                    raise GardenError(f"Cannot water {plant} - not a plant !")
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant: Plant):
        if plant.water_level < 1:
            raise PlantError(
                    f"({plant.name}) Water level {plant.water_level} " +
                    "is too low (min 1)")
        if plant.water_level > 10:
            raise PlantError(
                    f"({plant.name}) Water level {plant.water_level} " +
                    "is too high (max 10)"
            )
        if plant.sun_level < 2:
            raise PlantError(
                    f"({plant.name}) Sunlight hours {plant.sun_level} " +
                    "is too low (min 2)")
        if plant.sun_level > 12:
            raise PlantError(
                f"({plant.name}) Sunlight hours {plant.sun_level} " +
                "is too high (max 12)"
            )
        print(f"Plant '{plant.name}' is healthy!")

    def set_water_level(self, level: int):
        if level < 0:
            raise WaterError("Water leve cannot be negative !")
        self.water_in_tank = level


def test_add_plant(garden: Garden):
    try:
        garden.add_plant("tomato", 5, 8)
    except PlantError as e:
        print_error(e)

    try:
        garden.add_plant("lettuce", 14, 6)
    except PlantError as e:
        print_error(e)

    try:
        garden.add_plant("cucumber", 5, 6)
    except PlantError as e:
        print_error(e)

    try:
        garden.add_plant("", 0, 0)
    except PlantError as e:
        print_error(e)


def test_error_recovery(garden: Garden):
    try:
        garden.set_water_level(0)
    except WaterError as e:
        print_error(e)

    try:
        garden.water_plants()
    except GardenError as e:
        print_error(e)
        print("System recoverd and continued...")


def test_garden_management():
    print("=== Garden Management System ===")
    print("\nInitializing garden...")
    garden = Garden()
    print("Done")

    print("\nAdding plants to garden...")
    test_add_plant(garden)

    print("\nWatering plants...")
    try:
        garden.water_plants()
    except GardenError as e:
        print_error(e)

    print("\nChecking plant health...")
    for plant in garden.plants:
        try:
            Garden.check_plant_health(plant)
        except PlantError as e:
            print_error(e)

    print("\nTesting error recovery...")
    test_error_recovery(garden)

    print("\nGarden management system test completed!")


if __name__ == "__main__":
    test_garden_management()
