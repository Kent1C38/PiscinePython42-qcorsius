from ..ex0.Card import Card
from ..ex0.CreatureCard import CreatureCard
from ..ex1.SpellCard import SpellCard
from ..ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory
from enum import Enum
import random


class FantasyCreatures(Enum):
    DRAGON = (CreatureCard("Dragon", 5, "Legendary", 10, 7),
              25.0)
    GOBLIN = (CreatureCard("Goblin", 2, "Common", 3, 5),
              75.0)

    def get_card(self):
        return self.value[0]

    @staticmethod
    def get_chances():
        return {x.name.lower(): x.value[1] for x in FantasyCreatures}


class FantasySpells(Enum):
    FIREBALL = ((SpellCard("Fire Ball", 4, "Rare",
                "Deals 3 damage to the enemy"), 3),
                50.0)

    LIGHTNING_STRIKE = ((SpellCard("Lightning Strike", 5, "Epic",
                                   "Deals 5 damage to the enemy"), 5),
                        50.0)

    def get_card(self):
        return self.value[0][0]

    def get_power(self):
        return self.value[0][1]

    @staticmethod
    def get_chances():
        return {x.name.lower(): x.value[1] for x in FantasySpells}


class FantasyArtifacts(Enum):
    MANA_RING = (ArtifactCard("Mana Ring", 7, "Epic", 10, "+1 mana per turn"),
                 100.0)

    def get_card(self):
        return self.value[0]

    @staticmethod
    def get_chances():
        return {x.name.lower(): x.value[1] for x in FantasyArtifacts}


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, int):
            llist = [x.get_card() for x in FantasyCreatures]
            if name_or_power < 0 or name_or_power >= len(llist):
                return None
            return llist[name_or_power]

        if name_or_power is None:
            creatures = self.get_supported_types()["creatures"]
            if not creatures:
                return None
            return self.create_creature(random.choice(creatures))

        if name_or_power.upper() in [x.name for x in FantasyCreatures]:
            return FantasyCreatures[name_or_power.upper()].get_card()

        return None

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, int):
            llist = [x.get_card() for x in FantasySpells]
            if name_or_power < 0 or name_or_power >= len(llist):
                return None
            return llist[name_or_power]

        if name_or_power is None:
            spells = self.get_supported_types()["spells"]
            if not spells:
                return None
            return self.create_spell(random.choice(spells))

        if name_or_power.upper() in [x.name for x in FantasySpells]:
            return FantasySpells[name_or_power.upper()].get_card()

        return None

    def create_artifact(self, name_or_power: str | int | None) -> Card:
        if isinstance(name_or_power, int):
            llist = [x.get_card() for x in FantasyArtifacts]
            if name_or_power < 0 or name_or_power >= len(llist):
                return None
            return llist[name_or_power]

        if name_or_power is None:
            artifacts = self.get_supported_types()["artifacts"]
            if not artifacts:
                return None
            return self.create_artifact(random.choice(artifacts))

        if name_or_power.upper() in [x.name for x in FantasyArtifacts]:
            return FantasyArtifacts[name_or_power.upper()].get_card()

        return None

    def create_themed_deck(self, size: int) -> dict:

        hand = {}

        def roll_drop(drop_table: dict) -> str:
            total = sum(drop_table.values())
            roll = random.uniform(0, total)

            current = 0
            for item, chance in drop_table.items():
                current += chance
                if roll <= current:
                    return item

        type_chances = {"creature": 50, "spell": 30, "artifact": 20}

        for _ in range(size):
            match roll_drop(type_chances):
                case "creature":
                    key = self.create_creature(
                        roll_drop(FantasyCreatures.get_chances()))

                case "spell":
                    key = self.create_spell(
                        roll_drop(FantasySpells.get_chances()))

                case "artifact":
                    key = self.create_artifact(
                        roll_drop(FantasyArtifacts.get_chances()))

            hand[key] = hand.get(key, 0) + 1

        return hand

    def get_supported_types(self) -> dict:
        return {
            "creatures": [x[0].lower() for x in
                          FantasyCreatures.__members__.items()],
            "spells": [x[0].lower() for x in
                       FantasySpells.__members__.items()],
            "artifacts": [x[0].lower() for x in
                          FantasyArtifacts.__members__.items()]
        }


if __name__ == "__main__":
    factory = FantasyCardFactory()
    print({key.name: value for key, value in
           factory.create_themed_deck(10).items()})
    test = {"test": 0}
