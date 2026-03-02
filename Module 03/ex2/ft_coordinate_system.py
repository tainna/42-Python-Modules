import math


def calculate_distance(
        p1: tuple[int, int, int],
        p2: tuple[int, int, int]
) -> int:
    """
    Calculates the Euclidean distance between two 3D points,
    """
    # 3D pythagorean theorem
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]

    # calculate sum of squares
    sum_squares = (dx ** 2) + (dy ** 2) + (dz ** 2)

    return math.sqrt(sum_squares)


def parse_coordinates(coord_str: str) -> tuple[int, int, int]:
    """
    Parses a string 'x,y,z' into a tuple of integers.
    Raises ValueError if formatting is bad.
    """
    # 1. Split the string bby comma
    parts = coord_str.split(',')

    # 2. Convert each part to int (this might raise ValueError)
    # We create a tuple from a generator expression or list
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")

    # 1. Manuak Creation
    # We define origin and a player position using tuples
    origin = (0, 0, 0)
    player_pos = (10, 20, 5)

    print(f"Position created: {player_pos}")

    dist = calculate_distance(origin, player_pos)
    # :.2f limits decimal places to 2
    print(f"Distance between {origin} and {player_pos}: {dist:.2f}")

    # 2. Parsing Valid String
    input_str = "3,4,0"
    print(f"Parsing coordinates: \"{input_str}\"")

    # We call our parse function
    new_pos = parse_coordinates(input_str)
    print(f"Parsed position: {new_pos}")

    dist_new = calculate_distance(origin, new_pos)
    print(f"Distance between {origin} and {new_pos}: {dist_new}")

    # 3. Handling Invalid String
    bad_input = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{bad_input}\"")

    try:
        parse_coordinates(bad_input)
    except Exception as e:
        # We catch the error to show details instead of crashing
        print(f"Error parsing coordinates: {e}")
        # type{e}._name_gives us "ValueError"
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    # 4. Tuple Unpacking Demo
    print("Unpacking demonstration")

    # Unpacking: Assign items in tuple to separate variables
    p_x, p_y, p_z = new_pos

    print(f"Player at x={p_x}, y={p_y}, z={p_z}")
    print(f"coordinates: X={p_x}, Y={p_y}, Z={p_z}")


if __name__ == "__main__":
    ft_coordinate_system()
