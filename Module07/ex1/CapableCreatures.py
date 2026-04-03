from ex0.AbstractCreature import Creature
from .Capabilities import HealCapability, TransforfmCapability


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a few amount!"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a large amount!"


class Shiftling(Creature, TransforfmCapability):

    def transform(self) -> str:
        self.transform_active = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transform_active = False
        return f"{self.name} returns to normal"

    def attack(self) -> str:
        if self.transform_active:
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} attacks normally"


class Morphagon(Creature, TransforfmCapability):
    def transform(self) -> str:
        self.transform_active = True
        return f"{self.name} morphs into a draconic battle form!"

    def revert(self) -> str:
        self.transform_active = False
        return f"{self.name} stabilizes it's form"

    def attack(self) -> str:
        if self.transform_active:
            return f"{self.name} unleashes a devastating morph strike!"
        else:
            return f"{self.name} attacks normally"
