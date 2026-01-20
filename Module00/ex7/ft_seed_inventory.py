def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_name: str = f"{seed_type.capitalize()} seeds"
    match unit:
        case "packets":
            print(f"{seed_name}: {quantity} {unit} available")
        case "grams":
            print(f"{seed_name}: {quantity} {unit} total")
        case "area":
            print(f"{seed_name}: covers {quantity} square meters")
        case _:
            print("Unknown unit type.")
