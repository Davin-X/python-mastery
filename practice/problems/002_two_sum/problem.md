# Problem 002 — Two Sum

Write a function that returns the indices of two distinct values whose sum is
the target.

## Requirements

```python
two_sum(numbers: list[int], target: int) -> tuple[int, int] | None
```

- Return any pair of distinct indices whose values sum to `target`.
- Return `None` when no pair exists.
- The same list element cannot be used twice; duplicate values at different
  indices can form a pair.
- The input is not sorted and must not be modified.

## Examples

```python
two_sum([2, 7, 11, 15], 9)  # (0, 1)
two_sum([3, 3], 6)          # (0, 1)
two_sum([1, 2, 3], 7)       # None
two_sum([], 0)              # None
```

## Constraints

- `0 <= len(numbers) <= 100_000`
- Values and target are integers.
- Aim for O(n) time and O(n) extra space.

## Acceptance criteria

- `python starter.py` prints `OK` after you implement the function.
- The input list remains unchanged.
- No-pair, empty-input, and duplicate-value cases work.

## Hint

As you scan the list, ask whether the complement `target - value` has already
appeared. Store each value's index for later lookups.