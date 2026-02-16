if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("\nAccessing Storage Vault: ancient_fragment.txt")
    try:
        with open("ancient_fragment.txt") as archive:
            print("Connection established...")

            print("\nRECOVERED DATA:")
            print(archive.read())
            print("\nData Recovery Complete. Storage Unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
