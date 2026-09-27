# Decorators & Closures

> **Status:** reading-only companion. There is no dedicated notebook for this
> topic; the concepts appear in `09_metaclasses`, `11_design_patterns`, and
> `12_performance_optimization`. This guide consolidates them into one place.

## Why this matters

Decorators modify the behavior of functions or classes without changing their
source. They are the foundation of Flask/FastAPI routing, `pytest` fixtures,
`functools.lru_cache`, and property/staticmethod in your own classes.

## 1. Closures — the mechanism behind decorators

A function that "remembers" variables from the enclosing scope after that scope
has finished executing:

```python
def make_multiplier(factor: float):
    def multiply(x: float) -> float:
        return x * factor          # `factor` is captured
    return multiply

double = make_multiplier(2)
print(double(5))                   # 10
```

## 2. A simple function decorator

```python
import functools
import time
from typing import Any, Callable

def timer(func: Callable) -> Callable:
    @functools.wraps(func)                # preserves name + docstring
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.2f}s")
        return result
    return wrapper

@timer
def slow() -> str:
    time.sleep(0.5)
    return "done"
```

Always use `functools.wraps` — without it the decorated function loses its
`__name__`, `__doc__`, and signature, which breaks introspection and tooling.

## 3. Decorators with parameters

The outer layer receives parameters, the middle layer receives the function:

```python
def retry(max_attempts: int = 3, delay: float = 0.5):
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator
```

## 4. Class decorators

Any class with `__call__` can act as a decorator:

```python
class CountCalls:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.count += 1
        return self.func(*args, **kwargs)

@CountCalls
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## 5. `functools` essentials

- `wraps` / `update_wrapper` — preserve metadata on the wrapper.
- `lru_cache(maxsize=...)` — memoization for expensive pure functions.
- `partial` — pre-fill arguments:

  ```python
  from functools import partial

  def multiply(x: float, y: float) -> float: return x * y
  double = partial(multiply, 2)
  print(double(5))          # 10
  ```

## Common pitfalls

- **Forgetting `@functools.wraps`** — breaks `help()`, pickling, and debugging.
- **Mutating captured state without `nonlocal`** — reads are fine; writes need `nonlocal`.
- **Decorator order matters** — the closest `@` to the function runs first:
  ```python
  @timer
  @retry()
  def f(): ...
  ```
- **`lru_cache` on functions with mutable args** — raises `TypeError`.

## Further reading

- [`functools` — official docs](https://docs.python.org/3/library/functools.html)
- Primer on closures: [Python Execution Model](https://docs.python.org/3/reference/executionmodel.html)