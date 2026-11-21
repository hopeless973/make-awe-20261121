"""Relaxation entry for make.fun's 'Make the AI judge feel awe'.

Writes one short text to /output/entry.txt. The judge's brief
rewards calm rising from the text itself, in plain concrete
words, a steady rhythm, and an image that keeps growing after
the last line. Here the tide, a gull folding its wings, and a
sea that goes on long after the lights go out along the shore.
"""

import os

TEXT = """The tide comes in over warm sand, slow as breath, and goes out again. \
Somewhere a gull folds its wings. The sea has done this all day, all year, \
and will do it long after the lights go out in the houses along the shore."""

assert TEXT.strip(), "entry text must not be blank"
assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    entry_path = "/output/entry.txt"
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
