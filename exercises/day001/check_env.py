import sys
from pathlib import Path


def main() -> None:
    print("LLM App Roadmap Environment OK")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Current directory: {Path.cwd()}")


if __name__ == "__main__":
    main()
