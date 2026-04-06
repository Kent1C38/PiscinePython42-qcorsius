from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    match operation:
        case "add": callable_op = lambda x, y: operator.add(x, y)
        case "multiply": callable_op = lambda x, y: operator.mul(x, y)
        case "max": callable_op = lambda x, y: max(x, y)
        case "min": callable_op = lambda x, y: min(x, y)
        case _: callable_op = lambda _, __: None

    if spells:
        return reduce(callable_op, spells)
    return 0


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
def memoized_fibonacci(n: int):
    if n < 2 and n >= 0:
        return n
    elif n < 0:
        return 0

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispactcher() -> callable:

    @singledispatch
    def cast(spell):
        return f"Unknown Spell type: {type(spell)}"

    @cast.register(str)
    def _(spell):
        return f"Casting Enchantment: {spell}"

    @cast.register(int)
    def _(spell):
        return f"Casting Damage Spell: {spell} power"

    @cast.register(list)
    def _(spell):
        results = [cast(s) for s in spell]
        return "Multi-cast:\n" + "\n".join(results)

    return cast


if __name__ == "__main__":
    def fibo(x: int):
        if x < 2 and x >= 0:
            return x
        elif x < 0:
            return 0
        return fibo(x-1) + fibo(x-2)
    print("="*5 + "Reducer demo" + "="*5)
    print(spell_reducer([1, 2, 3, 4], "add"))
    print(spell_reducer([1, 2, 3, 4], "multiply"))
    print(spell_reducer([1, 2, 3, 4], "max"))
    print(spell_reducer([1, 2, 3, 4], "min"))
    print(spell_reducer([], "multiply"))
    print(spell_reducer([1, 2, 3, 4], "hfwuvwngv"))

    print("\n" + "="*5 + "Partial completing demo" + "="*5)

    def enchant(power: int, element: str, target) -> str:
        return f"Target: {target}, spell element: {element} ({power} power)"

    enchanter = partial_enchanter(enchant)
    print(enchanter["fire_enchant"]("test")())

    print("\n" + "="*5 + "LRU Cache demo" + "="*5)
    from time import perf_counter
    start = perf_counter()
    print(memoized_fibonacci(15), end="")
    print(f" ({perf_counter() - start: 0.6f}s elapsed)")

    start = perf_counter()
    print(memoized_fibonacci(30), end="")
    print(f" ({perf_counter() - start: 0.6f}s elapsed)")

    start = perf_counter()
    print(memoized_fibonacci(35), end="")
    print(f" ({perf_counter() - start: 0.6f}s elapsed)")

    print("\nDemo without memoisation")
    start = perf_counter()
    print(fibo(35), end="")
    print(f" ({perf_counter() - start: 0.6f}s elapsed)")

    print("\n" + "="*5 + "Dispatcher demo" + "="*5)

    dispatch = spell_dispactcher()
    print(dispatch("test"), end="\n\n")
    print(dispatch(50), end="\n\n")
    print(dispatch(["re-test", 40, lambda: "normalement ça marche pas"]))
