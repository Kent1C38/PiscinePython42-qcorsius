class Plant:
    """
    Creates a plant object

    Keyword arguments:
    name -- The name of your plant
    height -- The height of your plant (in cm)
    age -- How long your plant has been alive since (in day)
    """

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show_info(self):
        """
        Shows useful infos of your plant
        """
        pass


class Flower(Plant):
    """
    Creates a flower object

    Keyword arguments:
    name -- The name of your plant
    height -- The height of your plant (in cm)
    age -- How long your plant has been alive since (in day)
    color -- The color in full letters of your flower
    """

    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    """ Prints that your flower is blooming """

    def bloom(self):
        print(f"{self.name} is blooming beautifully !")

    """Override from Plant class"""

    def show_info(self):
        print(
            f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color"
        )


class Tree(Plant):
    """
    Creates a Tree object

    Keyword arguments:
    name -- The name of your plant
    height -- The height of your plant (in cm)
    age -- How long your plant has been alive since (in day)
    trunk_diameter -- The diameter (in cm) of your tree
    """

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    """ Define if the tree provides shades """

    def produce_shade(self):
        print(f"{self.name} provides some shade")

    """ Override from Plant class """

    def show_info(self):
        print(
            f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    """
    Creates a Vegetable object

    Keyword arguments:
    name -- The name of your plant
    height -- The height of your plant (in cm)
    age -- How long your plant has been alive since (in day)
    harvest_season -- The name of the harvest season of your vegetable in plain text
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritionnal_value: str,
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritionnal_value = nutritionnal_value

    """ Shows nutritionnal infos of your vegetable """

    def show_nutritionnal_info(self):
        print(self.nutritionnal_value)

    """ Override from Plant class """

    def show_info(self):
        print(
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest"
        )


"""
Checks if the object is an instance of the given class

Keyword arguments
obj -- The object you want to check
cls -- The class you want to knok if your oject is an instance of
"""


def check_instance(obj: object, cls: type):
    current_class = obj.__class__
    while True:
        if current_class == cls:
            return True
        bases = current_class.__bases__
        if len(bases) == 0:
            return False
        current_class = bases[0]


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    liste: Plant = []

    liste.append(Flower("Rose", 25, 30, "red"))
    liste.append(Tree("Oak", 500, 1825, 50))
    liste.append(Vegetable("Tomato", 80, 90, "summer", "Tomato is rich in vitamin C"))

    for obj in liste:
        obj.show_info()
        if check_instance(obj, Flower):
            obj.bloom()
        elif check_instance(obj, Tree):
            obj.produce_shade()
        elif check_instance(obj, Vegetable):
            obj.show_nutritionnal_info()
        print()
