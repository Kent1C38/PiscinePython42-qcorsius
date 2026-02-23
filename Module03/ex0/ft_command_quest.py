import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments recieved: {len(sys.argv) - 1}")
        counter = 1
        for arg in sys.argv:
            if arg == sys.argv[0]:
                pass
            else:
                print(f"Argument {counter}: {arg}")
                counter += 1
    print(f"Total arguments: {len(sys.argv)}")
