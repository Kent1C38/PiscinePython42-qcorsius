if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    print("\nInitializing new sotrage unit: new_discovery.txt ...")
    with open("new_discovery.txt", "w") as archive:
        print("Storage unit created successfully")

        print("\nInscribing preservation data...")

        data = """[ENTRY 001] New quantum algorythm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainee"""
        archive.write(data)
        print(data)

        print("\nData inscription complete. Storage unit sealed.")

    print("Archive 'new_discovery.txt' ready for long-term preservation.")
