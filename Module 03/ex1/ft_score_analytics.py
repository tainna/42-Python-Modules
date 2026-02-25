import sys


def ft_score_analytics() -> None:
    """
    Reads command line arguments and displays them
    like argc and argv.
    """
    print("===  Player Score Analytics ====")

    # Slicing from index 1 givs us just the user-provided arguments
    user_args = sys.argv[1:]
    # "1:" Start at item #1 and take everything until the end.

    if not user_args:
        print("No arguments provided.")
        print("Usage: python3 ft_score_analytics.py <score1> <score2>")
        return

    scores = []

    try:
        for arg in user_args:
            scores.append(int(arg))
    except ValueError:
        print("Error: Invalid input")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High core: {max(scores)}")
    print(f"Low sore: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
