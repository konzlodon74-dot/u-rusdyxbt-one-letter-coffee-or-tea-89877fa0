#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

Why coffee: coffee is the louder drink. It wakes you up, it bites back,
it turns a sleepy morning into a decision. Tea soothes; coffee declares.
"A" is also the first letter and the top mark -- the boldest possible
single-character answer to the coffee-versus-tea argument.
"""

import os

LETTER = "A"  # A = coffee, B = tea


def main() -> None:
    # The gate: exactly one character, non-whitespace, the letter we chose.
    assert len(LETTER) == 1, "entry must be exactly one character"
    assert not LETTER.isspace(), "entry must not be whitespace"
    assert LETTER in ("A", "B"), "entry must be A (coffee) or B (tea)"

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)

    # Read it back and enforce the gate on what actually landed on disk:
    # exactly one UTF-8 character, the letter we chose, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LETTER, f"entry.txt holds {written!r}, expected {LETTER!r}"
    assert len(written.encode("utf-8")) == 1, "entry must be one byte"


if __name__ == "__main__":
    main()
