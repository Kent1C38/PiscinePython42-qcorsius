from abc import ABC, abstractmethod
from ex0.AbstractCreature import Creature


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> str:
        ...

    def raise_invalid_creature_error(self, creature: Creature) -> None:
        raise Exception(f"{creature.name} is not suitable "
                        f"for {self.__class__.__name__} !")
