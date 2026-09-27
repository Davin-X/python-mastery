# Problem 004 — Binary Search

Given a sorted list of integers, return the index of the target's first
occurrence, or `-1` when it is absent.

## Requirements

```python
binary_search(numbers: list[int], target: int) -> int
```

- `numbers` is sorted in non-decreasing order and may contain duplicates.
- Return the leftmost matching index.
- Do not modify the input.
- Aim for O(log n) time and O(1) extra space.

## Examples

```python
binary_search([1, 3, 5, 7], 5)       # 2
binary_search([1, 2, 2, 2, 4], 2)    # 1
binary_search([1, 3, 5], 4)          # -1
binary_search([], 1)                 # -1
```

## Acceptance criteria

- `python starter.py` prints `OK` after implementation.
- Tests cover duplicates, empty input, and targets outside the list's range.
- The solution uses a binary-search loop rather than scanning the list.

## Hint

Use a half-open interval `[left, right)`. When a middle value is at least the
target, keep searching the left half; this finds the first occurrence.