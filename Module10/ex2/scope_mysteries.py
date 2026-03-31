def mage_counter() -> callable:
    if not hasattr(mage_counter, "counter"):
        mage_counter.counter = 0

    mage_counter.counter += 1
    return lambda: mage_counter.counter


def spell_accumulator(initial_power: int) -> callable:
    if not hasattr(spell_accumulator, "power"):
        spell_accumulator.power = initial_power

    def accumulate(power):
        spell_accumulator.power += power
        return spell_accumulator.power

    return lambda x: accumulate(x)


def enchantment_factory(enchantment_type: str) -> callable:
    return lambda x: f"{enchantment_type} {x}"


def memory_vault() -> dict[str, callable]:
    if not hasattr(memory_vault, "storage"):
        memory_vault.storage = dict()

    def store(key, value):
        memory_vault.storage[key] = value

    def recall(key):
        return memory_vault.storage.get(key, "Memory not found!")

    return {"store": lambda key, val: store(key, val),
            "recall": lambda key: recall(key)}


if __name__ == "__main__":
    for _ in range(5):
        mage_counter()()
    print(mage_counter()())

    accumulator = spell_accumulator(5)
    print(accumulator(10))
    print(accumulator(15))

    fire_factory = enchantment_factory("Flaming")

    print(fire_factory("Sword"))
    print(fire_factory("Arrow"))

    mem_vault = memory_vault()
    mem_vault["store"]("test", "test_val")
    print(mem_vault["recall"]("test"))
    print(mem_vault["recall"]("none"))
