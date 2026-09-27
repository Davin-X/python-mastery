# 🐍 Python Mastery — 14-Week Learning Path

A sequential path from Python fundamentals to a complete machine-learning
project. Work the **notebook** for each week, then build the weekly
**deliverable**. Budget ~8-10 h/week; the whole path is **~108-137 hours**.

## Structure

| Phase | Weeks | Focus | Notebooks |
|-------|-------|-------|-----------|
| 1 · Foundations | 1-4 | syntax, data structures, control flow, OOP | `01`-`04` |
| 2 · Intermediate | 5-8 | files, packages, errors, testing | `05`-`08` |
| 3 · Advanced | 9-12 | metaprogramming, async, patterns, performance | `09`-`12` |
| 4 · Data Science | 13-14 | pandas/NumPy → ML & statistics | `14`-`18` |
| Extras | — | interview prep, cheatsheets, guides | `references/` + `practice/` |

> Notebook index with time/prereqs per file: [`README.md`](README.md).
> One-page references: `references/cheatsheets/`. Hands-on practice:
> `practice/problems/`.

## How to use this guide

1. **Setup** — follow the Quick Start in [`README.md`](README.md).
2. **Each week** — open the notebook, read the theory cells, and *run* every
   code cell. Re-implement the examples from memory before reading the next
   section.
3. **Deliverable** — build the week's project **yourself**, using the spec in
   [`practice/projects/README.md`](practice/projects/README.md). This
   repository ships theory (`notebooks/`), references (`references/`), sample
   data (`practice/data/`), and practice problems (`practice/problems/`) — the
   weekly deliverables are *assignments for you*, not files you will find here.
4. **Assessment** — finish each week with the quiz/challenge listed below.

## Curriculum at a glance

| Wk | Focus | Notebook | Hours | Deliverable |
|----|-------|----------|-------|-------------|
| 1 | Python Basics | `01_python_basics` | 8-10 | Calculator CLI |
| 2 | Data Structures | `02_data_structures` | 8-10 | Inventory Manager |
| 3 | Control Flow & Functions | `03_control_flow` | 8-10 | Text Adventure Game |
| 4 | OOP Fundamentals | `04_oop_fundamentals` | 8-10 | Banking System |
| 5 | File I/O & Modules | `05_file_handling` | 6-8 | Log Analyzer |
| 6 | Packages & Virtual Env | `06_modules_packages` | 6-8 | Publishable Package |
| 7 | Error Handling & Logging | `07_error_handling` | 6-8 | Resilient Data Pipeline |
| 8 | Testing (pytest/TDD) | `08_testing` | 8-10 | 90% Coverage Suite |
| 9 | Metaclasses & Descriptors | `09_metaclasses` | 6-8 | Mini ORM/Validator |
| 10 | Async Programming | `10_async_programming` | 8-10 | Async Web Scraper |
| 11 | Design Patterns | `11_design_patterns` | 8-10 | Plugin Architecture |
| 12 | Performance Optimization | `12_performance_optimization` | 6-8 | 10x Speedup Report |
| 13 | Data Analysis (Pandas/NumPy) | `14_…`, `15_…` | 10-12 | EDA Dashboard |
| 14 | ML & Statistics | `16_…`, `17_…`, `18_…` | 12-15 | End-to-End ML Project |

## Prerequisites

- Python 3.10+ (ideally 3.12, see `.python-version`)
- A terminal + either `jupyter lab` or VS Code with the Jupyter extension
- Comfort opening/running a Jupyter notebook

---

## 🏗️ Phase 1: Python Foundations (Weeks 1-4)

### Week 1 — Python Basics

**Notebook:** `notebooks/1-fundamentals/01_python_basics.ipynb` · **8-10 h**

**Theory**
- Running Python: REPL, scripts, Jupyter
- Variables, built-in types (`int`, `float`, `str`, `bool`, `None`)
- Operators, type conversion, `f`-strings and formatting
- Comments, docstrings, `print`, basic input

**Practice (in the notebook)**
- Run every cell; predict outputs before executing.
- Write your own variants of each example.

**Tools:** Python 3.10+, Jupyter, a code editor (VS Code recommended)

**Deliverable — Calculator CLI**
A terminal calculator supporting `+ - * / **`, input validation, and a loop
until the user quits. Test with edge cases (divide by zero, non-numeric input).

**Assessment**
- Quiz: data types, operator precedence, string formatting
- Challenge: a unit converter (km↔mi, °C↔°F)

### Week 2 — Data Structures

**Notebook:** `notebooks/1-fundamentals/02_data_structures.ipynb` · **8-10 h**

**Theory**
- `list`, `tuple`, `dict`, `set`: construction, indexing, slicing, methods
- Mutability vs. immutability and why it matters
- List/dict/set comprehensions and generator expressions
- `collections`: `Counter`, `defaultdict`, `namedtuple`, `deque`

**Tools:** standard library (see `references/cheatsheets/data_structures.md`)

**Deliverable — Inventory Manager**
Track a shop inventory: add/remove items, update quantity, list fast-movers,
find items below a reorder threshold. Use a `dict` keyed by SKU; persisting to
file will come in week 5.

**Assessment**
- Quiz: time complexity of common list/dict/set operations
- Challenge: a word-frequency counter (see `practice/problems/001_word_frequency`)

### Week 3 — Control Flow & Functions

**Notebook:** `notebooks/1-fundamentals/03_control_flow.ipynb` · **8-10 h**

**Theory**
- `if`/`elif`/`else`, truthiness, short-circuiting
- `for` / `while`, `break`, `continue`, `pass`, `enumerate`, `zip`
- Functions: parameters, defaults, `*args`/`**kwargs`, `lambda`
- Comprehensions with conditions + nested grouping

**Tools:** `typing` for annotations (see `references/cheatsheets/python_syntax.md`)

**Deliverable — Text Adventure Game**
A small branching story game: player state, choices, win/lose conditions,
rooms as dicts/functions. Replayable loop.

**Assessment**
- Quiz: control-flow logic and function scoping
- Challenge: FizzBuzz variants and a data-validation validator

### Week 4 — OOP Fundamentals

**Notebook:** `notebooks/1-fundamentals/04_oop_fundamentals.ipynb` · **8-10 h**

**Theory**
- Classes, instances, `__init__`, class vs instance attributes
- Encapsulation, properties, name mangling (`_name`)
- Inheritance, method overriding, MRO, multiple inheritance
- Dunder methods (`__repr__`, `__eq__`, `__len__`, …)
- `@classmethod`, `@staticmethod`

**Tools:** stdlib — the notebook's worked examples are your template

**Deliverable — Banking System**
Account (deposit/withdraw/balance), `SavingsAccount` with interest,
`CheckingAccount` with fees; custom exceptions for insufficient funds;
overdraft limits. Unit-testable design.

**Assessment**
- Quiz: inheritance/MRO and encapsulation
- Challenge: a small `Library` model (Book, Member, Loan) using the patterns above

---

## ⚡ Phase 2: Intermediate Python (Weeks 5-8)

### Week 5 — File I/O & Modules

**Notebook:** `notebooks/2-intermediate/05_file_handling.ipynb` · **6-8 h**

**Theory**
- Reading/writing text & binary files; encoding
- `with` / context managers (`Path.open`, file objects)
- `pathlib`: paths, globbing, directories
- Reading large files line-by-line and in chunks
- `tempfile`, `csv`, `json` for real data formats

**Tools:** `pathlib`, `csv`, `json` (stdlib)

**Deliverable — Log Analyzer**
Parse an application log (`timestamp level message` rows), report counts per
level, error rate, busiest hour; export a summary to CSV. Uses week 2-4 skills.

**Assessment**
- Quiz: context managers and pathlib
- Challenge: search/redact a string across a directory tree

### Week 6 — Packages & Virtual Environments

**Notebook:** `notebooks/2-intermediate/06_modules_packages.ipynb` · **6-8 h**

**Theory**
- `import` mechanics, modules vs packages, `__init__.py`
- Relative imports, `if __name__ == "__main__"`
- Virtual environments (`venv`) and why isolation matters
- Packaging basics: `pyproject.toml`, `pip install -e .`
- `pip` fundamentals; publishing overview (PyPI)

**Tools:** `venv`, `pip`, `setuptools`; see `requirements*.txt`

**Deliverable — Publishable Package**
Convert your week 5 Log Analyzer into a package with a CLI entry point
(`pyproject.toml`), importable API, and an editable install.

**Assessment**
- Quiz: import resolution and packaging
- Challenge: structure a multi-module library with clean internal API

### Week 7 — Error Handling & Logging

**Notebook:** `notebooks/2-intermediate/07_error_handling.ipynb` · **6-8 h**

**Theory**
- Exception hierarchy, raising and chaining (`raise ... from ...`)
- `try`/`except`/`else`/`finally` patterns
- Custom exceptions for your domain
- `logging`: levels, handlers, formatters, file + console output
- Debugging: tracebacks, `pdb`, common pitfalls

**Deliverable — Resilient Data Pipeline**
Process a batch of records where rows can be malformed: log each failure with
context, skip gracefully, continue the batch, and summarize outcomes.

**Assessment**
- Quiz: exception flow and logging best practices
- Challenge: retry-with-backoff wrapper for an unreliable operation

### Week 8 — Testing (pytest / TDD)

**Notebook:** `notebooks/2-intermediate/08_testing.ipynb` · **8-10 h**

**Theory**
- `unittest` and `pytest` fundamentals; fixtures and parametrize
- Test doubles: mocks, monkeypatching
- Test-driven development (red-green-refactor)
- Coverage and what it does *not* guarantee
- CI integration (see `.github/workflows/ci.yml`)

**Tools:** `pytest`, `pytest-cov` (dev requirements)

**Deliverable — 90% Coverage Suite**
Unit-test your Bank (week 4) or pipeline (week 7) with parametrized edge cases,
mocked I/O, and a coverage report ≥ 90%.

**Assessment**
- Quiz: mocking and fixture design
- Challenge: property-style randomized tests for the calculator (week 1)

---

## 🚀 Phase 3: Advanced Python (Weeks 9-12)

### Week 9 — Metaclasses & Descriptors

**Notebook:** `notebooks/3-advanced/09_metaclasses.ipynb` · **6-8 h**

**Theory**
- Classes as objects; `type()` as the default metaclass
- Custom metaclasses: `__new__`/`__init__` hooks, attribute validation
- Descriptors (`__get__`/`__set__`/`__delete__`) and when to reach for them
- ORM-style validation built from metaclasses; `__slots__`
- Pitfalls: recursion, mutable class state, debug-ability

**Deliverable — Mini ORM/Validator**
A tiny model layer: declare `class User(Model): name = String(required=True)`
and get automatic validation, defaults, and `.to_dict()`; implement with
descriptors + an optional metaclass that registers models.

**Assessment**
- Quiz: metaclass hooks and descriptor protocol
- Challenge: an auto-documented API controller using method decorators

### Week 10 — Async Programming

**Notebook:** `notebooks/3-advanced/10_async_programming.ipynb` · **8-10 h**

**Theory**
- The event loop; coroutines vs threads; `async`/`await`
- `asyncio.Task`, `gather`, timeouts, cancellation
- Async I/O with `aiofiles` and `httpx`/`requests`-style async clients
- Producer-consumer with queues
- When *not* to use asyncio (CPU-bound)

**Deliverable — Async Web Scraper**
Fetch a set of URLs concurrently with a polite rate limit, parse the results,
and save with `aiofiles`; handle retries and timeouts.

**Assessment**
- Quiz: event-loop semantics and blocking pitfalls
- Challenge: async pipeline with a bounded queue

### Week 11 — Design Patterns

**Notebook:** `notebooks/3-advanced/11_design_patterns.ipynb` · **8-10 h**

**Theory**
- Creational: singleton, factory, builder, prototype
- Structural: adapter, facade, decorator, proxy, composite
- Behavioral: observer, strategy, command, state, template method
- When patterns help and when they're overkill (Pythonic alternatives)

**Deliverable — Plugin Architecture**
A system that discovers and loads plugins by convention (registry pattern),
each exposing a common interface; a CLI that lists/executes plugins.

**Assessment**
- Quiz: pattern identification and trade-offs
- Challenge: refactor a God-class module using strategy + facade

### Week 12 — Performance Optimization

**Notebook:** `notebooks/3-advanced/12_performance_optimization.ipynb` · **6-8 h**

**Theory**
- Measuring first: `timeit`, `cProfile`, `memory-profiler`, line-profiler
- Algorithmic choices vs micro-optimizations
- Caching with `functools.lru_cache`; memoization
- Generators and lazy evaluation for memory efficiency
- String/container patterns that actually matter

**Deliverable — 10x Speedup Report**
Take a slow routine (your pipeline or a contrived one), profile it, apply 2-3
optimizations, and write a short report with before/after timings and
complexity notes.

**Assessment**
- Quiz: complexity analysis and profiling output
- Challenge: memory-efficient chunked processing of a large file

---

## 📊 Phase 4: Data Science (Weeks 13-14)

### Week 13 — Data Analysis (Pandas & NumPy)

**Notebooks:** `notebooks/4-data_science/14_data_analysis_with_pandas.ipynb`, `notebooks/4-data_science/15_numpy_numerical_computing.ipynb` · **10-12 h**

**Theory**
- NumPy: `ndarray`, broadcasting, vectorized ops, ufuncs, linear algebra
- pandas: `Series`/`DataFrame`, indexing (`loc`/`iloc`), filtering
- Cleaning: missing values, dtypes, duplicates, string methods
- Aggregation: `groupby`, `pivot_table`, `resample`
- Merging/joining tables; exporting
- Matplotlib fundamentals: figures, axes, styling (preview for week 14)

**Deliverable — EDA Dashboard**
Pick a dataset (or generate one), clean it, and produce an exploratory report:
10+ summary stats, 5+ charts, and 3 written findings. Save as a notebook with
markdown narrative.

**Assessment**
- Quiz: pandas indexing vs. NumPy broadcasting
- Challenge: join + re-shape two DataFrames into a pivot with no rows lost

### Week 14 — ML & Statistics

**Notebooks:** `notebooks/4-data_science/16_data_visualization_matplotlib.ipynb`, `notebooks/4-data_science/17_machine_learning_basics.ipynb`, `notebooks/4-data_science/18_statistics_probability.ipynb` · **12-15 h**

**Theory**
- Visualization with Matplotlib: line/bar/scatter/heatmap, subplots, annotations
- ML workflow: split → preprocess → train → evaluate → tune
- Regression & classification; metrics (MSE, R², accuracy, confusion matrix)
- Unsupervised learning: clustering, elbow/silhouette
- Statistics: distributions, sampling, hypothesis testing, confidence intervals

**Deliverable — End-to-End ML Project**
On a small real dataset: EDA (from week 13), a baseline linear model, one
improved model, cross-validated evaluation, and a one-page summary with
visualizations and interpretation.

**Assessment**
- Quiz: bias/variance and metric selection
- Challenge: report whether a model improvement is statistically significant

---

## 🎁 Extras (post-course)

| Area | Where | What |
|------|-------|------|
| Interview prep | `references/interview-prep/` | 14-Q&A primer notebook + README |
| Problem practice | `practice/problems/` | Starter + solution exercises, stdlib-only |
| Sample data | `practice/data/` | Synthetic `sales.csv` (used by the EDA project) |
| Cheatsheets | `references/cheatsheets/` | Python, data structures, pandas one-pagers |
| Companion guides | `references/guides/` | Decorators & closures; automation & DevOps |
| Project specs | `practice/projects/` | The 14 weekly deliverable specs |

Suggested extras order: `practice/problems/` → `references/cheatsheets/` (ongoing) → `references/interview-prep/`.

## 🎯 Final Assessment & Certification

To "finish" the path, complete **all four phases** and:

1. **Portfolio:** week 14 ML project + week 8 test suite + week 6 package.
2. **Code quality:** PEP 8 via `black`/`ruff`, type hints, docstrings, tests,
   error handling + logging — all project code.
3. **Benchmarks:** persistence (day 1 vs week 14), complexity awareness,
   profiling experience from week 12.
4. **Interview readiness:** complete `references/interview-prep/` self-check.

## 📚 Resources

- Official Python tutorial: <https://docs.python.org/3/tutorial/>
- Real Python: <https://realpython.com/>
- pandas user guide: <https://pandas.pydata.org/docs/user_guide/>
- scikit-learn docs: <https://scikit-learn.org/stable/>
- For every week's notebook, the **Summary** cell lists further reading links.

---

*Happy learning — one week at a time. 🐍*