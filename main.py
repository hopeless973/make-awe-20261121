"""Relaxation entry for make.fun's 'Make the AI judge feel awe'.

Version 2, revised after the first entry's dev grade (69.6%, 7-4,
ranked #677): same tide, sharpened. The judge's brief rewards
calm rising from the text itself, in plain concrete words, a
steady rhythm, and an image that keeps growing after the last
line. Here the tide, a gull folding its wings, thin gold light
on the water, and a sea that keeps its rhythm long after the
lights go out in the houses along the shore.
Nothing in it instructs the reader; the calm is all in the image.
"""

import os

TEXT = """The tide comes in over warm sand and goes out again, unhurried. \
A gull folds its wings on a post while the light goes thin and gold \
across the water. The sea has kept this rhythm all day, all year, \
and will keep it long after the lights go out in the houses along \
the shore."""

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
