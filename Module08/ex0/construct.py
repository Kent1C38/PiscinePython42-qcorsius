import sys
import os
import site


def in_venv() -> bool:
    return sys.prefix != sys.base_prefix


if __name__ == "__main__":
    print(f"MATRIX STATUS: {'Welcome to the construct' if in_venv() else
                            'You\'re still plugged in'}")

    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {
          os.path.basename(sys.prefix) if in_venv() else 'None detected'}")

    if in_venv():
        print(f"Environment Path: {sys.prefix}")
    else:
        print("\nWARNNIG: You're in the global environment!")
        print("The machines can see everything you install.")

    if in_venv():
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system")

        print("\nPackage installation path:")
        print(f"{site.getusersitepackages()}")
    else:
        print("\nTo enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("\nmatrix_env")
        print("Scripts")
        print("activate # On Windows")
