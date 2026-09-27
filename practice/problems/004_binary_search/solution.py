"""Problem 004 — Binary Search reference solution. Run: python solution.py"""

from __future__ import annotations


def binary_search(numbers: list[int], target: int) -> int:
    """Return the leftmost target index in sorted numbers, or -1."""
    left = 0
    right = len(numbers)

    while left < right:
        middle = left + (right - left) // 2
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle

    if left < len(numbers) and numbers[left] == target:
        return left
    return -1


def _check() -> None:
    cases = [
        ([], 1, -1),
        ([5], 5, 0),
        ([1, 3, 5, 7], 1, 0),
        ([1, 3, 5, 7], 7, 3),
        ([1, 2, 2, 2, 4], 2, 1),
        ([1, 3, 5], 4, -1),
        ([1, 3, 5], 0, -1),
        ([1, 3, 5], 8, -1),
    ]
    for numbers, target, expected in cases:
        original = numbers.copy()
        actual = binary_search(numbers, target)
        assert actual == expected, f"{numbers!r}, {target}: got {actual}, expected {expected}"
        assert numbers == original, "input must not be modified"
    print("OK")


if __name__ == "__main__":
    _check()
