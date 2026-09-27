#!/usr/bin/env python3
"""Structural validation for every notebook in the repository.

Checks:
  * Expected notebook set per folder (parity with the curriculum).
  * Valid nbformat 4 document with a kernelspec.
  * No empty code cells.
  * No ``subprocess``-based ``pip install`` anti-patterns in code cells.

Usage (from the repository root):
    python scripts/validate_notebooks.py
Exit code is non-zero when any check fails.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PIP_SUBPROCESS = re.compile(r"subprocess\.(check_call|call|run|Popen)\([^)]*['\"]pip['\"]")

# Authoritative notebook layout — keep in sync with the README index.
EXPECTED: dict[str, list[str]] = {
    "notebooks/1-fundamentals": [
        "01_python_basics",
        "02_data_structures",
        "03_control_flow",
        "04_oop_fundamentals",
    ],
    "notebooks/2-intermediate": [
        "05_file_handling",
        "06_modules_packages",
        "07_error_handling",
        "08_testing",
    ],
    "notebooks/3-advanced": [
        "09_metaclasses",
        "10_async_programming",
        "11_design_patterns",
        "12_performance_optimization",
    ],
    "notebooks/4-data_science": [
        "14_data_analysis_with_pandas",
        "15_numpy_numerical_computing",
        "16_data_visualization_matplotlib",
        "17_machine_learning_basics",
        "18_statistics_probability",
    ],
    "references/interview-prep": ["interview_questions_mastery"],
}


def all_notebooks() -> list[Path]:
    paths = sorted(ROOT.glob("notebooks/**/*.ipynb"))
    paths += sorted((ROOT / "references" / "interview-prep").glob("*.ipynb"))
    return paths


def check_layout(failures: list[str]) -> None:
    for folder, expected in EXPECTED.items():
        actual = sorted(p.stem for p in (ROOT / folder).glob("*.ipynb"))
        if actual != expected:
            failures.append(f"{folder}/: expected {expected}, found {actual}")


def main() -> int:
    failures: list[str] = []
    check_layout(failures)

    notebooks = all_notebooks()
    for path in notebooks:
        rel = path.relative_to(ROOT).as_posix()
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"{rel}: invalid JSON ({exc})")
            continue

        if doc.get("nbformat") != 4:
            failures.append(f"{rel}: nbformat != 4")

        if not doc.get("metadata", {}).get("kernelspec", {}).get("name"):
            failures.append(f"{rel}: missing kernelspec")

        for index, cell in enumerate(doc.get("cells", []), start=1):
            cell_type = cell.get("cell_type")
            if cell_type not in {"markdown", "code", "raw"}:
                failures.append(f"{rel}: cell #{index} has invalid type {cell_type!r}")
            if cell_type != "code":
                continue
            source = "".join(cell.get("source", []))
            if not source.strip():
                failures.append(f"{rel}: empty code cell #{index}")
            if PIP_SUBPROCESS.search(source):
                failures.append(
                    f"{rel}: code cell #{index} installs via subprocess "
                    "(see docs/CONTRIBUTING.md)"
                )

    for failure in failures:
        print(f"FAIL  {failure}")
    print(f"checked {len(notebooks)} notebooks, {len(failures)} issue(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
