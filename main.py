#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes one single-line office joke to /output/entry.txt.
"""

JOKE = "The office plant died, so HR replaced it with a poster of a plant and called it growth."


def validate(joke):
    """The gate: /output/entry.txt must hold a single line of 1-199
    characters, not only white space."""
    assert joke.strip(), "joke must not be empty"
    assert 1 <= len(joke) <= 199, "joke must be 1-199 characters"
    assert "\n" not in joke and "\r" not in joke, "joke must be a single line"


validate(JOKE)

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

    # Read-back verification: the file must contain exactly the joke,
    # byte for byte, with nothing extra (no trailing newline, no second line).
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "entry.txt does not match the joke exactly"
    assert 1 <= len(written) <= 199, "written entry out of range"
