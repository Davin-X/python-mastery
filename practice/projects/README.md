# Projects — the 14 Weekly Deliverables

Every week of [`LEARNING_PATH.md`](../../LEARNING_PATH.md) ends with a project.
These are **your assignments** — the repository intentionally ships *specs,
not finished code*. Build them yourself after finishing the week's notebook,
then compare against the concepts you just learned.

## Specs at a glance

| # | Project | Minimum requirements | Acceptance bar |
|---|---------|----------------------|----------------|
| 1 | Calculator CLI | `+ - * / **`, input validation, loop until quit | handles zero/non-numeric input |
| 2 | Inventory Manager | SKU-keyed dict, add/remove/update, reorder alerts | fast-mover report works |
| 3 | Text Adventure Game | rooms, player state, choices, win/lose | replayable loop |
| 4 | Banking System | Account + Savings/Checking, custom exceptions | overdrafts rejected |
| 5 | Log Analyzer | parse `ts level msg`, level counts, error rate | CSV summary export |
| 6 | Publishable Package | `pyproject.toml`, CLI entry point | `pip install -e .` works |
| 7 | Resilient Data Pipeline | batch rows, malformed rows logged + skipped | summary report at end |
| 8 | 90% Coverage Suite | pytest + parametrized edge cases + mocked I/O | `pytest --cov` ≥ 90% |
| 9 | Mini ORM/Validator | `Model` base, typed fields, validation, `.to_dict()` | invalid values rejected |
| 10 | Async Web Scraper | concurrent fetches, rate limit, retries, `aiofiles` save | timeouts handled |
| 11 | Plugin Architecture | registry discovers plugins by convention | CLI lists/executes plugins |
| 12 | 10x Speedup Report | profile → 2-3 optimizations → before/after timings | complexity notes included |
| 13 | EDA Dashboard | clean `data/sales.csv` (`../data/`) or your own dataset | 10+ stats, 5+ charts, 3 findings |
| 14 | End-to-End ML Project | EDA + baseline + improved model + cross-validation | 1-page summary with charts |

## How to practice

- Implement Week *N* right after finishing the Week *N* notebook — from memory,
  not by copying cells.
- Earlier projects compound: Week 8's test suite should test Week 4's Bank,
  and Week 14's ML project reuses Week 13's EDA.
- Between projects, drill micro-skills with `practice/problems/`.
- Quality bar for every project: runs without errors · type hints · docstrings
  on public functions · error handling + logging where it matters.