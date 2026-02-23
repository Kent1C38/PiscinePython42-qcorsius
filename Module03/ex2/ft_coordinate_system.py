from math import sqrt


class Coord:

    def __init__(self, x: int, y: int, z: int):
        self._x = x
        self._y = y
        self._z = z

    def getX(self) -> int:
        return self._x

    def getY(self) -> int:
        return self._y

    def getZ(self) -> int:
        return self._z

    def get(self) -> tuple[int, int, int]:
        return (self.getX(), self.getY(), self.getZ())

    @staticmethod
    def from_str(string: str) -> "Coord":
        tmp = string.split(",")
        try:
            print(f"Parsing coordinates \"{string}\"")
            parsed_coord = Coord(int(tmp[0]), int(tmp[1]), int(tmp[2]))
            print(f"Parsed position: {parsed_coord.get()}")
            return parsed_coord
        except ValueError as e:
            print(f"Parsing invalid coordinates: \"{string}\"")
            print(f"Error parsing coordinates: {e}")


def distance_between_points(coord1: Coord, coord2: Coord) -> float:
    x1, y1, z1 = coord1.get()
    x2, y2, z2 = coord2.get()
    return sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    origin = Coord(0, 0, 0)

    print()
    pos1 = Coord(10, 20, 5)
    print(f"Position created: {pos1.get()}")
    print(f"Distance between {origin.get()} and {pos1.get()}:" +
          f"{distance_between_points(origin, pos1): 0.2f}")

    print()
    pos2 = Coord.from_str("3,4,0")
    print(f"Distance between {origin.get()} and {pos2.get()}:" +
          f"{distance_between_points(origin, pos2): 0.2f}")

    print()
    pos_err = Coord.from_str("abc,def,ghi")

    print("\nUnpacking demo:")
    x, y, z = pos2.get()
    print(f"Player as x={x}, y={y}, z={z}")
