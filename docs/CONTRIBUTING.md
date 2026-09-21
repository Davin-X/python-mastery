# Contributing

Thanks for your interest in improving **Python Mastery**! This is a learning
repository, so contributions range from fixing a typo to adding an entire
exercises section to a notebook.

## Ways to contribute

- 🐛 Report a factual or code error in an issue.
- 📝 Improve an explanation, add examples, or write a cheatsheet.
- 🧪 Add exercises and solutions to a notebook.
- 🎨 Fix repository hygiene (docs, CI, dependencies).

## Development setup

```bash
# 1. Clone
git clone git@github.com:Davin-X/python-mastery.git
cd python-mastery

# 2. Create an environment (Python >= 3.10)
python -m venv .venv
source .venv/bin/activate

# 3. Install runtime + dev dependencies
pip install -r requirements.txt -r requirements-dev.txt

# 4. Launch
jupyter lab
```

## Notebook conventions

- Keep the existing cell template shape: **objectives → concepts → exercises →
  summary**.
- Notebooks must execute top-to-bottom after `pip install -r requirements.txt`.
  Do **not** add `!pip install` or `subprocess.check_call(... pip install ...)`
  cells — dependencies belong in `requirements.txt`.
- Commit notebooks with outputs **cleared** (`nbstripout`) unless the change
  is specifically about rendered output.
- Keep notebooks machine-checkable by running:

  ```bash
  python scripts/validate_notebooks.py
  bash scripts/audit_repo.sh
  ```

## Commits

Conventional Commits, e.g. `docs(notebooks): add exercises to 02_data_structures`.

## Pull requests

1. Branch from `main` (e.g. `docs/fix-typos`).
2. Make focused changes with a clear commit message.
3. Update the relevant index in `README.md` / `LEARNING_PATH.md` when content
   changes.
4. Open a PR; CI validates notebook structure and repo hygiene.

## Code of Conduct

Be respectful — see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).