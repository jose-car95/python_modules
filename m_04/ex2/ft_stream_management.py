#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n\n")

    print("Input Stream active. Enter archivist ID: ")
    archivist_id: str = sys.stdin.readline()[:-1]

    print("Input Stream active. Enter status report: ")
    status_report: str = sys.stdin.readline()[:-1]

    sys.stdout.write(
        f"\n[STANDARD] Archive status from {archivist_id}: {status_report}\n"
    )
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
    )
    sys.stdout.write(
        "[STANDARD] Data transmission complete\n"
    )
    sys.stdout.write("\nThree-channel communication test successful.\n")


if __name__ == "__main__":
    main()
