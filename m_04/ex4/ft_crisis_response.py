#!/usr/bin/env python3


def crisis_handler(filename: str, restricted: bool = False) -> None:
    if restricted:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
    elif filename == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        if restricted:
            raise PermissionError("Restricted vault access")

        with open(filename, "r") as archive_file:
            content: str = archive_file.read().strip()

        print(f"SUCCESS: Archive recovered - ``{content}''")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stabilized")

    print()


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt", restricted=True)
    crisis_handler("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
