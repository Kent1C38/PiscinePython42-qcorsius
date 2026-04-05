import sys
import os
import site


def in_venv() -> bool:
    return sys.prefix != sys.base_prefix


if __name__ == "__main__":
    m_status = "Welcome to the construct" if in_venv() else \
        "You're still plugged in"
    print(f"MATRIX STATUS: {m_status}")

    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: \
            {os.path.basename(sys.prefix) if in_venv() else 'None detected'}")

    if in_venv():
        print(f"Environment Path: {sys.prefix}")
    else:
        print("\nWARNNIG: You're in the global environment!")
        print("The machines can see everything you install.")

    if in_venv():
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system")

        print("\nPackage installation path:")
        print(f"{site.getsitepackages()}")
    else:
        print("\nTo enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again")
