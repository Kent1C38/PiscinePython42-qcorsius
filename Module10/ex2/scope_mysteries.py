from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return lambda: increment()


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulate(to_add: int) -> int:
        nonlocal power
        power += to_add
        return power

    return lambda to_add: accumulate(to_add)


def enchantment_factory(enchantment_type: str) -> Callable:
    return lambda x: f"{enchantment_type} {x}"


def memory_vault() -> dict[str, Callable]:
    storage = dict()

    def store(key: Any, value: Any) -> None:
        storage[key] = value

    def recall(key: Any) -> Any:
        return storage.get(key, "Memory not found")

    return {"store": store,
            "recall": recall}


if __name__ == "__main__":
    print("Counter demo:")
    counter_1 = mage_counter()
    counter_2 = mage_counter()
    for _ in range(5):
        counter_1()
    print(f"Counter 1: {counter_1()}")
    print(f"Counter 2: {counter_2()}")

    print("\nAccumulator demo:")

    accumulator_1 = spell_accumulator(5)
    accumulator_2 = spell_accumulator(0)
    print(f"Accumulator 1: {accumulator_1(10)}")
    print(f"Accumulator 2: {accumulator_2(50)}")

    print("\nEnchat Factory demo:")
    fire_factory = enchantment_factory("Flaming")

    print(fire_factory("Sword"))
    print(fire_factory("Arrow"))

    print("\nMemory vault demo")
    mem_vault = memory_vault()
    mem_vault["store"]("test", "test_val")
    print(mem_vault["recall"]("test"))
    print(mem_vault["recall"]("none"))
