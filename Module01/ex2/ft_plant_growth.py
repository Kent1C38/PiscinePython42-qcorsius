class Plant:
    def __init__(self, name: str, height: int, lifetime: int):
        self.name = name
        self.height = height
        self.lifetime = lifetime

    def age(self, duration: int):
        self.lifetime += duration

    def grow(self, size: int):
        self.height += size

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
