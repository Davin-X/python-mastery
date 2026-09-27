# Problem 003 — Valid Parentheses

Given a string containing brackets, decide whether every opening bracket is
closed by the correct type and in the correct order.

## Requirements

```python
is_valid_parentheses(text: str) -> bool
```

- Supported characters are `(`, `)`, `[`, `]`, `{`, and `}`.
- Every closing bracket must match the most recent unmatched opening bracket.
- Return `False` for any character outside the supported bracket set.
- The empty string is valid.

## Examples

```python
is_valid_parentheses("()[]{}")  # True
is_valid_parentheses("{[()]}")  # True
is_valid_parentheses("(]")      # False
is_valid_parentheses("([)]")    # False
is_valid_parentheses("")        # True
```

## Constraints

- `0 <= len(text) <= 100_000`
- Aim for O(n) time and O(n) extra space.

## Acceptance criteria

- `python starter.py` prints `OK` after implementation.
- Tests cover mismatched order, unclosed brackets, and unsupported characters.

## Hint

Keep unmatched opening brackets in a stack. A closing bracket must match the
top of that stack.