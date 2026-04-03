from typing import Callable


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    if not isinstance(spell1, Callable) or not isinstance(spell2, Callable):
        return lambda: None
    return lambda x: (spell1(x), spell2(x))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    if not isinstance(base_spell, Callable):
        return lambda: None
    return lambda: base_spell() * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    if not isinstance(condition, Callable) or not isinstance(spell, Callable):
        return lambda: None
    return lambda x: spell(x) if condition(x) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda x: [spell(x) for spell in spells]


if __name__ == "__main__":
    print(*spell_combiner(lambda x: f"Hit {x}",
                          lambda x: f"Heal {x}")("Dragon"))

    print(power_amplifier(lambda: "Fireball ", 5)())

    print(conditional_caster(
        lambda x: len(x) <= 15, lambda x: f"Cast {x}")("fireball"))

    print(spell_sequence([lambda x: f"Fireball on {x}",
                          lambda x: f"Ice spike on {x}"])("Dragon"))
