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
        print(f"Created: {self.name} ({self.height}cm, {self.lifetime} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    print("\nTotal plants created: 5")
