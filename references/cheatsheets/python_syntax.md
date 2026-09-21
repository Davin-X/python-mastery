# Python Syntax Quick Reference

Companion to `notebooks/fundamentals/01_python_basics.ipynb`.

## Variables, types, operators

```python
name = "Alice"          # str
age = 25                # int
height = 5.7            # float
employed = True         # bool
nothing = None          # NoneType

print(f"Hello {name}, {age + 5} years next birthday")
print(type(height))     # <class 'float'>
```

Key operators: `+ - * / // % **`, comparisons `== != < > <= >=`,
logical `and or not`, membership `in`.

## Strings

```python
s = "hello"
s.upper()               # "HELLO"
s.split("e")            # ['h', '', 'llo']
"|".join(["a", "b"])    # "a|b"
s.strip()  s.startswith("h")  s.replace("l", "L")
f"{s!r}"                # repr; f"{value:,.2f}" formats numbers
```

## Control flow

```python
for i, item in enumerate(items):
    if item is None:
        continue
    elif item < 0:
        pass             # placeholder
    else:
        break

while (n := read()) > 0:   # walrus operator, Python 3.8+
    process(n)

match command:             # structural pattern matching, Python 3.10+
    case "start":
        start()
    case _:
        raise ValueError(command)
```

## Functions

```python
def greet(name: str, *, formal: bool = False) -> str:
    """Docstring: what the function does."""
    return f"Good day, {name}" if formal else f"Hi {name}"

greet("Alice")                 # positional
greet("Bob", formal=True)      # keyword-only after *
lambda x, y: x + y             # anonymous
```

## Comprehensions

```python
squares = [x * x for x in range(10)]
even = [x * x for x in range(10) if x % 2 == 0]
words = {w: len(w) for w in "go big".split()}
chars = {c for c in "abracadabra"}          # set
gen = (x * x for x in range(10))            # generator
```

## Errors

```python
try:
    risky()
except ValueError as exc:
    log(exc)
except (KeyError, IndexError):
    pass
else:
    print("no error")
finally:
    cleanup()
```

## Classes in one screen

```python
class Account:
    kind = "bank"                       # class attribute

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner              # instance attribute
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    @classmethod
    def empty(cls, owner: str) -> "Account":
        return cls(owner)

    @staticmethod
    def currency() -> str:
        return "USD"
```

## Env & files

```bash
python -m venv .venv && source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
jupyter lab
```

```python
from pathlib import Path
Path("data").mkdir(exist_ok=True)
Path("data/out.txt").write_text("hi", encoding="utf-8")
print(Path("data/out.txt").read_text(encoding="utf-8"))
```

## Resources

- [Official tutorial](https://docs.python.org/3/tutorial/)
- [Official datastructures reference](https://docs.python.org/3/tutorial/datastructures.html)