# 🐍 Python Mastery

A structured **14-week path from Python basics to machine learning** — 18
interactive notebooks, cheatsheets and guides, practice problems, and an
interview primer. Built to be completed in order at ~8-10 h/week.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📅 14-Week Curriculum

| Week | Focus | Notebook(s) | Hours | Deliverable |
|------|-------|-------------|-------|-------------|
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

Syllabus with theory/practice/assessment per week →
[`LEARNING_PATH.md`](LEARNING_PATH.md). Week & deliverable specs →
[`practice/projects/README.md`](practice/projects/README.md). Practice index →
[`practice/README.md`](practice/README.md).

## 🧭 Contents — notebooks

| Notebook | Week | Level | Topic |
|----------|------|-------|-------|
| `01_python_basics` | 1 | Fundamentals | variables, types, operators, strings |
| `02_data_structures` | 2 | Fundamentals | list/tuple/dict/set, comprehensions |
| `03_control_flow` | 3 | Fundamentals | conditionals, loops, functions |
| `04_oop_fundamentals` | 4 | Fundamentals | classes, inheritance, dunders |
| `05_file_handling` | 5 | Intermediate | I/O, context managers, `pathlib` |
| `06_modules_packages` | 6 | Intermediate | packages, venv, packaging |
| `07_error_handling` | 7 | Intermediate | exceptions, logging, debugging |
| `08_testing` | 8 | Intermediate | `unittest`, `pytest`, TDD, coverage |
| `09_metaclasses` | 9 | Advanced | `type()`, metaclasses, descriptors |
| `10_async_programming` | 10 | Advanced | `asyncio`, async/await, `aiofiles` |
| `11_design_patterns` | 11 | Advanced | GoF + Pythonic patterns |
| `12_performance_optimization` | 12 | Advanced | profiling, caching, generators |
| `14_data_analysis_with_pandas` | 13 | Data Science | Series/DataFrame, cleaning, aggregation |
| `15_numpy_numerical_computing` | 13 | Data Science | `ndarray`, ufuncs, linear algebra |
| `16_data_visualization_matplotlib` | 14 | Data Science | figures, axes, charts |
| `17_machine_learning_basics` | 14 | Data Science | regression, classification, clustering |
| `18_statistics_probability` | 14 | Data Science | distributions, hypothesis testing |

> Curriculum notebooks live in `notebooks/{1-fundamentals,2-intermediate,3-advanced,4-data_science}/`.
> There is no `13_*.ipynb` — the old 13 (web development) was removed; the
> data-science notebooks keep their original numbers.
> The curriculum contains 41 function-writing prompts; the interview primer
> adds 10 more: `references/interview-prep/interview_questions_mastery.ipynb`.

## 📁 Structure

```
python-mastery/
├── notebooks/                 # the 14-week curriculum (18 notebooks)
│   ├── 1-fundamentals/  01-04
│   ├── 2-intermediate/  05-08
│   ├── 3-advanced/      09-12
│   └── 4-data_science/  14-18
├── references/                # lookup & study material; start at references/README.md
│   ├── cheatsheets/           # syntax · data structures · algorithms · testing · pandas
│   ├── guides/                # decorators · automation & DevOps
│   └── interview-prep/        # 14 concept Q&A + 10 coding prompts
├── practice/                  # hands-on work
│   ├── solutions/             # five phase-level answer files
│   ├── problems/              # question + starter + solution
│   ├── projects/              # the 14 weekly deliverable specs
│   └── data/                  # sample dataset (synthetic)
├── scripts/                   # validate_notebooks · audit_repo · strip_pip_installs
├── docs/                      # CONTRIBUTING · CHANGELOG · SECURITY · CoC
├── README.md  LEARNING_PATH.md  LICENSE
├── requirements.txt  requirements-dev.txt  pyproject.toml
└── .github/workflows/ci.yml  .editorconfig  .gitattributes  .python-version  .vscode/
```

## 🚀 Quick Start

```bash
# 1. Clone
git clone git@github.com:Davin-X/python-mastery.git
cd python-mastery

# 2. Environment (Python 3.10+)
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Dependencies
pip install -r requirements.txt  # + requirements-dev.txt for tooling

# 4. Start learning
jupyter lab
# open notebooks/1-fundamentals/01_python_basics.ipynb
```

## ✅ What you'll learn

- **Weeks 1-4 (Foundations):** syntax, data structures, control flow, OOP.
- **Weeks 5-8 (Intermediate):** file I/O, packages, error handling, testing.
- **Weeks 9-12 (Advanced):** metaprogramming, async, design patterns, profiling.
- **Weeks 13-14 (Data Science):** pandas, NumPy, matplotlib, scikit-learn,
  statistics — enough to build and evaluate an end-to-end ML project.

## 🧠 Repo convention

Notebooks never run `pip install` (see [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md)); dependencies live in
`requirements.txt` and are installed once. Every notebook is checked by
`scripts/validate_notebooks.py` in CI.

## 🤝 Contributing

See [`CONTRIBUTING.md`](docs/CONTRIBUTING.md) and
[`CODE_OF_CONDUCT.md`](docs/CODE_OF_CONDUCT.md). Bug or typo? Open an issue —
every contribution helps.

## 📄 License

[MIT](LICENSE) © 2026 Devendra Kumar