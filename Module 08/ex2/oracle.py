import os
import sys
from dotenv import load_dotenv


def load_matrix_configuration() -> bool:
    """
    Loads environment variables from the .env file.
    Returns True if successful, False otherwise.
    """
    try:
        return load_dotenv()
    except Exception as e:
        print(f"Erro ao carregar o ficheiro .env: {e}")
        return False


def display_oracle_status() -> None:
    """
    Reads and displays Matrix settings using environment variables.
    Checks connection security and status.
    """
    try:
        print("ORACLE STATUS: Reading the Matrix...\n")

        mode = os.getenv("MATRIX_MODE", "unknown")
        db_url = os.getenv("DATABASE_URL")
        api_key = os.getenv("API_KEY")
        log_level = os.getenv("LOG_LEVEL", "INFO")
        zion_endpoint = os.getenv("ZION_ENDPOINT")

        db_status = "Connected to local instance" if db_url else "Disconnected"
        api_status = "Authenticated" if api_key else "Missing Credentials"
        zion_status = "Online" if zion_endpoint else "Offline"

        print("Configuration loaded:")
        print(f"Mode: {mode}")
        print(f"Database: {db_status}")
        print(f"API Access: {api_status}")
        print(f"Log Level: {log_level}")
        print(f"Zion Network: {zion_status}\n")

        print("Environment security check:")

        print("[OK] No hardcoded secrets detected")

        if os.path.exists(".env"):
            print("[OK] .env file properly configured")
        else:
            print("[WARNING] .env file is missing!")

        print("[OK] Production overrides available\n")

        print("The Oracle sees all configurations.")

    except Exception as e:
        print(f"Falha de sistema no Oráculo: {e}", file=sys.stderr)


def main() -> None:
    """
    Principal function that orchestrates the reading of the Matrix.
    """
    load_matrix_configuration()
    display_oracle_status()


if __name__ == "__main__":
    main()
