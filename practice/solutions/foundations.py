"""Reference answers for the 10 foundation prompts in the curriculum."""

from collections import Counter


def format_duration(total_seconds: int) -> str:
    """Format non-negative seconds as zero-padded hours, minutes, and seconds."""
    if total_seconds < 0:
        raise ValueError("total_seconds must not be negative")
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def calculate_tip(subtotal: float, tip_percent: float) -> float:
    """Calculate a tip rounded to cents after validating its inputs."""
    if subtotal < 0:
        raise ValueError("subtotal must not be negative")
    if not 0 <= tip_percent <= 100:
        raise ValueError("tip_percent must be between 0 and 100")
    return round(subtotal * tip_percent / 100, 2)


def unique_in_order(items: list[int]) -> list[int]:
    """Return unique values in first-seen order."""
    seen: set[int] = set()
    result: list[int] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def count_items(words: list[str]) -> dict[str, int]:
    """Count exact, case-sensitive strings."""
    return dict(Counter(words))


def top_k_frequent(values: list[int], k: int) -> list[int]:
    """Return the k most frequent values, breaking ties numerically."""
    counts = Counter(values)
    if not 0 <= k <= len(counts):
        raise ValueError("k must be between zero and the number of distinct values")
    return sorted(counts, key=lambda value: (-counts[value], value))[:k]


def fizz_buzz(n: int) -> list[str]:
    """Return FizzBuzz labels from one through n."""
    results: list[str] = []
    for value in range(1, n + 1):
        if value % 15 == 0:
            results.append("FizzBuzz")
        elif value % 3 == 0:
            results.append("Fizz")
        elif value % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(value))
    return results


def letter_grade(score: int) -> str:
    """Convert an integer score from zero through one hundred to a letter."""
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def count_runs(text: str) -> int:
    """Count consecutive runs of identical characters."""
    if not text:
        return 0
    return 1 + sum(current != previous for previous, current in zip(text, text[1:]))


class BankAccount:
    """A simple non-overdraft bank account."""

    def __init__(self, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("initial balance must not be negative")
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount


class ShoppingCart:
    """Store item prices and quantities and calculate the cart total."""

    def __init__(self) -> None:
        self._items: dict[str, tuple[float, int]] = {}

    def add(self, name: str, unit_price: float, quantity: int = 1) -> None:
        if not name.strip():
            raise ValueError("name must not be empty")
        if unit_price < 0:
            raise ValueError("unit_price must not be negative")
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if name in self._items:
            existing_price, existing_quantity = self._items[name]
            if existing_price != unit_price:
                raise ValueError("an item's unit price cannot change")
            quantity += existing_quantity
        self._items[name] = (unit_price, quantity)

    def total(self) -> float:
        return sum(price * quantity for price, quantity in self._items.values())


def _check() -> None:
    assert format_duration(0) == "00:00:00"
    assert format_duration(3661) == "01:01:01"
    assert format_duration(90061) == "25:01:01"
    assert calculate_tip(50.00, 18) == 9.0
    assert calculate_tip(19.99, 15) == 3.0
    assert unique_in_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert unique_in_order([]) == []
    assert count_items(["tea", "Tea", "tea"]) == {"tea": 2, "Tea": 1}
    assert top_k_frequent([4, 4, 2, 2, 9], 2) == [2, 4]
    assert top_k_frequent([1, 1], 0) == []
    assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizz_buzz(0) == []
    assert letter_grade(90) == "A"
    assert letter_grade(59) == "F"
    assert count_runs("aaabbca") == 4
    assert count_runs("") == 0
    account = BankAccount(100)
    account.deposit(25)
    assert account.balance == 125
    account.withdraw(25)
    assert account.balance == 100
    cart = ShoppingCart()
    cart.add("book", 12.50, 2)
    cart.add("pen", 1.50)
    assert cart.total() == 26.5


if __name__ == "__main__":
    _check()
    print("OK")
