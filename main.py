"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt. Deterministic:
the same bytes on every run. Standard library only.
"""

import os
import sys

JOKE = "I started a band called The Leftovers, but we broke up \u2014 every rehearsal turned into a reheating."

# The gate allows 1 to 200 characters; this joke is 97 characters.
JOKE_LENGTH = len(JOKE)
assert 1 <= JOKE_LENGTH <= 200

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_output_dir() -> None:
    """Remove every child of /output, never /output itself."""
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for filename in files:
                    os.remove(os.path.join(root, filename))
                for dirname in dirs:
                    os.rmdir(os.path.join(root, dirname))
            os.rmdir(path)
        else:
            os.remove(path)


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_output_dir()
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
