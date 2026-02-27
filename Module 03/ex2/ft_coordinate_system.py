import sys
import math


def ft_coordinate_system() -> None:
    """
    Reads command line arguments and displays them
    like argc and argv.
    """
    print("===   Game Coordinate System ====")

    # Slicing from index 1 givs us just the user-provided arguments
    user_args = sys.argv[1:]
    # "1:" Start at item #1 and take everything until the end.

    if not user_args:
        print("No arguments provided.")
        return

    scores = tuple()

    try:
        for arg in user_args:
            scores = (int(arg))
    except ValueError:
        print("Error: Invalid input")
        return

    s = math.sqrt((scores[0])**2 + (scores[1])**2 + (scores[2])**2)

    print(f"Position created: {scores}")
    print(f"Distance between (0, 0, 0) and ({scores[1]}")
    print(f"{scores[2]}, {scores[3]}): {s}")


if __name__ == "__main__":
    ft_coordinate_system()
