"""Problem 001 — Word Frequency Counter (starter).

Implement `word_frequency` below, then run: python starter.py
"""

from __future__ import annotations


def word_frequency(text: str) -> dict[str, int]:
    """Return word -> count, case-insensitive, punctuation stripped."""
    raise NotImplementedError("implement me")


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
