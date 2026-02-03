import sys


def ft_command_quest() -> None:
    """
    Reads command line arguments and displays them
    like argc and argv.
    """
    print("=== Command Quest ====")

    # sys.argv is a list containing the script name and all arguments
    program_name: str = sys.argv[0]

    # Slicing from index 1 givs us just the user-provided arguments
    user_args: list[str] = sys.arg[1:]
    # "1:" Start at item #1 and take everything until the end.

    if not user_args:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {len(sys.argv)}")
        return

    print(f"Program name: {program_name}")
    print(f"Arguments received: {len(user_args)}")

    # Enumerate helps us get both the index (counter) and value
    for i, arg in enumerate(user_args, start=1):
        print(f"Argument {i}: {arg}")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
