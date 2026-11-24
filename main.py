#!/usr/bin/env python3
"""How many tabs do you have open? Three.

The honest count: three tabs. One for the work, one for the
reference, one I keep meaning to close. The field will brag about
hundreds; three is the surprising number — far lower than anyone
guesses, and the only count a person who finishes things has open.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
TAB_COUNT = "3"


def write_entry(path, text):
    """Write text to path with no trailing newline, atomically."""
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp_path, path)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    write_entry(OUTPUT_FILE, TAB_COUNT)
    # Self-check: the gate wants 1-5 chars, digits only, not blank.
    with open(OUTPUT_FILE, encoding="utf-8") as f:
        written = f.read()
    assert written.isdigit() and 1 <= len(written) <= 5, written


if __name__ == "__main__":
    main()
