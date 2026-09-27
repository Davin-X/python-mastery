# Algorithms Quick Reference

Companion to the data-structures notebooks and interview practice. These are
starting points; choose a pattern from the input constraints, then verify it
with edge cases.

## Complexity at a glance

| Complexity | Typical example |
|------------|-----------------|
| $O(1)$ | list indexing, average dictionary lookup |
| $O(\log n)$ | binary search in sorted data |
| $O(n)$ | one pass over a sequence |
| $O(n \log n)$ | comparison sorting |
| $O(n^2)$ | comparing every pair with nested loops |
| $O(2^n)$ | enumerating all subsets |

State both time and extra-space complexity. For hash tables, $O(1)$ lookup is
an average-case expectation, not a worst-case guarantee.

## Choose a pattern

| Signal in the problem | Consider |
|-----------------------|----------|
| Fast lookup by previously seen value | Dictionary or set |
| Sorted input, pair or boundary search | Two pointers or binary search |
| Contiguous range with a condition | Sliding window or prefix sums |
| Matching nested delimiters / next greater item | Stack |
| Repeated smallest/largest selection | Heap |
| Tree/graph reachability | DFS or BFS with a visited set |
| Repeated subproblems with optimal substructure | Dynamic programming |

## Common templates

### Frequency counting

```python
from collections import Counter

counts = Counter("mississippi")
most_common = counts.most_common(2)
```

### Two pointers on sorted input

```python
def has_pair_with_sum(numbers: list[int], target: int) -> bool:
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return True
        if total < target:
            left += 1
        else:
            right -= 1

    return False
```

This assumes `numbers` is sorted. It runs in $O(n)$ time and uses $O(1)$ extra
space.

### Binary search

```python
def binary_search(numbers: list[int], target: int) -> int:
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = left + (right - left) // 2
        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
```

The input must be sorted. This version returns any matching index, or `-1` if
the target is absent.

## Before you code

1. Clarify input shape, ordering, duplicates, and expected behavior for empty input.
2. Work a small example by hand and name the invariant your loop maintains.
3. Start with the simplest correct approach; optimize against stated constraints.
4. Test empty, one-item, duplicate, boundary, and not-found cases as relevant.
5. Explain time and extra space separately.

See [practice problems](../../practice/problems/) for prompts with starter code
and solutions.