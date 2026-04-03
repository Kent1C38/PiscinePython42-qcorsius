from ..elements import create_air
from elements import create_fire
import alchemy.potions


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew {create_air()} " +
            f"and {alchemy.potions.strenght_potion()} " +
            f"mixed with {create_fire()}")
