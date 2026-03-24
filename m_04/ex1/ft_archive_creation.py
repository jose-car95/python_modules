#!/usr/bin/env python3


def main() -> None:
    data: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    try:
        print("Initializing new storage unit: new_discovery.txt")
        with open('new_discovery.txt', 'w') as file:
            print("Storage unit created successfully...")
            print("Inscribing preservation data...")
            for entry in data:
                file.write(entry + '\n')
                print(entry)
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except OSError:
        print("ERROR: Could not write to the file...")


if __name__ == "__main__":
    main()
