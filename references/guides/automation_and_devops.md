# Automation & DevOps

> **Status:** reading-only companion. This topic has no dedicated notebook; the
> skills below build on `05_file_handling` (pathlib/shutil), `07_error_handling`
> (logging), and `08_testing`.

## What you can automate with the standard library alone

A practical, production-shaped script combines `argparse`, `logging`, `pathlib`,
and `shutil`. The canonical example is a **file organizer**: move files into
category folders, optionally grouped by modification date, with duplicate
handling and a dry-run mode.

```python
#!/usr/bin/env python3
"""Organize a directory's files by extension (and optionally by year/month)."""
import argparse
import logging
import shutil
from datetime import datetime
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("file_organizer.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".md", ".odt"],
    "spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
    "code": [".py", ".js", ".ts", ".html", ".css", ".java", ".scala"],
    "archives": [".zip", ".tar", ".gz", ".7z"],
    "others": [],
}


def category_of(path: Path) -> str:
    suffix = path.suffix.lower()
    return next((name for name, exts in CATEGORIES.items() if suffix in exts), "others")


def organize(source: Path, dest: Path, by_date: bool) -> int:
    dest.mkdir(parents=True, exist_ok=True)
    moved = 0
    for file_path in source.rglob("*"):
        if not file_path.is_file():
            continue
        target = dest / category_of(file_path)
        if by_date:
            modified = datetime.fromtimestamp(file_path.stat().st_mtime)
            target /= f"{modified.year}-{modified.month:02d}"
        target.mkdir(parents=True, exist_ok=True)

        sibling = target / file_path.name          # de-duplicate names
        counter = 1
        while sibling.exists():
            sibling = target / f"{file_path.stem}_{counter}{file_path.suffix}"
            counter += 1

        shutil.move(str(file_path), str(sibling))
        logger.info("moved %s -> %s", file_path, sibling)
        moved += 1
    return moved


def main() -> None:
    parser = argparse.ArgumentParser(description="Organize files by category/date")
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--by-date", action="store_true")
    args = parser.parse_args()
    count = organize(args.source, args.destination, args.by_date)
    print(f"organized {count} file(s)")


if __name__ == "__main__":
    main()
```

## Beyond scripts

| Area | Tool | Notes |
|------|------|-------|
| Task scheduling | `cron` / Task Scheduler / `apscheduler` | For long-running Python jobs prefer `apscheduler` |
| Isolation | `venv`, `pip-tools`, `uv` | Pin versions for reproducible runs |
| Containers | `Docker` | Package the app + environment as one image |
| CI/CD | GitHub Actions | Like this repo's `.github/workflows/ci.yml` |
| Deployment | `systemd`, `Fly.io`, `Railway` | Serve long-running jobs or APIs |

## Practice suggestions

1. Add `--dry-run` to the organizer above (show what *would* move without touching files).
2. Write a scheduler that runs the organizer weekly and reports via `logging`.
3. Add three `unittest`/`pytest` tests for `category_of` and the rename loop.
4. Convert the script into a `pyproject.toml`-based package with a `cli` entry point
   (see `06_modules_packages`).

## Further reading

- [pathlib — official docs](https://docs.python.org/3/library/pathlib.html)
- [Python Packaging User Guide](https://packaging.python.org/)