from .AbstractBattleStrategy import BattleStrategy
from ex0.AbstractCreature import Creature
from ex1.Capabilities import TransforfmCapability, HealCapability


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            self.invalid_creature_error(creature)

        turn = creature.attack()
        return turn


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransforfmCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            self.invalid_creature_error(creature)

        turn = creature.transform()
        turn += f"\n{creature.attack()}"
        turn += f"\n{creature.revert()}"
        return turn


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            self.invalid_creature_error(creature)

        turn = creature.attack()
        turn += f"\n{creature.heal()}"
        return turn
