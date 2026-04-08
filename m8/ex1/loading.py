import importlib
import sys


def check_dependency(package_name: str) -> tuple[bool, str]:
    try:
        module = importlib.import_module(package_name)
        version: str = getattr(module, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, ""


def check_all_dependencies() -> bool:
    dependencies: list[tuple[str, str]] = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computing ready"),
        ("requests", "Network access ready"),
        ("matplotlib", "Visualization ready")
    ]
    all_installed: bool = True
    for package_name, description in dependencies:
        installed, version = check_dependency(package_name)
        if installed:
            print(f"[OK] {package_name} ({version}) - {description}")
        else:
            print(f"[KO] {package_name} - MISSING")
            print("Install with: pip install -r requirements.txt")
            print("Or with Poetry: poetry install")
            all_installed = False
    return all_installed


def generate_matrix_analysis() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    data_points: int = 1000
    values = np.random.normal(loc=50, scale=15, size=data_points)
    data_frame = pd.DataFrame({
        "index": range(data_points),
        "value": values
    })

    plt.figure(figsize=(10, 5))
    plt.plot(data_frame["index"], data_frame["value"], color="green")
    plt.title("Matrix Analysis")
    plt.xlabel("Data Point")
    plt.ylabel("Signal Value")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("\nAnalyzing Matrix data...")
    print(f"Processing {data_points} data points...")
    print("Generating visualization...\n")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    if not check_all_dependencies():
        sys.exit(1)

    generate_matrix_analysis()


if __name__ == "__main__":
    main()
