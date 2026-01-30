def check_instance(obj: object, cls: type) -> bool:
    return cls in obj.__class__.__mro__


class Plant:
    _types = {}

    def __init_subclass__(cls, *, type_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if type_name:
            Plant._types[type_name] = cls

    def __init__(self, name: str, height: int):
        if Plant.is_height_valid(height):
            self.name = name
            self.height = height
        else:
            raise ValueError("Height must be a positive integer !")

    def grow(self, size: int):
        if Plant.is_height_valid(size):
            self.height += size
            print(f"{self.name} grew {size}cm")
        else:
            raise ValueError("Size must be a positive integer !")

    def get_infos(self) -> str:
        return f"{self.name}: {self.height}cm"

    @classmethod
    def create(cls, type_name, *args, **kwargs):
        try:
            return cls._types[type_name](*args, **kwargs)
        except KeyError:
            raise ValueError("Unknown plant type")

    @staticmethod
    def is_height_valid(height: int):
        return height > 0


class BasePlant(Plant, type_name="plant"):
    pass


class FloweringPlant(Plant, type_name="flower"):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.blooming = False

    def bloom(self):
        self.blooming = True

    def get_infos(self) -> str:
        msg = f"{super().get_infos()}, {self.color} flowers"
        if self.blooming:
            msg = f"{msg} (blooming)"
        return msg


class PrizeFlower(FloweringPlant, type_name="prized"):
    def __init__(self, name: str, height: int, color: str, prize_points: int):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_infos(self) -> str:
        return f"{super().get_infos()}, {self.prize_points} prize points"


class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.content: dict[str, Plant] = {}

    def add_plant(self, plant: Plant):
        self.content[plant.name] = plant

    def get_plant(self, name: str):
        return self.content[name]

    def grow_plant(self, name: str, size: int):
        self.get_plant(name).grow(size)

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.content.values():
            print(f"- {plant.get_infos()}")


class GardenStats:
    def __init__(self):
        self.regular = 0
        self.flowering = 0
        self.prize = 0
        self.total_added = 0
        self.total_growth = 0
        self.garden_count = 0

    @staticmethod
    def get_total_points(garden: Garden) -> int:
        total = 0
        for plant in garden.content.values():
            if check_instance(plant, PrizeFlower):
                total += plant.prize_points
        return total


class GardenManager:
    def __init__(self):
        self.stats = GardenStats()

    def add_garden(self, owner: str):
        self.gardens[owner] = Garden(owner)
        self.stats.garden_count += 1
        print(f"{owner} registered their garden")

    def get_garden(self, owner: str) -> Garden:
        return self.gardens.get(owner)

    def grow_plant(self, owner: str, name: str, size: int):
        self.get_garden(owner).get_plant(name).grow()
        self.stats.total_growth += size

    def grow_all_plants(self, owner: str, size: int):
        print(f"{owner} is helping all the plants from their garden to grow...")
        for plant in self.get_garden(owner).content.values():
            plant.grow(size)
            self.stats.total_growth += size

    def add_plant_to_garden(self, owner: str, plant: Plant):
        if self.get_garden(owner) is None:
            return
        self.gardens[owner].add_plant(plant)
        self.stats.total_added += 1
        if check_instance(plant, PrizeFlower):
            self.stats.prize += 1
        elif check_instance(plant, FloweringPlant):
            self.stats.flowering += 1
        else:
            self.stats.regular += 1
        print(f"Added {plant.name} to {owner}'s Garden")

    def show_stats(self):
        scores = ""
        for garden in self.gardens.values():
            if scores != "":
                scores = (
                    f"{scores}, {garden.owner}: {GardenStats.get_total_points(garden)}"
                )
            else:
                scores = f"{garden.owner}: {GardenStats.get_total_points(garden)}"
        print(
            f"Plants added: {self.stats.total_added}, Total growth: {self.stats.total_growth}cm"
        )
        print(
            f"Plant types: {self.stats.regular} regular, {self.stats.flowering} flowering, {self.stats.prize} prize flower\n"
        )
        print("Height validation: True (Would just break if not valid)")
        print(f"Garden scores - {scores}")
        print(f"Total managed gardens: {self.stats.garden_count}")


def create_garden_network() -> GardenManager:
    manager = GardenManager()
    manager.gardens: dict[str, Garden] = {}
    return manager


if __name__ == "__main__":
    print("=== Garden Manager System Demo ===\n")
    manager = create_garden_network()

    manager.add_garden("Alice")
    manager.add_garden("Bob")

    print()
    manager.add_plant_to_garden("Alice", Plant.create("plant", "Oak tree", 101))
    manager.add_plant_to_garden("Alice", Plant.create("flower", "Rose", 26, "red"))
    manager.add_plant_to_garden("Bob", Plant.create("flower", "Tulip", 10, "rose"))

    sunflo = Plant.create("prized", "Sunflower", 51, "yellow", 10)
    sunflo.bloom()

    manager.add_plant_to_garden("Alice", sunflo)

    print()
    manager.grow_all_plants("Alice", 3)
    manager.get_garden("Bob").get_plant("Tulip").grow(5)

    print()
    manager.get_garden("Alice").report()
    manager.get_garden("Bob").report()

    print()
    manager.show_stats()
