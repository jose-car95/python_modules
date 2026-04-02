import sys


def print_stdout(text: str) -> None:
    sys.stdout.write(text)
    sys.stdout.flush()


def print_stderr(text: str) -> None:
    sys.stderr.write(text)


def read_stdin() -> str:
    return sys.stdin.readline()[:-1]


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    print_stdout("Input Stream active. Enter archivist ID: ")
    archivist_id: str = read_stdin()
    print_stdout("Input Stream active. Enter status report: ")
    status_report: str = read_stdin()
    print_stdout(
        f"\n[STANDARD] Archive status from {archivist_id}: {status_report}\n"
    )
    print_stderr(
        "[ALERT] System diagnostic: Communication channels verified\n"
    )
    print_stdout("[STANDARD] Data transmission complete\n")
    print_stdout("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
