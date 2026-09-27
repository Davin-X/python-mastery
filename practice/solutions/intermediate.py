"""Reference answers for the 10 intermediate Python prompts."""

import csv
import re
import unicodedata
from collections import Counter
from collections.abc import Callable
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TypeVar

Result = TypeVar("Result")


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    """Read CSV data rows as dictionaries keyed by the header row."""
    with path.open(newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def count_log_levels(lines: list[str]) -> dict[str, int]:
    """Count levels from well-formed timestamp/level/message log lines."""
    levels: Counter[str] = Counter()
    for line in lines:
        parts = line.split(maxsplit=2)
        if len(parts) == 3:
            levels[parts[1].upper()] += 1
    return dict(levels)


def find_files(root: Path, suffix: str) -> list[Path]:
    """Return recursively found files with the requested case-insensitive suffix."""
    normalized_suffix = suffix.lower()
    if not normalized_suffix.startswith("."):
        normalized_suffix = f".{normalized_suffix}"
    return sorted(
        (
            path
            for path in root.rglob("*")
            if path.is_file() and path.suffix.lower() == normalized_suffix
        ),
        key=lambda path: path.as_posix(),
    )


def slugify(text: str) -> str:
    """Create a lowercase ASCII slug separated by single hyphens."""
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", ascii_text)).strip("-")


def resolve_setting(
    cli_value: str | None,
    env_value: str | None,
    default: str,
) -> str:
    """Choose a setting from command-line, environment, then default values."""
    if cli_value is not None:
        return cli_value
    if env_value is not None:
        return env_value
    return default


def parse_positive_int(text: str) -> int:
    """Parse a positive integer and chain invalid integer conversions."""
    try:
        value = int(text.strip())
    except ValueError as exc:
        raise ValueError("text must contain an integer") from exc
    if value <= 0:
        raise ValueError("integer must be positive")
    return value


def parse_settings(lines: list[str]) -> dict[str, str]:
    """Parse key-value lines, skipping comments and blank lines."""
    settings: dict[str, str] = {}
    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        key, separator, value = stripped.partition("=")
        if not separator or not key.strip():
            raise ValueError(f"malformed setting on line {line_number}")
        settings[key.strip()] = value.strip()
    return settings


def retry_call(operation: Callable[[], Result], attempts: int) -> Result:
    """Retry an operation on timeouts and propagate all other errors."""
    if attempts < 1:
        raise ValueError("attempts must be at least 1")
    for attempt in range(attempts):
        try:
            return operation()
        except TimeoutError:
            if attempt == attempts - 1:
                raise
    raise AssertionError("unreachable")


def normalize_email(address: str) -> str:
    """Normalize and validate the deliberately small email format in the prompt."""
    normalized = address.strip().lower()
    if normalized.count("@") != 1:
        raise ValueError("address must contain exactly one @")
    local_part, domain = normalized.split("@")
    labels = domain.split(".")
    if not local_part or len(labels) < 2 or any(not label for label in labels):
        raise ValueError("address must have a local part and dotted domain")
    return normalized


def partition_records(
    records: list[dict[str, object]],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    """Partition records by non-empty name and non-negative integer age."""
    valid: list[dict[str, object]] = []
    invalid: list[dict[str, object]] = []
    for record in records:
        name = record.get("name")
        age = record.get("age")
        has_valid_name = isinstance(name, str) and bool(name.strip())
        has_valid_age = isinstance(age, int) and not isinstance(age, bool) and age >= 0
        (valid if has_valid_name and has_valid_age else invalid).append(record)
    return valid, invalid


def _check() -> None:
    assert count_log_levels(["10:00 info started", "bad", "10:01 ERROR failed"]) == {
        "INFO": 1,
        "ERROR": 1,
    }
    with TemporaryDirectory() as temporary_directory:
        root = Path(temporary_directory)
        (root / "a.csv").write_text("name,score\nAda,10\n", encoding="utf-8")
        (root / "empty.csv").write_text("name,score\n", encoding="utf-8")
        nested = root / "nested"
        nested.mkdir()
        (nested / "B.CSV").write_text("x\n1\n", encoding="utf-8")
        (root / "note.txt").write_text("not csv", encoding="utf-8")
        assert read_csv_rows(root / "a.csv") == [{"name": "Ada", "score": "10"}]
        assert read_csv_rows(root / "empty.csv") == []
        assert [path.name for path in find_files(root, ".csv")] == [
            "a.csv",
            "empty.csv",
            "B.CSV",
        ]
    assert slugify("  Python, Packages! ") == "python-packages"
    assert slugify("Part 2 / Tests") == "part-2-tests"
    assert slugify("Café") == "cafe"
    assert resolve_setting("fast", "safe", "default") == "fast"
    assert resolve_setting(None, "safe", "default") == "safe"
    assert resolve_setting(None, None, "default") == "default"
    assert resolve_setting("", "safe", "default") == ""
    assert parse_positive_int(" 12 ") == 12
    assert parse_settings(["# note", "mode=fast", "path=a=b"]) == {
        "mode": "fast",
        "path": "a=b",
    }
    assert retry_call(lambda: 7, attempts=2) == 7
    attempts = 0

    def flaky_operation() -> str:
        nonlocal attempts
        attempts += 1
        if attempts < 2:
            raise TimeoutError
        return "ready"

    assert retry_call(flaky_operation, attempts=2) == "ready"
    assert normalize_email(" Ada@Example.COM ") == "ada@example.com"
    records = [{"name": "Ada", "age": 36}, {"name": "", "age": 2}]
    original = [record.copy() for record in records]
    valid, invalid = partition_records(records)
    assert valid == [records[0]]
    assert invalid == [records[1]]
    assert records == original


if __name__ == "__main__":
    _check()
    print("OK")
