def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x.get("power", 0), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x.get("power", 0) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(list(map(lambda x: x.get("power", 0), mages))),
        "min_power": min(list(map(lambda x: x.get("power", 0), mages))),
        "avg_power": sum(list(
            map(lambda x: x.get("power", 0), mages))) / len(mages)
    }


if __name__ == "__main__":
    print(artifact_sorter([{"power": 5}, {"power": 10}, {"power": 6},
                           {"name": "test"}]))

    print(power_filter(
        [{"power": 50}, {"power": 20}, {"power": 10}, {"power": 5}], 15))

    print(spell_transformer(["test", "yes", "no"]))

    print(mage_stats([
        {"name": "test", "power": 15},
        {"name": "yes", "power": 10},
        {"name": "no", "power": 5}
    ]))
