import sys
import os
import site


def get_package_path() -> str:
    """
    Retrieves the site-packages installation path.
    Returns 'Unknown' if detection fails.
    """
    try:
        packages = site.getsitepackages()
        return packages[0] if packages else "Unknown"
    except Exception:
        return "Unknown"


def display_matrix_status() -> None:
    """
    Detects the Python environment and displays status or instructions.
    Implements environment detection logic as required.
    """
    try:
        is_venv = sys.prefix != sys.base_prefix
        current_python = sys.executable

        if not is_venv:
            print("MATRIX STATUS: You're still plugged in")
            print(f"Current Python: {current_python}")
            print("Virtual Environment: None detected")
            print("\nWARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("\nTo enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\\Scripts\\activate   # On Windows")
            print("\nThen run this program again.")
        else:
            venv_path = sys.prefix
            venv_name = os.path.basename(venv_path)
            pkg_path = get_package_path()

            print("MATRIX STATUS: Welcome to the construct")
            print(f"Current Python: {current_python}")
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {venv_path}")
            print("\nSUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting "
                  "the global system.")
            print(f"\nPackage installation path:\n {pkg_path}")

    except Exception as e:
        print(f"Critical error in the Zion system: {e}")


if __name__ == "__main__":
    display_matrix_status()
