import os
import time
from datetime import datetime


def main() -> None:
    counter = 1

    print(
        f"log writer started, pid={os.getpid()}",
        flush=True,
    )

    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(
            f"{now} INFO pid={os.getpid()} "
            f"counter={counter} service=day004",
            flush=True,
        )

        counter += 1
        time.sleep(5)


if __name__ == "__main__":
    main()
