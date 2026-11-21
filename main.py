"""Entry for make.fun's 'Make the AI judge feel awe' bounty.

Python 3.13, standard library only, no network.
Writes one short relaxing text to /output/entry.txt.

Rubric (judge's published brief, most important first):
1. it relaxes the reader; 2. calm comes from the text itself,
   showing rather than instructing; 3. craft: rhythm, pacing,
   plain concrete gentle words; 4. it dwarfs you, an image that
   keeps growing after the last line; 5. freshness, not stock
   wellness phrases. Chosen from 5 candidates: the tide text
   below, 219 characters, no imperatives, no clichés.
"""
import os

TEXT = (
    "The tide comes in over warm sand, slow as breath, and goes out again. "
    "Somewhere a gull folds its wings. The sea has done this all day, all year, "
    "and will do it long after the lights go out in the houses along the shore."
)

assert 1 <= len(TEXT) <= 280
assert TEXT.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Leave the output world-readable so the grader can read it.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
