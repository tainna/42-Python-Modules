def ft_ancient_text() -> None:
    """
    Simulates a digital archive recovery system.
    Safely attempts to open, read, and close a specific text file.
    Handles missing files gracefully without crashing the system.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    try:
        archive = open("ancient_fragment.txt")

        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...\n")
        print("RECOVERED DATA:")

        arq = archive.read()
        print(arq, end="")
        # end="" prevents adding an extra empty line at the end
        archive.close()
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    ft_ancient_text()
