# Data Structures Quick Reference

Companion to `notebooks/fundamentals/02_data_structures.ipynb`.

## The big four

| Type | Ordered | Mutable | Duplicates | Used for |
|------|---------|---------|------------|----------|
| `list` | ✅ | ✅ | ✅ | sequences, stacks, queues |
| `tuple` | ✅ | ❌ | ✅ | fixed records, dict keys |
| `dict` | ✅ (3.7+) | ✅ | keys unique | key → value lookups |
| `set` | ❌ | ✅ | ❌ | membership, de-duplication, set math |

## Lists

```python
xs = [3, 1, 2]
xs.append(4)            # insert at end
xs.insert(0, 0)         # insert at index
xs.extend([5, 6])       # merge
x = xs.pop()            # remove + return last; pop(0) for first
xs.remove(1)            # remove by value
xs.sort() / sorted(xs)  # in-place / new list
xs[::-1]  xs[1:3]  xs[::2]      # reverse / slice / stride
len(xs)  xs.count(1)  xs.index(3)  any(...)  all(...)
```

## Tuples

```python
point = (3, 4)
x, y = point                    # unpacking
lat, lon = (12.9, 77.6)
```

## Dictionaries

```python
d = {"a": 1}
d["b"] = 2
d.get("c", 0)                   # 0 (no KeyError)
d.setdefault("d", 4)            # write only if absent
d.update({"e": 5})
for k, v in d.items(): ...
{k: v for k, v in d.items() if v > 1}
d.pop("a", None)  del d["b"]
```

## Sets

```python
a, b = {1, 2, 3}, {3, 4}
a | b            # union
a & b            # intersection
a - b            # difference
a ^ b            # symmetric difference
{1, 2} <= {1, 2, 3}   # subset
```

## The `collections` module

```python
from collections import Counter, defaultdict, deque, namedtuple

Counter("aabbc")                    # {'a':2, 'b':2, 'c':1}
c.most_common(1)                    # [('a', 2)]

defaultdict(list)["missing"]        # returns [] instead of KeyError

dq = deque([1, 2, 3])               # O(1) append/popleft on both ends
dq.appendleft(0)  dq.pop()

Point = namedtuple("Point", ["x", "y"])   # tuple with field names
```

## Common time complexities

| Operation | Cost |
|-----------|------|
| list index / append / pop | O(1) |
| list `in` (search) | O(n) |
| sort / sorted | O(n log n) |
| dict / set get, set, in | O(1) average |
| deque popleft/appendleft | O(1) |

## Resources

- [Official tutorial — data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Time complexity wiki (Python)](https://wiki.python.org/moin/TimeComplexity)