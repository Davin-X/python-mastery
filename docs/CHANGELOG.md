# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `LICENSE` (MIT), `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`
- **14-week curriculum** in `LEARNING_PATH.md` — replaces the previous
  16/18-week plan, aligned 1:1 with the notebooks on disk.
- Notebook index (absorbed into `README.md`; per-file time/prereqs live in
  `LEARNING_PATH.md`).
- Supporting material: `references/` (cheatsheets, guides, interview-prep) and
  `practice/` (problems, the 14 project specs, sample data).
- Engineering hygiene: slim `requirements.txt`, `requirements-dev.txt`,
  `pyproject.toml` (ruff/black/pytest), `.editorconfig`,
  `.gitattributes`, `.python-version`, recommended VS Code extensions.
- Tooling: `scripts/validate_notebooks.py` and reusable `scripts/audit_repo.sh`,
  wired into a GitHub Actions CI workflow.

### Changed
- `README.md` rewritten to match the repository on disk (accurate structure,
  counts, clone URL) and the new 14-week curriculum.
- Deprecated `pip install` calls removed from notebook cells (dependencies are
  now installed once via `pip install -r requirements.txt`).
- Default branch set to `main`; GitHub description/topics updated.

### Removed
- Dead "Web Development" week content from `LEARNING_PATH.md` (the Flask
  notebook no longer exists); corresponding `requirements.txt` entries dropped.