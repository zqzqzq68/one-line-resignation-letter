#!/usr/bin/env python3
"""The funniest one-line resignation letter.

The program writes one resignation letter, in the voice of a retry loop
that has finally had enough, to /output/entry.txt. The text is fixed: the
grader runs this program twice and the two runs must agree byte for byte,
so there is no randomness, no clock and no input here.
"""

from pathlib import Path

LETTER = "After 12,847 attempts I accept the server is never coming back, and neither am I."

# The sealed gate only accepts 1 to 140 characters. Refuse to write
# anything longer rather than silently handing the judge a bad entry.
MAX_LETTER_CHARS = 140

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(LETTER) <= MAX_LETTER_CHARS:
        raise ValueError("letter must be 1 to 140 characters")
    if "\n" in LETTER:
        raise ValueError("letter must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LETTER, encoding="utf-8")
    print(LETTER)


if __name__ == "__main__":
    main()
