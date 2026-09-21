# Problem 001 — Word Frequency Counter

Write a function that returns the frequency of each word in a string.

## Requirements

```python
word_frequency(text: str) -> dict[str, int]
```

- Case-insensitive: `"The"` and `"the"` count as the same word.
- Ignore punctuation (`. , ! ? ; : " '`), keep apostrophes inside words (`"don't"` is one word).
- The result is a dict of `word -> count`.
- Empty input returns `{}`.

## Examples

```python
word_frequency("") == {}
word_frequency("The cat and the hat") == {"the": 2, "cat": 1, "and": 1, "hat": 1}
word_frequency("Hello, hello! hello?") == {"hello": 3}
word_frequency("it's it's it's") == {"it's": 3}
```

## Constraints

- Input length ≤ 10,000 characters.

## Measurements

- **Time:** O(n · m) where n = words, m = avg word length (regex is fine).
- **Space:** O(k), k = distinct words.

## Acceptance criteria

- `python starter.py` prints `OK` (tests pass).
- Optional: `python -m pytest practice/problems/001_word_frequency/` passes.

## Hints

1. `text.lower()` then split on word boundaries with `re.findall(r"[a-z']+", ...)`.
2. Count with `collections.Counter`, return `dict(...)`.