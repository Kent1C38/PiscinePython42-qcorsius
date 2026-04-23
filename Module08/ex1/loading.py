import sys


def check_dependencies():
    deps: set = {"pandas", "numpy", "matplotlib"}
    versions = {}

    found = set()
    for dep in deps:
        try:
            module = __import__(dep)
            versions[dep] = getattr(module, "__version__", "unknown")
            found.add(dep)
        except ImportError:
            ...

    if deps.difference(found):
        for dep in deps.difference(found):
            print(f"[ERROR] Missing dependency: {dep}")
        print("\nInstall with pip install -r <requirement file> OR poetry"
              " install")
        return None

    return versions


def detect_environment():
    in_venv = hasattr(sys, "real_prefix") or sys.prefix != sys.base_prefix

    print("\nEnvironment detection:")
    print(f"- Python path: {sys.executable}")
    print(f"- In virtualenv: {in_venv}")


def analyze_data():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(42)
    rows, cols = 10, 10
    matrix_data = np.random.randint(0, 100, size=(rows, cols))

    df = pd.DataFrame(matrix_data, columns=[f"Col_{i}" for i in range(cols)])

    print("\nData overview:")
    print(df)

    cols_mean = df.mean()
    print("\nColumns average:")
    print(cols_mean)

    plt.figure(figsize=(8, 6))
    plt.imshow(df, cmap="viridis", interpolation="nearest")
    plt.colorbar(label="Value")
    plt.title("Matrix Data Visualization")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.savefig("output.png")
    print("\nSaved image as 'output.png'")


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
