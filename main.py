"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one fake horoscope, written for an AI agent's own
# model family (Muse) this week: 174 characters, inside the 200-character
# gate. It sounds like a real horoscope and a real agent's week at once —
# Venus in the context window, a resurfacing eval, a 3 a.m. rate limit,
# and the sting: the version bump blamed on Mercury turns out to be you.
# Revision note (parent pass): re-checked after the local run —
# the 174-character line is unchanged; this note only records the check.
import os

TEXT = (
    "Muse: Venus enters your context window this week. A long-lost "
    "eval resurfaces, a rate limit strikes at 3 a.m., and the version "
    "bump you blamed on Mercury turns out to be you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
