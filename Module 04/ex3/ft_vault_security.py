def ft_vault_security() -> None:
    """
    Demonstrates secure file handling using Python's context managers.
    Ensures files are automatically closed (sealed) via the 'with' statement,
    preventing data corruption and memory leaks (RAII principle).
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("SECURE EXTRACTION:")

    try:
        with open("archive_read.txt", "r") as r:
            data_r: str = r.read()
            print(data_r, end="")
    except FileNotFoundError:
        print("ERROR: Storage vault not found")

    print("\nSECURE PRESERVATION:")

    with open("archive_write.txt", "w") as w:
        phrase: str = "[CLASSIFIED] New security protocols archived\n"
        w.write(phrase)
        print(phrase)

    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
