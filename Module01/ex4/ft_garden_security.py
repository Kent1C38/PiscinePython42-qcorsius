"""
security_check(val_type: str, value: int)

Checks if the value is valid

Keyword arguments:
val_type -- The name of the value you're trying to updated
"""


def security_check(val_type: str, value: int) -> bool:
    unit: str
    match val_type:
        case "height":
            unit = "cm"
        case "age":
            unit = " days"
        case _:
            print(f"Invalid value name: {val_type}")
            return False
    if value < 0:
        print(f"Invalid operation attempted: {val_type} {value}{unit} [REJECTED]")
        print(f"Security: Negative {val_type} rejected")
        return False
    return True


class SecurePlant:
    """
    SecurePlant(name: str)

    Create a new SecurePlant object

    Keyword arguments:
    name -- The name of your new plant
    """

    def __init__(self, name: str):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {name}")

    """
    set_height(value: int)

    Set the plant's height to the specified value if it's valid

    Keyword arguments:
    value -- The new height (in cm)
    """

    def set_height(self, value: int):
        if security_check("height", value):
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    """
    set_age(value: int)

    Set the plant's age to the specified value if it's valid

    Keyword arguments:
    value -- The new age (in days)
    """

    def set_age(self, value: int):
        if security_check("age", value):
            self.__age = value
            print(f"Age updated: {value} days [OK]")

    """
    get_height()

    Returns the plant's height (in cm)
    """

    def get_height(self) -> int:
        return self.__height

    """
    get_age()

    Return the plant's age (in days)
    """

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    print(f"Current plant: {rose.name} ({rose.get_height()}cm, {rose.get_age()} days)")
