"""Problem 003 — Valid Parentheses reference solution. Run: python solution.py"""

from __future__ import annotations


def is_valid_parentheses(text: str) -> bool:
    """Return whether all supported brackets are correctly balanced."""
    opening_to_closing = {"(": ")", "[": "]", "{": "}"}
    closing_brackets = set(opening_to_closing.values())
    stack: list[str] = []

    for character in text:
        if character in opening_to_closing:
            stack.append(character)
        elif character in closing_brackets:
            if not stack or opening_to_closing[stack.pop()] != character:
                return False
        else:
            return False

    return not stack


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
