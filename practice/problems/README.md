# Problems

Small, standalone practice problems (question + starter code + solution) that
reinforce the notebook curriculum. Modeled on coding-practice platforms, but
runnable locally with zero dependencies.

```
problems/
├── 001_word_frequency/
│   ├── problem.md    # prompt, examples, acceptance criteria
│   ├── starter.py    # signature + failing tests — implement this
│   └── solution.py   # reference solution + passing tests
├── 002_two_sum/
│   └── ...            # same three-file format
├── 003_valid_parentheses/
│   └── ...
├── 004_binary_search/
│   └── ...
└── ...
```

## How to practice

1. Open `problem.md`, implement in `starter.py`.
2. Verify: run `python starter.py` (it should print `OK` once implemented).
3. Compare with `solution.py` **after** you finish.

## Contributing

Add `NNN_short_name/` with the three files above; keep the solution in the same
style (stdlib, typed, simple). Update this index.

| # | Problem | Concepts | Done |
|---|---------|----------|------|
| 001 | Word frequency counter | dict, `collections.Counter`, regex | |
| 002 | Two Sum | dictionary lookup, complement, edge cases | |
| 003 | Valid Parentheses | strings, stack, invariants | |
| 004 | Binary Search | sorted input, boundaries, loop invariants | |