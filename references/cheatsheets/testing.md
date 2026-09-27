# Testing Quick Reference

Companion to `notebooks/2-intermediate/08_testing.ipynb`. Prefer tests that
describe observable behavior and cover boundary cases, not implementation details.

## Run tests

```bash
python -m pytest
python -m pytest -q
python -m pytest -k "parser"
python -m pytest --cov=your_package --cov-report=term-missing
```

Install the development tools with `pip install -r requirements-dev.txt`.

## Test a function

```python
import pytest


def divide(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ValueError("denominator must not be zero")
    return numerator / denominator


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [(8, 2, 4), (3, 2, 1.5), (0, 4, 0)],
)
def test_divide(numerator: float, denominator: float, expected: float) -> None:
    assert divide(numerator, denominator) == expected


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="denominator"):
        divide(1, 0)
```

## Fixtures

Use a fixture when setup is shared or needs cleanup:

```python
from pathlib import Path

import pytest


@pytest.fixture
def sample_file(tmp_path: Path) -> Path:
    path = tmp_path / "input.txt"
    path.write_text("hello\n", encoding="utf-8")
    return path
```

`tmp_path` is a built-in fixture. Each test gets its own temporary directory.

## Doubles and isolation

- Use `monkeypatch` to replace an environment variable, attribute, or dependency
  at the point the code under test looks it up.
- Use `unittest.mock` when call assertions or a configurable fake are useful.
- Prefer a small fake object when it makes expected behavior clearer than a mock.
- Don't mock the function being tested or stable standard-library behavior.

## A practical checklist

- Normal case and return value.
- Empty and boundary inputs.
- Invalid input and expected exceptions.
- Side effects: files, network calls, or state changes.
- Regression case for each bug fixed.

Coverage shows which lines ran; it does not prove that assertions are meaningful
or that every important behavior is correct.