def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")

        with open("ancient_fragment.txt", "r") as file:
            print("Connection established..")
            data: str = file.read()

        print("\nRECOVERED DATA:")
        print(data)

        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
