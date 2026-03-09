def ft_archive_creation() -> None:
    """
    Simulates the creation of a digital time capsule.
    Opens a new file in write mode, inscribes specific data entries,
    and safely seals the file.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("Initializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...")
    print("Inscribing preservation data...")

    archive = open("new_discovery.txt", "w")

    archive.write("[ENTRY 001] New quantum algorithm discovered\n")
    archive.write("[ENTRY 002] Efficiency increased by 347%\n")
    archive.write("[ENTRY 003] Archived by Data Archivist trainee\n")

    archive.close()

    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    ft_archive_creation()
