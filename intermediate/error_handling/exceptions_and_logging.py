#!/usr/bin/env python3
"""
Python Error Handling Mastery: Exceptions, Logging, Debugging

This file demonstrates comprehensive error handling in Python:
- Exception types and hierarchy
- Try/except/else/finally blocks
- Custom exceptions
- Logging with different levels
- Debugging techniques
- Best practices for robust code
"""

import sys
import os
import logging
import logging.handlers
from typing import Optional, Dict, Any, List
import json
import time
from functools import wraps

# BASIC EXCEPTION HANDLING
print("=== BASIC EXCEPTION HANDLING ===")

# Common exception types
def demonstrate_basic_exceptions():
    """Demonstrate basic exception handling patterns."""

    # ZeroDivisionError
    try:
        result = 10 / 0
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    # ValueError
    try:
        number = int("not_a_number")
        print(f"Number: {number}")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    # TypeError
    try:
        result = "string" + 5
        print(f"Result: {result}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")

    # IndexError
    try:
        my_list = [1, 2, 3]
        value = my_list[10]
        print(f"Value: {value}")
    except IndexError as e:
        print(f"Caught IndexError: {e}")

    # KeyError
    try:
        my_dict = {"a": 1, "b": 2}
        value = my_dict["c"]
        print(f"Value: {value}")
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    # FileNotFoundError
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
            print(f"Content: {content}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

# TRY/EXCEPT/ELSE/FINALLY BLOCKS
print("\n=== TRY/EXCEPT/ELSE/FINALLY BLOCKS ===")

def comprehensive_exception_handling():
    """Demonstrate complete exception handling structure."""

    def divide_numbers(a, b):
        """Divide two numbers with comprehensive error handling."""
        try:
            # Code that might raise exceptions
            result = a / b
            print(f"Division successful: {a} / {b} = {result}")
            return result

        except ZeroDivisionError as e:
            print(f"Error: Cannot divide by zero - {e}")
            return None

        except TypeError as e:
            print(f"Error: Invalid types for division - {e}")
            return None

        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"Unexpected error: {e}")
            return None

        else:
            # Executed only if no exception occurred
            print("Division completed without errors")
            return result

        finally:
            # Always executed, regardless of exceptions
            print("Division operation finished (finally block)")

    # Test the function
    print("Testing divide_numbers function:")
    divide_numbers(10, 2)  # Success
    print()
    divide_numbers(10, 0)  # ZeroDivisionError
    print()
    divide_numbers("10", 2)  # TypeError

# CUSTOM EXCEPTIONS
print("\n=== CUSTOM EXCEPTIONS ===")

class ValidationError(Exception):
    """Custom exception for validation errors."""

    def __init__(self, field: str, value: Any, message: str = ""):
        self.field = field
        self.value = value
        self.message = message or f"Invalid value for field '{field}': {value}"
        super().__init__(self.message)

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""

    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        message = f"Insufficient funds. Balance: ${balance:.2f}, Required: ${amount:.2f}"
        super().__init__(message)

class UserNotFoundError(Exception):
    """Custom exception for user not found."""

    def __init__(self, user_id: str):
        self.user_id = user_id
        message = f"User with ID '{user_id}' not found"
        super().__init__(message)

def validate_user_data(user_data: Dict[str, Any]) -> None:
    """Validate user data and raise custom exceptions."""
    required_fields = ["name", "email", "age"]

    # Check required fields
    for field in required_fields:
        if field not in user_data:
            raise ValidationError(field, None, f"Missing required field: {field}")

    # Validate name
    name = user_data["name"]
    if not isinstance(name, str) or len(name.strip()) < 2:
        raise ValidationError("name", name, "Name must be a string with at least 2 characters")

    # Validate email
    email = user_data["email"]
    if not isinstance(email, str) or "@" not in email:
        raise ValidationError("email", email, "Email must be a valid email address")

    # Validate age
    age = user_data["age"]
    if not isinstance(age, int) or age < 0 or age > 150:
        raise ValidationError("age", age, "Age must be an integer between 0 and 150")

class BankAccount:
    """Bank account with custom exception handling."""

    def __init__(self, account_id: str, initial_balance: float = 0):
        self.account_id = account_id
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """Deposit money into account."""
        if amount <= 0:
            raise ValidationError("amount", amount, "Deposit amount must be positive")

        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        """Withdraw money from account."""
        if amount <= 0:
            raise ValidationError("amount", amount, "Withdrawal amount must be positive")

        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)

        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

def test_custom_exceptions():
    """Test custom exception handling."""
    print("Testing custom exceptions:")

    # Test validation errors
    try:
        validate_user_data({"name": "", "email": "invalid", "age": -5})
    except ValidationError as e:
        print(f"Validation error: {e}")

    # Test bank account
    account = BankAccount("12345", 1000)

    try:
        account.deposit(500)
        account.withdraw(200)
        account.withdraw(2000)  # This should fail
    except (ValidationError, InsufficientFundsError) as e:
        print(f"Bank error: {e}")

    try:
        account.deposit(-100)  # This should fail
    except ValidationError as e:
        print(f"Deposit error: {e}")

# EXCEPTION HIERARCHY AND INHERITANCE
print("\n=== EXCEPTION HIERARCHY ===")

def demonstrate_exception_hierarchy():
    """Show Python's exception hierarchy."""

    # BaseException is the root of all exceptions
    # Exception is the base for user-defined exceptions

    print("Python Exception Hierarchy:")
    print("BaseException")
    print("├── SystemExit")
    print("├── KeyboardInterrupt")
    print("├── GeneratorExit")
    print("└── Exception")
    print("    ├── ArithmeticError")
    print("    │   ├── ZeroDivisionError")
    print("    │   └── OverflowError")
    print("    ├── LookupError")
    print("    │   ├── IndexError")
    print("    │   └── KeyError")
    print("    ├── ValueError")
    print("    │   ├── UnicodeError")
    print("    │   └── TypeError")
    print("    ├── OSError")
    print("    │   └── FileNotFoundError")
    print("    └── Custom exceptions...")

    # Multiple exception handling
    def handle_multiple_exceptions():
        """Handle multiple exception types."""
        exceptions_to_test = [
            ("ZeroDivisionError", lambda: 1 / 0),
            ("ValueError", lambda: int("abc")),
            ("TypeError", lambda: "string" + 123),
            ("IndexError", lambda: [1, 2, 3][10]),
            ("KeyError", lambda: {"a": 1}["b"]),
        ]

        for exception_name, func in exceptions_to_test:
            try:
                result = func()
                print(f"{exception_name}: No exception raised")
            except ZeroDivisionError:
                print(f"{exception_name}: Caught as ZeroDivisionError")
            except ValueError:
                print(f"{exception_name}: Caught as ValueError")
            except TypeError:
                print(f"{exception_name}: Caught as TypeError")
            except LookupError:  # Parent class for IndexError and KeyError
                print(f"{exception_name}: Caught as LookupError")
            except Exception as e:
                print(f"{exception_name}: Caught as {type(e).__name__}: {e}")

    handle_multiple_exceptions()

# LOGGING SYSTEM
print("\n=== LOGGING SYSTEM ===")

def setup_logging():
    """Set up comprehensive logging configuration."""

    # Create logger
    logger = logging.getLogger('python_mastery')
    logger.setLevel(logging.DEBUG)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create file handler
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)

    # Create rotating file handler (for production)
    rotating_handler = logging.handlers.RotatingFileHandler(
        'app_rotating.log',
        maxBytes=1024*1024,  # 1MB
        backupCount=5
    )
    rotating_handler.setLevel(logging.WARNING)

    # Create formatter
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    )
    simple_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )

    # Set formatters
    console_handler.setFormatter(simple_formatter)
    file_handler.setFormatter(detailed_formatter)
    rotating_handler.setFormatter(detailed_formatter)

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(rotating_handler)

    return logger

def demonstrate_logging():
    """Demonstrate different logging levels and features."""

    logger = setup_logging()

    logger.debug("This is a debug message (detailed info)")
    logger.info("This is an info message (general info)")
    logger.warning("This is a warning message (potential problem)")
    logger.error("This is an error message (serious problem)")
    logger.critical("This is a critical message (system failure)")

    # Logging with extra context
    user_id = "user123"
    action = "login"

    logger.info(f"User {user_id} performed action: {action}")
    logger.info("User action", extra={"user_id": user_id, "action": action})

    # Logging exceptions
    try:
        result = 1 / 0
    except ZeroDivisionError:
        logger.exception("An error occurred while performing division")

    # Conditional logging
    data_size = 1500
    if data_size > 1000:
        logger.warning(f"Large data size detected: {data_size} items")

    print("Logging demonstration completed. Check app.log and console output.")

# DECORATOR FOR ERROR HANDLING
print("\n=== ERROR HANDLING DECORATOR ===")

def handle_exceptions(*exception_types):
    """Decorator to handle exceptions in functions."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_types as e:
                logger = logging.getLogger('python_mastery')
                logger.error(f"Exception in {func.__name__}: {e}")
                return None
            except Exception as e:
                logger = logging.getLogger('python_mastery')
                logger.critical(f"Unexpected error in {func.__name__}: {e}")
                raise  # Re-raise unexpected exceptions
        return wrapper
    return decorator

@handle_exceptions(ValueError, TypeError)
def risky_function(x, y):
    """A function that might raise exceptions."""
    if x == 0:
        raise ValueError("x cannot be zero")
    if not isinstance(y, (int, float)):
        raise TypeError("y must be a number")

    return x / y

def test_error_decorator():
    """Test the error handling decorator."""
    print("Testing error handling decorator:")

    # These should be handled gracefully
    result1 = risky_function(0, 5)  # ValueError
    result2 = risky_function(10, "abc")  # TypeError

    # This should work normally
    result3 = risky_function(10, 2)  # Success

    print(f"Result 1 (should be None): {result1}")
    print(f"Result 2 (should be None): {result2}")
    print(f"Result 3 (should be 5.0): {result3}")

# PRACTICAL APPLICATIONS
print("\n=== PRACTICAL APPLICATIONS ===")

class DataProcessor:
    """Data processing class with comprehensive error handling and logging."""

    def __init__(self):
        self.logger = logging.getLogger('data_processor')
        self.processed_count = 0
        self.error_count = 0

    def load_json_file(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load data from JSON file with error handling."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.logger.info(f"Successfully loaded JSON from {filename}")
                return data
        except FileNotFoundError:
            self.logger.error(f"JSON file not found: {filename}")
            self.error_count += 1
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in {filename}: {e}")
            self.error_count += 1
        except Exception as e:
            self.logger.critical(f"Unexpected error loading {filename}: {e}")
            self.error_count += 1

        return None

    def validate_data(self, data: Dict[str, Any]) -> bool:
        """Validate data structure."""
        required_fields = ["name", "age", "email"]

        try:
            for field in required_fields:
                if field not in data:
                    raise ValidationError(field, None, f"Missing required field: {field}")

                if field == "age" and not isinstance(data[field], int):
                    raise ValidationError(field, data[field], "Age must be an integer")

                if field == "email" and "@" not in str(data[field]):
                    raise ValidationError(field, data[field], "Invalid email format")

            return True

        except ValidationError as e:
            self.logger.warning(f"Data validation failed: {e}")
            self.error_count += 1
            return False

    def process_user_data(self, user_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Process user data with comprehensive error handling."""
        try:
            # Validate data
            if not self.validate_data(user_data):
                return None

            # Process data
            processed_data = {
                "full_name": user_data["name"].title(),
                "age_category": "adult" if user_data["age"] >= 18 else "minor",
                "email_domain": user_data["email"].split("@")[1] if "@" in user_data["email"] else "unknown",
                "processed_at": time.time()
            }

            self.processed_count += 1
            self.logger.info(f"Successfully processed user: {user_data['name']}")

            return processed_data

        except KeyError as e:
            self.logger.error(f"Missing key in user data: {e}")
            self.error_count += 1
        except Exception as e:
            self.logger.critical(f"Unexpected error processing user data: {e}")
            self.error_count += 1

        return None

    def get_statistics(self) -> Dict[str, Any]:
        """Get processing statistics."""
        return {
            "processed": self.processed_count,
            "errors": self.error_count,
            "success_rate": (self.processed_count / max(self.processed_count + self.error_count, 1)) * 100
        }

def demonstrate_data_processor():
    """Demonstrate the data processor with various scenarios."""
    processor = DataProcessor()

    # Test data
    test_users = [
        {"name": "Alice Johnson", "age": 25, "email": "alice@example.com"},
        {"name": "Bob", "age": "invalid", "email": "bob@example.com"},  # Invalid age
        {"name": "Charlie", "email": "charlie@example.com"},  # Missing age
        {"name": "Diana", "age": 30, "email": "invalid-email"},  # Invalid email
    ]

    print("Processing user data:")
    for user in test_users:
        result = processor.process_user_data(user)
        if result:
            print(f"✓ Processed {user['name']}: {result['age_category']}")
        else:
            print(f"✗ Failed to process {user.get('name', 'unknown')}")

    # Show statistics
    stats = processor.get_statistics()
    print("
Processing statistics:")
    print(f"Successfully processed: {stats['processed']}")
    print(f"Errors encountered: {stats['errors']}")
    print(".1f")
# RUN DEMONSTRATIONS
if __name__ == "__main__":
    print("Python Error Handling and Logging Mastery Demo")
    print("=" * 60)

    # Basic exception handling
    demonstrate_basic_exceptions()

    # Comprehensive exception handling
    comprehensive_exception_handling()

    # Custom exceptions
    test_custom_exceptions()

    # Exception hierarchy
    demonstrate_exception_hierarchy()

    # Logging setup and demonstration
    demonstrate_logging()

    # Error handling decorator
    test_error_decorator()

    # Practical data processor
    demonstrate_data_processor()

    print("\n" + "=" * 60)
    print("Error handling demonstration completed!")
    print("Check the generated log files for detailed logging output.")
    print("=" * 60)
