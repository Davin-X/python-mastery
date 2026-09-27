"""Reference answers for the 10 coding interview prompts."""

from collections import Counter, OrderedDict, deque
from collections.abc import Callable
from functools import wraps
from typing import TypeVar

Result = TypeVar("Result")


def first_unique_index(text: str) -> int:
    """Return the index of the first character that appears exactly once."""
    counts = Counter(text)
    return next((index for index, character in enumerate(text) if counts[character] == 1), -1)


def product_except_self(values: list[int]) -> list[int]:
    """Return each position's product of all other values without division."""
    products = [1] * len(values)
    prefix_product = 1
    for index, value in enumerate(values):
        products[index] = prefix_product
        prefix_product *= value

    suffix_product = 1
    for index in range(len(values) - 1, -1, -1):
        products[index] *= suffix_product
        suffix_product *= values[index]
    return products


def merge_intervals(
    intervals: list[tuple[int, int]],
) -> list[tuple[int, int]]:
    """Merge overlapping closed intervals without mutating the input."""
    if any(start > end for start, end in intervals):
        raise ValueError("interval starts must not exceed their ends")
    merged: list[list[int]] = []
    for start, end in sorted(intervals):
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return [(start, end) for start, end in merged]


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group case-sensitive anagrams, preserving input order within groups."""
    groups: dict[tuple[str, ...], list[str]] = {}
    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())


def minimum_window(source: str, target: str) -> str:
    """Return the earliest shortest substring containing target characters."""
    if not source or not target:
        return ""
    required = Counter(target)
    window: Counter[str] = Counter()
    formed = 0
    left = 0
    best_start = 0
    best_length = len(source) + 1

    for right, character in enumerate(source):
        window[character] += 1
        if character in required and window[character] == required[character]:
            formed += 1

        while formed == len(required):
            current_length = right - left + 1
            if current_length < best_length:
                best_start = left
                best_length = current_length
            left_character = source[left]
            window[left_character] -= 1
            if left_character in required and window[left_character] < required[left_character]:
                formed -= 1
            left += 1

    if best_length > len(source):
        return ""
    return source[best_start : best_start + best_length]


def flatten(items: list[object]) -> list[object]:
    """Flatten arbitrarily nested lists while treating other values as atomic."""
    flattened: list[object] = []
    pending = list(reversed(items))
    while pending:
        item = pending.pop()
        if isinstance(item, list):
            pending.extend(reversed(item))
        else:
            flattened.append(item)
    return flattened


class LRUCache:
    """A least-recently-used cache with average O(1) get and put operations."""

    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("capacity must be positive")
        self._capacity = capacity
        self._items: OrderedDict[object, object] = OrderedDict()

    def get(self, key: object) -> object | None:
        if key not in self._items:
            return None
        self._items.move_to_end(key)
        return self._items[key]

    def put(self, key: object, value: object) -> None:
        self._items[key] = value
        self._items.move_to_end(key)
        if len(self._items) > self._capacity:
            self._items.popitem(last=False)


def compare_versions(left: str, right: str) -> int:
    """Compare numeric dot-separated versions, ignoring trailing zeroes."""

    def parse(version: str) -> list[int]:
        components = version.split(".")
        if not version or any(not component.isdecimal() for component in components):
            raise ValueError("versions must contain non-negative integer components")
        values = [int(component) for component in components]
        while values and values[-1] == 0:
            values.pop()
        return values

    left_parts = parse(left)
    right_parts = parse(right)
    for index in range(max(len(left_parts), len(right_parts))):
        left_value = left_parts[index] if index < len(left_parts) else 0
        right_value = right_parts[index] if index < len(right_parts) else 0
        if left_value != right_value:
            return 1 if left_value > right_value else -1
    return 0


def memoize(function: Callable[..., Result]) -> Callable[..., Result]:
    """Cache results for calls with hashable positional and keyword arguments."""
    cache: dict[tuple[object, ...], Result] = {}

    @wraps(function)
    def wrapper(*args: object, **kwargs: object) -> Result:
        key = (*args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = function(*args, **kwargs)
        return cache[key]

    return wrapper


def allow_requests(timestamps: list[float], limit: int, window: float) -> list[bool]:
    """Allow requests under a sliding limit; only allowed requests consume slots."""
    if limit < 1 or window <= 0:
        raise ValueError("limit and window must be positive")
    if any(current <= previous for previous, current in zip(timestamps, timestamps[1:])):
        raise ValueError("timestamps must be strictly increasing")

    allowed: list[bool] = []
    accepted: deque[float] = deque()
    for timestamp in timestamps:
        window_start = timestamp - window
        while accepted and accepted[0] < window_start:
            accepted.popleft()
        if len(accepted) < limit:
            allowed.append(True)
            accepted.append(timestamp)
        else:
            allowed.append(False)
    return allowed


def _check() -> None:
    assert first_unique_index("swiss") == 1
    assert first_unique_index("aabb") == -1
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([0, 2, 0]) == [0, 0, 0]
    assert merge_intervals([(1, 3), (2, 5), (8, 9)]) == [(1, 5), (8, 9)]
    assert group_anagrams(["eat", "tea", "tan", "ate"]) == [
        ["eat", "tea", "ate"],
        ["tan"],
    ]
    assert minimum_window("ADOBECODEBANC", "ABC") == "BANC"
    assert minimum_window("abc", "z") == ""
    assert flatten([1, [2, [3]], "ab"]) == [1, 2, 3, "ab"]
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    cache.put("c", 3)
    assert cache.get("b") is None
    assert compare_versions("1.2", "1.2.0") == 0
    assert compare_versions("1.10", "1.2") == 1
    calls = 0

    @memoize
    def add(a: int, b: int) -> int:
        nonlocal calls
        calls += 1
        return a + b

    assert add(a=2, b=3) == add(b=3, a=2) == 5
    assert calls == 1
    assert allow_requests([0.0, 1.0, 2.0], limit=2, window=2.0) == [True, True, False]


if __name__ == "__main__":
    _check()
    print("OK")
