"""Problem 002 — Two Sum. Implement the function, then run: python starter.py"""

from __future__ import annotations


def two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Return indices of two distinct values that sum to target, if present."""
    raise NotImplementedError("implement me")


def _check() -> None:
    cases = [
        ([2, 7, 11, 15], 9, True),
        ([3, 3], 6, True),
        ([1, 2, 3], 7, False),
        ([], 0, False),
        ([4], 8, False),
    ]
    for numbers, target, has_pair in cases:
        original = numbers.copy()
        result = two_sum(numbers, target)
        if has_pair:
            assert result is not None, f"expected a pair for {numbers!r}"
            first, second = result
            assert first != second, f"indices must differ: {result!r}"
            assert numbers[first] + numbers[second] == target
        else:
            assert result is None, f"expected no pair, got {result!r}"
        assert numbers == original, "input must not be modified"
    print("OK")


if __name__ == "__main__":
    _check()
