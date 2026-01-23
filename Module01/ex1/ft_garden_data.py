class Plant:
    """
    Plant(name: str, height: int, lifetime: int)

    Creates a plant object

    Keyword arguments:
    name -- The name of your plant
    height -- The height of your plant (in cm)
    lifetime -- How long your plant has been alive since (in day)
    """

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def print_values(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Registry ===")
    rose.print_values()
    sunflower.print_values()
    cactus.print_values()
