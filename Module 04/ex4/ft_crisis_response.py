def test_archive_access(filename: str, is_routine: bool = False) -> None:
    """
    Attempts to safely read an archive using context managers.
    Handles FileNotFoundError and PermissionError gracefully.
    """
    if is_routine:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as f:
            data = f.read()
        clean_data = data.strip()
        print(f"SUCCESS: Archive recovered - ``{clean_data}''")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    test_archive_access("lost_archive.txt")

    test_archive_access("classified_vault.txt")

    test_archive_access("standard_archive.txt", is_routine=True)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
