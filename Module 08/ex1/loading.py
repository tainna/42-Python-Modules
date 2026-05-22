import importlib
from typing import List
import importlib.metadata


def check_dependencies(libs: List[str]) -> bool:
    """Checks if required libraries are installed and prints their versions."""
    all_available = True
    print("LOADING STATUS: Loading programs...")

    for lib in libs:
        try:
            # Try to import the module dynamically
            module = importlib.import_module(lib)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {lib} ({version}) - Ready for deployment")
        except ImportError:
            print(f"[MISSING] {lib} - System alert: program not found")
            all_available = False

    return all_available


def run_matrix_analysis() -> None:
    """Simulates data processing and saves a visualization."""
    required = ["pandas", "numpy", "matplotlib"]

    if not check_dependencies(required):
        print("\nERROR: Required programs are not loaded.")
        print("Use 'pip install -r requirements.txt' or 'poetry install'.")
        return

    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        print("Analyzing Matrix data...")
        # Simulate data engineering work
        data = pd.DataFrame({
            'signal': np.random.randn(100).cumsum()
        })

        # Generate the required visualization
        plt.figure(figsize=(10, 5))
        plt.plot(data['signal'], color='green')
        plt.title("Matrix Data Stream")
        plt.savefig("matrix_analysis.png")
        print("Analysis complete! Results saved to: matrix_analysis.png")

    except Exception as e:
        print(f"An unexpected error occurred during analysis: {e}")


if __name__ == "__main__":
    run_matrix_analysis()
