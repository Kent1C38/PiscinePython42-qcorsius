from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        return lambda: None
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        return lambda: None
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        return lambda: None
    return lambda target, power: (spell(target, power)
                                  if condition(target, power)
                                  else "Spell fizzled")


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [spell(target, power) for spell in spells]


if __name__ == "__main__":

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} and deals {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Healing {target} for {power} HP"

    def is_spell_valid(target: str, power: int) -> bool:
        return len(target) > 3 and power > 0

    print(spell_combiner(fireball, heal)("Dragon", 5))

    print()

    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Snowman", 5))

    print()

    spell_cast = conditional_caster(is_spell_valid, heal)
    print(spell_cast("Dummy", 0))
    print(spell_cast("Dummy", 5))

    print()

    sequence = spell_sequence([fireball, heal])
    print(sequence("test", 8))
