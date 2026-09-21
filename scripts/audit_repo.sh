#!/usr/bin/env bash
# =============================================================================
# audit_repo.sh — repo hygiene gate (Tier 1 of the repo standard).
#
# Run from inside the repository root. Prints PASS/FAIL per check and exits
# non-zero if anything fails, so it is safe to run from CI.
#
# Usage: bash scripts/audit_repo.sh
# =============================================================================
set -u

fail=0
pass=0

root="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "ERROR: not inside a git repository"; exit 1; }
cd "$root"

check() { # $1 = ok (0/1)   $2 = label
  if [ "$1" -eq 0 ]; then
    pass=$((pass + 1))
    printf 'PASS  %s\n' "$2"
  else
    fail=$((fail + 1))
    printf 'FAIL  %s\n' "$2"
  fi
}

# --- README / metadata ------------------------------------------------------
if [ -f README.md ] && [ "$(wc -c < README.md 2>/dev/null || echo 0)" -gt 500 ]; then
  check 0 "README.md exists and is non-trivial"
else
  check 1 "README.md exists and is non-trivial"
fi

[ -f LICENSE ]; check $? "LICENSE exists"

[ -f .gitignore ]; check $? ".gitignore exists"

[ "$(grep -ci 'mit license' LICENSE 2>/dev/null || echo 0)" -gt 0 ]; check $? "LICENSE text mentions MIT"

# --- .gitignore hygiene -----------------------------------------------------
dup=$(grep -vE '^\s*(#|$)' .gitignore 2>/dev/null | sort | uniq -d | wc -l | tr -d ' ')
[ "$dup" -eq 0 ]; check $? ".gitignore has no duplicate lines (duplicates=$dup)"

# --- Junk on disk / in git --------------------------------------------------
ds_store_disk=$(find . -path ./.git -prune -o -name '.DS_Store' -print | wc -l | tr -d ' ')
[ "$ds_store_disk" -eq 0 ]; check $? "no .DS_Store files on disk (count=$ds_store_disk)"

if git ls-files | grep -qE '\.DS_Store|__pycache__|\.pyc$|\.egg-info|node_modules|/target/|\.class$|\.ipynb_checkpoints'; then
  ok=1
else
  ok=0
fi
check "$ok" "no junk files tracked by git"

# --- Git state --------------------------------------------------------------
dirty=$(git status --porcelain | wc -l | tr -d ' ')
dirty=$((dirty))
[ "$dirty" -eq 0 ]; check $? "working tree is clean (dirty=$dirty)"

branch=$(git rev-parse --abbrev-ref HEAD)
[ "$branch" = main ]; check $? "default branch is 'main' (got '$branch')"

printf '\n%d passed, %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]