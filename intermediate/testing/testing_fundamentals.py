#!/usr/bin/env python3
"""
Python Testing Fundamentals: unittest, pytest, TDD

This file demonstrates comprehensive testing in Python:
- unittest framework basics
- pytest framework and features
- Test-driven development (TDD)
- Mocking and fixtures
- Test organization and best practices
- Code coverage and reporting
"""

import unittest
import pytest
from unittest.mock import Mock, patch, MagicMock
import tempfile
import os
import json
from typing import List, Dict, Any, Optional
import math

# UNITTEST FRAMEWORK BASICS
print("=== UNITTEST FRAMEWORK BASICS ===")

class Calculator:
    """Simple calculator class for testing examples."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def factorial(self, n: int) -> int:
        """Calculate factorial."""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class using unittest."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
        print(f"Setting up test for {self._testMethodName}")

    def tearDown(self):
        """Clean up after each test method."""
        print(f"Tearing down test for {self._testMethodName}")

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures once for all tests."""
        print("Setting up TestCalculator class")
        cls.shared_calc = Calculator()

    @classmethod
    def tearDownClass(cls):
        """Clean up class-level fixtures once after all tests."""
        print("Tearing down TestCalculator class")

    # Basic assertion tests
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_mixed_numbers(self):
        """Test addition of positive and negative numbers."""
        result = self.calc.add(5, -3)
        self.assertEqual(result, 2)

    def test_subtract(self):
        """Test subtraction."""
        result = self.calc.subtract(10, 3)
        self.assertEqual(result, 7)

    def test_multiply(self):
        """Test multiplication."""
        result = self.calc.multiply(4, 5)
        self.assertEqual(result, 20)

    def test_divide(self):
        """Test division."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_factorial_zero(self):
        """Test factorial of zero."""
        result = self.calc.factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_positive(self):
        """Test factorial of positive numbers."""
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(10), 3628800)

    def test_factorial_negative(self):
        """Test factorial of negative numbers raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)

    # Assertion methods demonstration
    def test_assertion_methods(self):
        """Demonstrate various assertion methods."""
        # assertEqual
        self.assertEqual(1 + 1, 2)

        # assertNotEqual
        self.assertNotEqual(1 + 1, 3)

        # assertTrue/assertFalse
        self.assertTrue(5 > 3)
        self.assertFalse(3 > 5)

        # assertIs/assertIsNot
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        self.assertIs(a, b)  # Same object
        self.assertIsNot(a, c)  # Different objects, same content

        # assertIn/assertNotIn
        my_list = [1, 2, 3, 4, 5]
        self.assertIn(3, my_list)
        self.assertNotIn(6, my_list)

        # assertIsInstance
        self.assertIsInstance("hello", str)
        self.assertIsInstance(42, int)

        # assertAlmostEqual (for floating point comparisons)
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)

        # assertRaises context manager
        with self.assertRaises(ZeroDivisionError):
            1 / 0

    def test_skip_example(self):
        """Example of skipping a test."""
        if True:  # Some condition
            self.skipTest("Skipping this test for demonstration")

    @unittest.expectedFailure
    def test_expected_failure(self):
        """Test that is expected to fail."""
        self.assertEqual(1 + 1, 3)  # This will fail but is expected

# PYTEST FRAMEWORK
print("\n=== PYTEST FRAMEWORK ===")

# pytest examples (these would typically be in separate files)
def test_calculator_add():
    """Test calculator addition with pytest."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_calculator_subtract():
    """Test calculator subtraction with pytest."""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2

def test_calculator_multiply():
    """Test calculator multiplication with pytest."""
    calc = Calculator()
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(-2, 3) == -6

def test_calculator_divide():
    """Test calculator division with pytest."""
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(7, 2) == 3.5

def test_calculator_divide_by_zero():
    """Test calculator division by zero with pytest."""
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)

# Parametrized tests with pytest
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_calculator_add_parametrized(a, b, expected):
    """Parametrized test for addition."""
    calc = Calculator()
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (10, 3628800),
])
def test_factorial_parametrized(n, expected):
    """Parametrized test for factorial."""
    calc = Calculator()
    assert calc.factorial(n) == expected

# Fixtures in pytest
@pytest.fixture
def calculator():
    """Fixture that provides a Calculator instance."""
    return Calculator()

@pytest.fixture
def sample_data():
    """Fixture that provides sample test data."""
    return {
        "numbers": [1, 2, 3, 4, 5],
        "expected_sum": 15,
        "expected_product": 120
    }

def test_calculator_with_fixture(calculator):
    """Test using calculator fixture."""
    assert calculator.add(2, 3) == 5
    assert calculator.multiply(4, 5) == 20

def test_data_processing_with_fixture(sample_data):
    """Test using sample data fixture."""
    numbers = sample_data["numbers"]
    assert sum(numbers) == sample_data["expected_sum"]
    assert math.prod(numbers) == sample_data["expected_product"]

# MOCKING AND PATCHING
print("\n=== MOCKING AND PATCHING ===")

class DataFetcher:
    """Class that fetches data from external sources."""

    def __init__(self, api_url: str):
        self.api_url = api_url

    def fetch_user_data(self, user_id: int) -> Dict[str, Any]:
        """Fetch user data from API."""
        # In real code, this would make an HTTP request
        # For testing, we'll simulate it
        import requests
        response = requests.get(f"{self.api_url}/users/{user_id}")
        response.raise_for_status()
        return response.json()

    def process_user_data(self, user_id: int) -> str:
        """Process user data and return formatted string."""
        user_data = self.fetch_user_data(user_id)
        return f"User: {user_data['name']}, Age: {user_data['age']}"

def test_data_fetcher_with_mock():
    """Test DataFetcher using mocks."""
    # Create mock response
    mock_response = Mock()
    mock_response.json.return_value = {"name": "Alice", "age": 25}

    # Test the process_user_data method with mocked fetch
    fetcher = DataFetcher("https://api.example.com")

    with patch.object(fetcher, 'fetch_user_data', return_value={"name": "Alice", "age": 25}):
        result = fetcher.process_user_data(123)
        assert result == "User: Alice, Age: 25"

def test_data_fetcher_with_patch():
    """Test DataFetcher using patch decorator."""
    fetcher = DataFetcher("https://api.example.com")

    with patch('requests.get') as mock_get:
        # Configure the mock
        mock_response = Mock()
        mock_response.json.return_value = {"name": "Bob", "age": 30}
        mock_get.return_value = mock_response

        # Call the method
        result = fetcher.fetch_user_data(456)

        # Assertions
        assert result == {"name": "Bob", "age": 30}
        mock_get.assert_called_once_with("https://api.example.com/users/456")

# TEST-DRIVEN DEVELOPMENT (TDD) EXAMPLE
print("\n=== TEST-DRIVEN DEVELOPMENT EXAMPLE ===")

class StringProcessor:
    """String processing utility class - built with TDD approach."""

    def reverse_string(self, text: str) -> str:
        """Reverse a string."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        return text[::-1]

    def capitalize_words(self, text: str) -> str:
        """Capitalize first letter of each word."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        return text.title()

    def count_vowels(self, text: str) -> int:
        """Count vowels in a string."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char in vowels)

    def is_palindrome(self, text: str) -> bool:
        """Check if string is a palindrome."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        cleaned = ''.join(c.lower() for c in text if c.isalnum())
        return cleaned == cleaned[::-1]

# Tests for StringProcessor (following TDD approach)
def test_reverse_string():
    """Test string reversal."""
    processor = StringProcessor()

    assert processor.reverse_string("hello") == "olleh"
    assert processor.reverse_string("Python") == "nohtyP"
    assert processor.reverse_string("") == ""
    assert processor.reverse_string("a") == "a"

    # Test error cases
    with pytest.raises(TypeError):
        processor.reverse_string(123)

def test_capitalize_words():
    """Test word capitalization."""
    processor = StringProcessor()

    assert processor.capitalize_words("hello world") == "Hello World"
    assert processor.capitalize_words("python programming") == "Python Programming"
    assert processor.capitalize_words("a") == "A"
    assert processor.capitalize_words("") == ""

def test_count_vowels():
    """Test vowel counting."""
    processor = StringProcessor()

    assert processor.count_vowels("hello") == 2  # e, o
    assert processor.count_vowels("Python") == 1  # o
    assert processor.count_vowels("AEIOU") == 5
    assert processor.count_vowels("bcdfg") == 0
    assert processor.count_vowels("") == 0

def test_is_palindrome():
    """Test palindrome checking."""
    processor = StringProcessor()

    assert processor.is_palindrome("radar") == True
    assert processor.is_palindrome("A man a plan a canal Panama") == True
    assert processor.is_palindrome("hello") == False
    assert processor.is_palindrome("Python") == False
    assert processor.is_palindrome("") == True
    assert processor.is_palindrome("a") == True

# CODE COVERAGE AND BEST PRACTICES
print("\n=== CODE COVERAGE AND BEST PRACTICES ===")

def demonstrate_coverage():
    """Demonstrate code coverage concepts."""
    processor = StringProcessor()

    # These calls should achieve high coverage
    processor.reverse_string("test")
    processor.capitalize_words("test string")
    processor.count_vowels("testing")
    processor.is_palindrome("radar")

    # Test edge cases for better coverage
    processor.reverse_string("")
    processor.capitalize_words("")
    processor.count_vowels("")
    processor.is_palindrome("")

    print("Coverage demonstration completed")

# Test organization and structure
class TestSuite:
    """Example of organizing tests into suites."""

    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []

    def run_test(self, test_func, *args, **kwargs):
        """Run a single test."""
        try:
            test_func(*args, **kwargs)
            self.passed += 1
            print(f"✓ {test_func.__name__}")
        except Exception as e:
            self.failed += 1
            self.errors.append((test_func.__name__, str(e)))
            print(f"✗ {test_func.__name__}: {e}")

    def run_all_tests(self):
        """Run all tests in the suite."""
        print("Running test suite...")

        # Calculator tests
        calc = Calculator()
        self.run_test(lambda: assert calc.add(2, 3) == 5, "Calculator add")
        self.run_test(lambda: assert calc.subtract(5, 3) == 2, "Calculator subtract")
        self.run_test(lambda: assert calc.multiply(4, 5) == 20, "Calculator multiply")
        self.run_test(lambda: assert calc.divide(10, 2) == 5, "Calculator divide")

        # String processor tests
        processor = StringProcessor()
        self.run_test(lambda: assert processor.reverse_string("hello") == "olleh", "String reverse")
        self.run_test(lambda: assert processor.capitalize_words("hello world") == "Hello World", "String capitalize")
        self.run_test(lambda: assert processor.count_vowels("hello") == 2, "Vowel count")
        self.run_test(lambda: assert processor.is_palindrome("radar") == True, "Palindrome check")

        print(f"\nTest Results: {self.passed} passed, {self.failed} failed")
        if self.errors:
            print("Failed tests:")
            for test_name, error in self.errors:
                print(f"  - {test_name}: {error}")

# PRACTICAL TESTING SCENARIOS
print("\n=== PRACTICAL TESTING SCENARIOS ===")

class UserManager:
    """User management system for testing examples."""

    def __init__(self, data_file: str = "users.json"):
        self.data_file = data_file
        self.users = self._load_users()

    def _load_users(self) -> Dict[str, Dict[str, Any]]:
        """Load users from file."""
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save_users(self):
        """Save users to file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.users, f, indent=2)

    def create_user(self, username: str, email: str, age: int) -> bool:
        """Create a new user."""
        if username in self.users:
            return False

        if not isinstance(age, int) or age < 0 or age > 150:
            return False

        if "@" not in email:
            return False

        self.users[username] = {
            "email": email,
            "age": age,
            "created_at": "2025-01-01"  # Would use datetime in real code
        }
        self._save_users()
        return True

    def get_user(self, username: str) -> Optional[Dict[str, Any]]:
        """Get user by username."""
        return self.users.get(username)

    def update_user(self, username: str, **updates) -> bool:
        """Update user information."""
        if username not in self.users:
            return False

        user = self.users[username]

        # Validate updates
        if "age" in updates and (not isinstance(updates["age"], int) or updates["age"] < 0):
            return False

        if "email" in updates and "@" not in updates["email"]:
            return False

        user.update(updates)
        self._save_users()
        return True

    def delete_user(self, username: str) -> bool:
        """Delete a user."""
        if username not in self.users:
            return False

        del self.users[username]
        self._save_users()
        return True

# Tests for UserManager
def test_user_manager():
    """Test UserManager with temporary files."""

    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name

    try:
        # Test user manager
        manager = UserManager(temp_file)

        # Test creating users
        assert manager.create_user("alice", "alice@example.com", 25) == True
        assert manager.create_user("bob", "bob@example.com", 30) == True
        assert manager.create_user("alice", "alice2@example.com", 26) == False  # Duplicate

        # Test getting users
        alice = manager.get_user("alice")
        assert alice is not None
        assert alice["email"] == "alice@example.com"
        assert alice["age"] == 25

        # Test updating users
        assert manager.update_user("alice", age=26, email="alice_updated@example.com") == True
        alice_updated = manager.get_user("alice")
        assert alice_updated["age"] == 26
        assert alice_updated["email"] == "alice_updated@example.com"

        # Test deleting users
        assert manager.delete_user("bob") == True
        assert manager.get_user("bob") is None
        assert manager.delete_user("nonexistent") == False

        print("UserManager tests passed!")

    finally:
        # Clean up
        if os.path.exists(temp_file):
            os.unlink(temp_file)

# RUN DEMONSTRATIONS
if __name__ == "__main__":
    print("Python Testing Fundamentals Demo")
    print("=" * 50)

    # Run unittest tests
    print("Running unittest tests...")
    unittest.main(argv=[''], exit=False, verbosity=2)

    print("\n" + "=" * 50)

    # Run pytest-style tests
    print("Running pytest-style tests...")

    # Basic calculator tests
    test_calculator_add()
    test_calculator_subtract()
    test_calculator_multiply()
    test_calculator_divide()
    test_calculator_divide_by_zero()

    # Parametrized tests
    test_calculator_add_parametrized(2, 3, 5)
    test_factorial_parametrized(5, 120)

    # String processor tests
    test_reverse_string()
    test_capitalize_words()
    test_count_vowels()
    test_is_palindrome()

    # Mocking tests
    test_data_fetcher_with_mock()
    test_data_fetcher_with_patch()

    # Coverage demonstration
    demonstrate_coverage()

    # Test suite
    suite = TestSuite()
    suite.run_all_tests()

    # Practical tests
    test_user_manager()

    print("\n" + "=" * 60)
    print("Testing fundamentals demonstration completed!")
    print("All tests demonstrate proper testing practices and patterns.")
    print("=" * 60)
