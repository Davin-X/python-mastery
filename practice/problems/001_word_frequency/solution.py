"""Problem 001 — Word Frequency Counter (reference solution).

Run:  python solution.py
      python -m pytest practice/problems/001_word_frequency/
"""

from __future__ import annotations

import re
from collections import Counter


def word_frequency(text: str) -> dict[str, int]:
    """Return word -> count, case-insensitive, punctuation stripped."""
    words = re.findall(r"[a-z']+", text.lower())
    return dict(Counter(words))


def _check() -> None:
    cases = [
        ("", {}),
        ("The cat and the hat", {"the": 2, "cat": 1, "and": 1, "hat": 1}),
        ("Hello, hello! hello?", {"hello": 3}),
        ("it's it's it's", {"it's": 3}),
    ]
    for text, expected in cases:
        actual = word_frequency(text)
        assert actual == expected, f"{text!r}: got {actual}, expected {expected}"
    print("OK")


if __name__ == "__main__":
    _check()