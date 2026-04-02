def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    print("Initializing new storage unit: new_discovery.txt")
    with open("new_discovery.txt", "w") as file:
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        entries: tuple[str, ...] = (
            "[ENTRY 001] New quantum algorithm discovered",
            "[ENTRY 002] Efficiency increased by 347%",
            "[ENTRY 003] Archived by Data Archivist trainee"
        )
        for entry in entries:
            file.write(entry + "\n")
            print(entry)
    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
