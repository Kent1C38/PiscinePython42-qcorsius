from functools import reduce, partial, lru_cache


def spell_reducer(spells: list[int], operation: str) -> int:
    match operation:
        case "add": callable_op = lambda x, y: x + y
        case "multiply": callable_op = lambda x, y: x * y
        case "max": callable_op = lambda x, y: max(x, y)
        case "min": callable_op = lambda x, y: min(x, y)
        case _: callable_op = lambda _, __: None

    return reduce(callable_op, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": lambda t: partial(base_enchantment,
                                          power=50,
                                          element="fire",
                                          target=t),

        "ice_enchant": lambda t: partial(base_enchantment,
                                         power=50,
                                         element="ice",
                                         target=t),

        "lightning_enchant": lambda t: partial(base_enchantment,
                                               power=50,
                                               element="lightning",
                                               target=t)
    }


@lru_cache
def memoized_fibonacci(n):


if __name__ == "__main__":
    print(spell_reducer([1, 2, 3, 4], "add"))
    print(spell_reducer([1, 2, 3, 4], "multiply"))
    print(spell_reducer([1, 2, 3, 4], "max"))
    print(spell_reducer([1, 2, 3, 4], "min"))

    def enchant(power: int, element: str, target) -> str:
        return f"Target: {target}, spell: {element} ({power} power)"

    enchanter = partial_enchanter(enchant)
    print(enchanter["fire_enchant"]("test")())
