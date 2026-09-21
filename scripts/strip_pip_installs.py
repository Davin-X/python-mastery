#!/usr/bin/env python3
"""Remove ``subprocess``-based ``pip install`` anti-patterns from notebooks.

Only cells that call ``subprocess.check_call([sys.executable, '-m', 'pip', ...])``
are modified. Literal shell-style pip commands used to *teach* packaging
(notebooks ``06_modules_packages`` / ``08_testing``) are left untouched.

Idempotent. Run from the repository root:
    python scripts/strip_pip_installs.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PIP_SUBPROCESS = re.compile(r"subprocess\.(check_call|call|run|Popen)\([^)]*['\"]pip['\"]")
PRINT_INSTALLING = re.compile(
    r"print\(['\"](?:Installing |[^'\"]*not available[^'\"]*[Ii]nstalling)"
)

HELP_COMMENT = "    # Dependency missing? Install once with: pip install -r requirements.txt\n"


def process_cell(source: str) -> tuple[str, bool]:
    lines = source.splitlines(keepends=True)
    changed = False

    # Pass 1: drop pip install calls and "Installing ..." prints.
    kept: list[str] = []
    for line in lines:
        stripped = line.strip()
        if PIP_SUBPROCESS.search(stripped):
            changed = True
            continue
        if PRINT_INSTALLING.search(stripped):
            kept.append(HELP_COMMENT)
            changed = True
            continue
        kept.append(line)
    lines = kept

    # Pass 2: drop `import subprocess` / `import sys` if no longer referenced.
    for module in ("subprocess", "sys"):
        if re.search(rf"\b{module}\.", "".join(lines)):
            continue
        cleaned: list[str] = []
        for line in lines:
            if re.match(rf"import {module}\s*$", line.strip()):
                changed = True
                continue
            cleaned.append(line)
        lines = cleaned

    return "".join(lines), changed


def main() -> int:
    changed_files: list[str] = []
    for path in sorted(ROOT.glob("notebooks/**/*.ipynb")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        dirty = False
        for cell in doc.get("cells", []):
            if cell.get("cell_type") != "code":
                continue
            source = "".join(cell.get("source", []))
            new_source, changed = process_cell(source)
            if changed:
                cell["source"] = new_source
                dirty = True
        if dirty:
            path.write_text(
                json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
            )
            changed_files.append(str(path))

    if changed_files:
        print(f"cleaned {len(changed_files)} notebook(s):")
        for name in changed_files:
            print(f"  - {name}")
    else:
        print("no notebooks needed changes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())