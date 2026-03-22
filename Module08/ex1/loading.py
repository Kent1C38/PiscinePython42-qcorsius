# loading.py

import sys


def check_dependencies():
    deps = ["pandas", "numpy", "matplotlib"]
    versions = {}

    for dep in deps:
        try:
            module = __import__(dep)
            versions[dep] = getattr(module, "__version__", "unknown")
        except ImportError:
            print(f"[ERROR] Missing dependency: {dep}")
            print(f"Install with pip install {dep} OR poetry install "
                  "inside a venv")
            return None

    return versions


def detect_environment():
    import os

    in_venv = hasattr(sys, "real_prefix") or sys.prefix != sys.base_prefix
    poetry = "POETRY_ACTIVE" in os.environ or "poetry" \
        in sys.executable.lower()

    print("\nEnvironment detection:")
    print(f"- Python path: {sys.executable}")
    print(f"- In virtualenv: {in_venv}")
    print(f"- Likely using Poetry: {poetry}")


def analyze_data():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Simulated Matrix data
    np.random.seed(42)
    rows, cols = 10, 10
    matrix_data = np.random.randint(0, 100, size=(rows, cols))

    df = pd.DataFrame(matrix_data, columns=[f"Col_{i}" for i in range(cols)])

    print("\nData overview:")
    print(df)

    # Analysis
    cols_mean = df.mean()
    print("\nColumns average:")
    print(cols_mean)

    # Visualization
    plt.figure(figsize=(8, 6))
    plt.imshow(df, cmap="viridis", interpolation="nearest")
    plt.colorbar(label="Value")
    plt.title("Matrix Data Visualization")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.show()


def main():
    print("=== Loading.py - Matrix Data Analysis ===")

    versions = check_dependencies()
    if versions is None:
        return

    print("\nInstalled package versions:")
    for k, v in versions.items():
        print(f"- {k}: {v}")

    detect_environment()
    analyze_data()


if __name__ == "__main__":
    main()
