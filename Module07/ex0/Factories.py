from .AbstractFactory import CreatureFactory
from .AbstractCreature import Creature
from .Creatures import Flameling, Pyrodon, Aquabub, Torragon


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> Creature:
        return Pyrodon("Pyrodon", "Fire/Flying")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> Creature:
        return Torragon("Torragon", "Water")
