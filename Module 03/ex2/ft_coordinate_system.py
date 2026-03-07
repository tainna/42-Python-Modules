import math
from typing import Tuple


def calculate_distance(
        p1: Tuple[int, int, int],
        p2: Tuple[int, int, int]
) -> float:
    """
    Calculates the Euclidean distance between two 3D points
    using the 3D extension of the Pythagorean theorem.
    """
    dx: int = p2[0] - p1[0]
    dy: int = p2[1] - p1[1]
    dz: int = p2[2] - p1[2]

    """ Sum of the squared differences on each axis """
    sum_squares: int = (dx ** 2) + (dy ** 2) + (dz ** 2)

    return math.sqrt(sum_squares)


def parse_coordinates(coord_str: str) -> Tuple[int, int, int]:
    """
    Safely converts a comma-separated string into a 3D coordinate tuple.
    Relies on the int() cast, which natively raises a ValueError
    if the string contains non-numeric characters.
    """
    parts: list[str] = coord_str.split(',')

    x: int = int(parts[0])
    y: int = int(parts[1])
    z: int = int(parts[2])

    return (x, y, z)


def ft_coordinate_system() -> None:
    """
    Main simulation routine. Demonstrates tuple creation,
    distance calculation, string parsing, and unpacking mechanics.
    """
    print("=== Game Coordinate System ===\n")

    origin: Tuple[int, int, int] = (0, 0, 0)
    player_pos: Tuple[int, int, int] = (10, 20, 5)

    print(f"Position created: {player_pos}")

    dist: float = calculate_distance(origin, player_pos)
    print(f"Distance between {origin} and {player_pos}: {dist:.2f}\n")

    input_str: str = "3,4,0"
    print(f"Parsing coordinates: \"{input_str}\"")

    new_pos: Tuple[int, int, int] = parse_coordinates(input_str)
    print(f"Parsed position: {new_pos}")

    dist_new: float = calculate_distance(origin, new_pos)
    print(f"Distance between {origin} and {new_pos}: {dist_new}\n")

    bad_input: str = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{bad_input}\"")

    try:
        parse_coordinates(bad_input)
    except ValueError as e:
        """
        Catches specifically ValueError to avoid masking other critical bugs
        (like memory or syntax errors) that a generic Exception would hide.
        """
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("\nUnpacking demonstration:")

    """
    Tuple Unpacking: Instantly maps the 3 elements of the tuple
    into 3 distinct variables in a single operation.
    """
    p_x, p_y, p_z = new_pos

    print(f"Player at x={p_x}, y={p_y}, z={p_z}")
    print(f"Coordinates: X={p_x}, Y={p_y}, Z={p_z}")


if __name__ == "__main__":
    ft_coordinate_system()
