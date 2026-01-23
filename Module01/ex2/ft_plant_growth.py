class Plant:
    """
    Plant(name: str, height: int, lifetime: int)

    Creates a plant object

    Keyword arguments:
    name -- The name of your plant
    height -- The height of your plant (in cm)
    lifetime -- How long your plant has been alive since (in day)
    """

    def __init__(self, name: str, height: int, lifetime: int):
        self.name = name
        self.height = height
        self.lifetime = lifetime

    """
    age(duration: int)

    Add days to the current age of your plant

    Keyword arguments:
    duration -- how many days to add
    """

    def age(self, duration: int):
        self.lifetime += duration

    """
    grow(size: int)

    Add cm to the current height of your plant

    Keyword arguments:
    size -- the size to add
    """

    def grow(self, size: int):
        self.height += size

    """
    get_infos()

    Print all informations of your plant
    """

    def get_infos(self):
        print(f"{self.name}: {self.height}cm, {self.lifetime} days old")


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_infos()

    growth: int = 6
    print("=== Day 7 ===")
    rose.grow(growth)
    rose.age(6)
    rose.get_infos()
    print(f"Growth this week: +{growth}cm")
