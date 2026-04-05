from typing import Callable


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    if not isinstance(spell1, Callable) or not isinstance(spell2, Callable):
        return lambda: None
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    if not isinstance(base_spell, Callable):
        return lambda: None
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: callable, spell: callable) -> callable:
    if not isinstance(condition, Callable) or not isinstance(spell, Callable):
        return lambda: None
    return lambda target, power: (spell(target, power)
                                  if condition(target, power)
                                  else "Spell fizzled")


def spell_sequence(spells: list[callable]) -> callable:
    return lambda target, power: [spell(target, power) for spell in spells]


if __name__ == "__main__":

    def fireball(target: str, power: int):
        return f"Fireball hits {target} and deals {power} damage"

    def heal(target: str, power: int):
        return f"Healing {target} for {power} HP"

    def is_spell_valid(target: str, power: int):
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
