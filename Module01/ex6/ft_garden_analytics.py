class Plant:
    __types = {}

    """
    Initializes plants subclasses by registering them with a type name

    Keyword arguments:
    cls - The class/subclass that inherits from plants you want
        to make inherit your new subclass
    Optionnal arguments:
    type_name - The 'registered' name used in the creation of
        a plant to specify the class inheritance
    **kwargs - Options from other classes
    """

    def __init_subclass__(cls, *, type_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if type_name:
            Plant.__types[type_name] = cls

    """
    Creates a Plant object

    Keyword arguments:
    name - The plant's name (positive int)
    height - The plants's height (positive int)
    """

    def __init__(self, name: str, height: int):
        if Plant.is_height_valid(height):
            self.name = name
            self.height = height
        else:
            print(f"Could not create '{name}': " +
                  "Height must be a positive integer !")

    """
    Increases the height of your plant

    Keyword arguments:
    size - The size (in cm) your plant must grow (positive int)
    """

    def grow(self, size: int) -> bool:
        if Plant.is_height_valid(size):
            self.height += size
            print(f"{self.name} grew {size}cm")
            return True
        else:
            print(f"Cannot grow {self.name}: Size must be a positive integer!")
            return False

    """
    Retrieves useful infos about your plant

    Return value: str
    """

    def get_infos(self) -> str:
        return f"{self.name}: {self.height}cm"

    """
    Creates a new plant using the right subclass following the given type name

    Keyword arguments:
    cls: The current class
    type_name: The string representing the class you want it to inherit
    *args: The arguments that should be given to create your plant
    **kwargs: Arguments that are consumed by the constructor
    """

    @classmethod
    def create(cls, type_name, *args, **kwargs):
        try:
            return cls.__types[type_name](*args, **kwargs)
        except KeyError:
            print("Could not create plant: Unknown plant type '{type_name}'")

    """
    Checks if the given value is valid for the height value

    Return value: bool
    """

    @staticmethod
    def is_height_valid(height: int) -> bool:
        return height > 0


class BasePlant(Plant, type_name="plant"):
    pass


class FloweringPlant(Plant, type_name="flower"):
    """
    Cretes a Flower object

    Keyworda args:
    name - The name of your flower
    height - The name of your flower
    color - The color of your flower
    """

    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.blooming = False

    """
    Define your flower as blooming
    """

    def bloom(self):
        self.blooming = True

    """
    Override from Plant class
    """

    def get_infos(self) -> str:
        msg = f"{super().get_infos()}, {self.color} flowers"
        if self.blooming:
            msg = f"{msg} (blooming)"
        return msg


class PrizeFlower(FloweringPlant, type_name="prized"):
    """
    Creates a PrizeFlower object

    Keyword arguments:
    name - The name of your flower
    height - The height of your flower
    color - The color of your flower
    prize_points - Points attributed to your flower
    """

    def __init__(self, name: str, height: int, color: str, prize_points: int):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    """
    Override from FloweringPlant class
    """

    def get_infos(self) -> str:
        return f"{super().get_infos()}, {self.prize_points} prize points"


class Garden:
    """
    Creates a Garden object

    Keyword arguments:
    owner - The name of the garden's owner
    """

    def __init__(self, owner: str):
        self.owner = owner
        self.content: dict[str, Plant] = {}

    """
    Adds a plant in the garden

    Keyword arguments:
    plant - The plant to add
    """

    def add_plant(self, plant: Plant):
        self.content[plant.name] = plant

    """
    Get the plant object from it's name

    Keyword arguments:
    name - The name of the wated plant

    Return values: The associated Plant object | None if not found
    """

    def get_plant(self, name: str):
        return self.content[name]

    """
    Increases the height of your plant

    Keyword arguments:
    name - The name of he plant you want to grow
    size - The amount it should be increased
    """

    def grow_plant(self, name: str, size: int) -> bool:
        return self.get_plant(name).grow(size)

    """
    Reports all informations of the garden
    """

    def report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.content.values():
            print(f"- {plant.get_infos()}")


class GardenStats:
    """
    Creates a GardenStats object
    """

    def __init__(self):
        self.regular = 0
        self.flowering = 0
        self.prize = 0
        self.total_added = 0
        self.total_growth = 0
        self.garden_count = 0

    """
    Retrieves the total amount of prize points of all
        the flowers inside the garden

    Return value: int
    """

    @staticmethod
    def get_total_points(garden: Garden) -> int:
        total = 0
        for plant in garden.content.values():
            if isinstance(plant, PrizeFlower):
                total += plant.prize_points
        return total


class GardenManager:
    """
    Creates a GardenManager object
    """

    def __init__(self):
        self.stats = GardenStats()

    """
    Add a garden that the manager will handle

    Keyword arguments:
    owner - The name of the new garden's owner
    """

    def add_garden(self, owner: str):
        self.gardens[owner] = Garden(owner)
        self.stats.garden_count += 1
        print(f"{owner} registered their garden")

    """
    Retrieves the garden owned by the specified person

    Keyword arguments:
    owner - The name of the owner you want the garden from

    Return value: Garden
    """

    def get_garden(self, owner: str) -> Garden:
        return self.gardens.get(owner)

    """
    Increases the specified plant height from a person's garden

    Keyword arguments:
    owner - The owner's name
    name - The plant's name
    size - The amount the height must be incremented
    """

    def grow_plant(self, owner: str, name: str, size: int):
        if self.get_garden(owner).grow_plant(name, size):
            self.stats.total_growth += size

    """
    Grows all plants from someone's garden

    Keyword arguments:
    owner - The owner's name
    size - The amount all plants must grow
    """

    def grow_all_plants(self, owner: str, size: int):
        print(f"{owner} is helping all the plants " +
              "from their garden to grow...")
        for plant in self.get_garden(owner).content.values():
            if plant.grow(size):
                self.stats.total_growth += size

    """
    Adds a plant in someone's garden

    Keyword arguments:
    owner - The name of the person that own the garden
        the plant shoul be added to
    plant - The plant that is going to be added
    """

    def add_plant_to_garden(self, owner: str, plant: Plant):
        if self.get_garden(owner) is None:
            return
        self.gardens[owner].add_plant(plant)
        self.stats.total_added += 1
        if isinstance(plant, PrizeFlower):
            self.stats.prize += 1
        elif isinstance(plant, FloweringPlant):
            self.stats.flowering += 1
        else:
            self.stats.regular += 1
        print(f"Added {plant.name} to {owner}'s Garden")

    """
    Shows all the statistics tracked by GardenStats
    """

    def show_stats(self):
        scores = ""
        for garden in self.gardens.values():
            if scores != "":
                scores = (
                    f"{scores}, {garden.owner}: " +
                    f"{GardenStats.get_total_points(garden)}"
                )
            else:
                scores = (
                        f"{garden.owner}: " +
                        f"{GardenStats.get_total_points(garden)}"
                )
        print(
            f"Plants added: {self.stats.total_added}," +
            f"Total growth: {self.stats.total_growth}cm"
        )
        print(
            f"Plant types: {self.stats.regular} regular, " +
            f"{self.stats.flowering} " +
            f"flowering, {self.stats.prize} prize flower\n"
        )
        print("Height validation: True (invalid operations not permitted)")
        print(f"Garden scores - {scores}")
        print(f"Total managed gardens: {self.stats.garden_count}")


"""
Creates the GardenManager fully initialized

Return value: GardenManager
"""


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
    manager.add_plant_to_garden("Alice",
                                Plant.create("plant", "Oak tree", 101))
    manager.add_plant_to_garden("Alice",
                                Plant.create("flower", "Rose", 26, "red"))
    manager.add_plant_to_garden("Bob",
                                Plant.create("flower", "Tulip", 10, "rose"))

    sunflo = Plant.create("prized", "Sunflower", 51, "yellow", 10)
    sunflo.bloom()

    manager.add_plant_to_garden("Alice", sunflo)

    print()
    manager.grow_all_plants("Alice", -3)
    print()
    manager.grow_plant("Bob", "Tulip", 5)

    manager.get_garden("Alice").report()
    manager.get_garden("Bob").report()

    print()
    manager.show_stats()
