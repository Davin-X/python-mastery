"""Problem 003 — Valid Parentheses. Implement, then run: python starter.py"""

from __future__ import annotations


def is_valid_parentheses(text: str) -> bool:
    """Return whether all supported brackets are correctly balanced."""
    raise NotImplementedError("implement me")


def _check() -> None:
    cases = [
        ("", True),
        ("()[]{}", True),
        ("{[()]}", True),
        ("(]", False),
        ("([)]", False),
        ("((", False),
        (")", False),
        ("(a)", False),
    ]
    for text, expected in cases:
        actual = is_valid_parentheses(text)
        assert actual is expected, f"{text!r}: got {actual}, expected {expected}"
    print("OK")


if __name__ == "__main__":
    _check()
