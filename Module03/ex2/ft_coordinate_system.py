import sys
from math import sqrt


def create_coord(x: int, y: int, z: int):
    return (x, y, z)


def parse_coord(string: str):
    temp = string.split(',')
    try:
        coord = create_coord(int(temp[0]), int(temp[1]), int(temp[2]))
        print(f"Parsing coordinates: \"{string}\"")
        print(f"Parsed position: {coord}")
        return coord
    except ValueError as e:
        print(f"Parsing invalid arguments: {string}")
        print(f"Error parsing coordinates: {e}")


def distance_between_points(coord1, coord2) -> float:
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    user_coord = None
    try:
        user_coord = parse_coord(sys.argv[1])
    except IndexError:
        print("No arguments given: fallback to demo")
    origin = create_coord(0, 0, 0)
    pos1 = create_coord(10, 20, 5)
    print(f"Position created: {pos1}")
    print(f"Distance between: {origin} and {pos1}: " +
          f"{distance_between_points(origin, pos1): .2f}\n")
    pos2 = parse_coord("3,4,0")
    print(f"Distance between: {origin} and {pos2}: " +
          f"{distance_between_points(origin, pos2): .1f}\n")
    pos3 = parse_coord("abc,def,ghi")

    print("\nUnpacking Demo (Works if user input is valid)")
    if user_coord is not None:
        print(f"User position: {user_coord}")
        x, y, z = user_coord
        print(f"Unpacked coords: x={x}, y={y}, z={z}")
    else:
        print("User input was invalid, cannot show Unpacking")
