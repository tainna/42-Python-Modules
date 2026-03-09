import sys


def ft_stream_management() -> None:
    """
    Simulates a secure communication protocol using the three
    standard operating system streams: stdin, stdout, and stderr.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    archive_id: str = input("Input Stream active. Enter archivist ID: ")
    report: str = input("Input Stream active. Enter status report: ")

    print(f"[STANDARD] Archive status from ARCH_7742: {archive_id}: {report}")
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr
        )
    print("[STANDARD] Data transmission complete")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
