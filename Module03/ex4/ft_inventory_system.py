from sys import argv


def parse_to_inv(string: str, inv: dict):
    try:
        tmp = string.split(":")
        inv[tmp[0]] = int(tmp[1])
    except ValueError as e:
        print(f"Error occured while parsing data to inventory: {e}")


def count_items(*arg):
    total = 0
    for item in arg:
        total += item
    return total


def show_inv(inv: dict):
    total_items = count_items(*inv.values())
    sorted_inv = dict(
        sorted(inv.items(), key=lambda item: item[1], reverse=True))
    for item, count in sorted_inv.items():
        print(f"{item}: {count} units ({count/total_items*100:.1f}%)")


def get_most_item(inv: dict):
    biggest = ([], 0)
    for item, count in inv.items():
        if count > biggest[1]:
            biggest = ([item], count)
        elif count == biggest[1]:
            biggest[0].append(item)
    return biggest


def get_least_item(inv: dict):
    lowest = None
    for item, count in inv.items():
        if lowest is None or count < lowest[1]:
            lowest = ([item], count)
        elif count == lowest[1]:
            lowest[0].append(item)
    return lowest


def concat_str_list(ls: list) -> str:
    res = None
    for string in ls:
        if res is None:
            res = string
        else:
            res += f", {string}"
    return res


if __name__ == "__main__":
    inventory = {}
    for arg in argv[1:]:
        parse_to_inv(arg, inventory)
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {count_items(*inventory.values())}")
    print(f"Unique items count: {len(inventory.keys())}")

    print("\n=== Current Inventory ===")
    show_inv(inventory)

    print("\n=== Inventory Statistics ===")
    most_item = get_most_item(inventory)
    print("Most abundant: "
          + f"{concat_str_list(most_item[0])} ({most_item[1]} units)")
    least_item = get_least_item(inventory)
    print("Least abundant: "
          + f"{concat_str_list(least_item[0])} ({least_item[1]} units)")

    print("\n=== Item Categories ===")
    moderate_category = {k: v for k, v in inventory.items() if v >= 4}
    scarce_category = {k: v for k, v in inventory.items() if v < 4}
    print(f"Moderate: {moderate_category}")
    print(f"Scarce: {scarce_category}")

    print("\n=== Management Suggestions ===")
    refill_needed = [k for k, v in inventory.items() if v <= 1]
    print(f"Restock needed: {refill_needed}")

    print("\n=== Dictionnary Properties Demo ===")
    print(f"Dictionnary keys: {list(inventory.keys())}")
    print(f"Dictionnary values: {list(inventory.values())}")
    sword_is_present = "sword" in inventory.keys()
    print(f"Sample lookup - 'sword' in inventory: {sword_is_present}")
