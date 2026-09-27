"""Reference answers for the 10 data-science notebook prompts."""

from math import ceil
from random import Random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def monthly_revenue(sales: pd.DataFrame) -> pd.Series:
    """Sum valid revenue by calendar month and return chronological periods."""
    dates = pd.to_datetime(sales["date"], errors="coerce")
    revenue = pd.to_numeric(sales["revenue"], errors="coerce")
    valid = dates.notna() & revenue.notna()
    months = dates[valid].dt.to_period("M")
    return revenue[valid].groupby(months).sum().sort_index()


def clean_sales(sales: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy containing valid dates and numeric revenue."""
    cleaned = sales.copy()
    cleaned["date"] = pd.to_datetime(cleaned["date"], errors="coerce")
    cleaned["revenue"] = pd.to_numeric(cleaned["revenue"], errors="coerce")
    return cleaned.dropna(subset=["date", "revenue"])


def standardize_columns(values: np.ndarray) -> np.ndarray:
    """Z-score each column, mapping constant and empty columns to zeros."""
    array = np.asarray(values, dtype=float)
    if array.ndim != 2:
        raise ValueError("values must be a two-dimensional array")
    if array.size == 0:
        return array.copy()
    centered = array - array.mean(axis=0)
    deviations = array.std(axis=0)
    return np.divide(
        centered,
        deviations,
        out=np.zeros_like(centered),
        where=deviations != 0,
    )


def moving_average(values: np.ndarray, window: int) -> np.ndarray:
    """Return means for each complete one-dimensional window."""
    array = np.asarray(values, dtype=float)
    if array.ndim != 1:
        raise ValueError("values must be one-dimensional")
    if not 1 <= window <= len(array):
        raise ValueError("window must be between one and the input length")
    return np.convolve(array, np.ones(window) / window, mode="valid")


def plot_series(x, y, *, ax=None, label="Value"):
    """Plot a labeled series and return its axes without displaying it."""
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel(label)
    return ax


def plot_category_counts(frame: pd.DataFrame, column: str, *, ax=None):
    """Plot non-missing category counts in descending order and return axes."""
    if column not in frame:
        raise KeyError(column)
    if ax is None:
        _, ax = plt.subplots()
    frame[column].value_counts().plot(kind="bar", ax=ax)
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    return ax


def binary_metrics(actual: list[int], predicted: list[int]) -> dict[str, float]:
    """Calculate accuracy, precision, recall, and F1 for binary labels."""
    if not actual or len(actual) != len(predicted):
        raise ValueError("inputs must be non-empty and have equal lengths")
    if any(label not in (0, 1) for label in actual + predicted):
        raise ValueError("labels must be zero or one")

    true_positive = sum(left == 1 and right == 1 for left, right in zip(actual, predicted))
    false_positive = sum(left == 0 and right == 1 for left, right in zip(actual, predicted))
    false_negative = sum(left == 1 and right == 0 for left, right in zip(actual, predicted))
    correct = sum(left == right for left, right in zip(actual, predicted))
    precision = (
        true_positive / (true_positive + false_positive) if true_positive + false_positive else 0.0
    )
    recall = (
        true_positive / (true_positive + false_negative) if true_positive + false_negative else 0.0
    )
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "accuracy": correct / len(actual),
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def holdout_indices(
    size: int,
    test_fraction: float,
    seed: int,
) -> tuple[list[int], list[int]]:
    """Return deterministic, shuffled train and test index lists."""
    if size < 2 or not 0 < test_fraction < 1:
        raise ValueError("size must be at least two and fraction strictly between zero and one")
    indices = list(range(size))
    Random(seed).shuffle(indices)
    test_count = min(size - 1, max(1, ceil(size * test_fraction)))
    return indices[test_count:], indices[:test_count]


def bootstrap_mean_interval(
    values,
    *,
    resamples: int,
    confidence: float,
    seed: int,
) -> tuple[float, float]:
    """Return a seeded percentile bootstrap interval for the mean."""
    sample = np.asarray(values, dtype=float)
    if sample.ndim != 1 or sample.size < 2 or not np.isfinite(sample).all():
        raise ValueError("values must contain at least two finite numbers")
    if resamples < 1 or not 0 < confidence < 1:
        raise ValueError("resamples must be positive and confidence strictly between zero and one")
    generator = np.random.default_rng(seed)
    bootstrap_means = generator.choice(sample, size=(resamples, sample.size), replace=True).mean(
        axis=1
    )
    tail = (1 - confidence) / 2
    lower, upper = np.quantile(bootstrap_means, [tail, 1 - tail])
    return float(lower), float(upper)


def permutation_p_value(group_a, group_b, *, resamples: int, seed: int) -> float:
    """Return a two-sided permutation p-value for a difference in means."""
    first = np.asarray(group_a, dtype=float)
    second = np.asarray(group_b, dtype=float)
    if first.ndim != 1 or second.ndim != 1 or not first.size or not second.size:
        raise ValueError("both groups must be non-empty one-dimensional samples")
    if not np.isfinite(first).all() or not np.isfinite(second).all():
        raise ValueError("samples must contain only finite numbers")
    if resamples < 1:
        raise ValueError("resamples must be positive")

    pooled = np.concatenate((first, second))
    observed = abs(first.mean() - second.mean())
    generator = np.random.default_rng(seed)
    extreme = 0
    for _ in range(resamples):
        shuffled = generator.permutation(pooled)
        difference = abs(shuffled[: first.size].mean() - shuffled[first.size :].mean())
        extreme += difference >= observed
    return (extreme + 1) / (resamples + 1)


def _check() -> None:
    sales = pd.DataFrame(
        {
            "date": ["2026-01-02", "2026-01-20", "2026-02-01", "invalid"],
            "revenue": [3, 4, 5, 6],
        }
    )
    monthly = monthly_revenue(sales)
    assert monthly.loc[pd.Period("2026-01", freq="M")] == 7
    cleaned = clean_sales(sales)
    assert len(cleaned) == 3
    assert sales.loc[3, "date"] == "invalid"
    standardized = standardize_columns(np.array([[1.0, 5.0], [3.0, 5.0]]))
    assert np.allclose(standardized[:, 0], [-1.0, 1.0])
    assert np.allclose(standardized[:, 1], [0.0, 0.0])
    assert np.allclose(moving_average(np.array([1, 2, 3, 4]), 2), [1.5, 2.5, 3.5])
    axes = plot_series([1, 2], [3, 4], label="Revenue")
    assert axes.get_ylabel() == "Revenue"
    plt.close(axes.figure)
    axes = plot_category_counts(pd.DataFrame({"region": ["west", "east", "west"]}), "region")
    assert axes.get_ylabel() == "Count"
    plt.close(axes.figure)
    metrics = binary_metrics([1, 0, 1], [1, 0, 0])
    assert metrics["accuracy"] == 2 / 3
    assert metrics["recall"] == 0.5
    train, test = holdout_indices(10, 0.2, seed=7)
    assert set(train).isdisjoint(test)
    assert sorted(train + test) == list(range(10))
    assert holdout_indices(10, 0.2, seed=7) == (train, test)
    lower, upper = bootstrap_mean_interval([1, 2, 3, 4], resamples=1000, confidence=0.95, seed=3)
    assert lower <= 2.5 <= upper
    p_value = permutation_p_value([1, 2, 3], [1, 2, 3], resamples=500, seed=3)
    assert 0.0 < p_value <= 1.0


if __name__ == "__main__":
    _check()
    print("OK")
