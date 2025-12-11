#!/usr/bin/env python3
"""
Python Decorators Mastery: Advanced Function and Class Decorators

This file demonstrates advanced decorator patterns in Python:
- Function decorators with and without parameters
- Class decorators
- Multiple decorators and decorator chaining
- Decorators for method wrapping
- Property decorators and descriptors
- Real-world decorator applications
"""

import time
import functools
from typing import Callable, Any, TypeVar, Generic, Optional, Dict, List
import logging

# BASIC FUNCTION DECORATORS
print("=== BASIC FUNCTION DECORATORS ===")

def simple_timer(func: Callable) -> Callable:
    """Basic timer decorator without functools.wraps."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def timer_with_wraps(func: Callable) -> Callable:
    """Timer decorator with proper metadata preservation."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@simple_timer
def slow_function_without_wraps():
    """Function decorated with simple timer."""
    time.sleep(0.1)
    return "Done without wraps"

@timer_with_wraps
def slow_function_with_wraps():
    """Function decorated with proper timer."""
    time.sleep(0.1)
    return "Done with wraps"

print("Function metadata comparison:")
print(f"Without wraps - Name: {slow_function_without_wraps.__name__}")
print(f"With wraps - Name: {slow_function_with_wraps.__name__}")

# DECORATORS WITH PARAMETERS
print("\n=== DECORATORS WITH PARAMETERS ===")

def retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator that retries a function on failure."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                        time.sleep(delay)
                    else:
                        print(f"All {max_attempts} attempts failed.")

            # If we get here, all attempts failed
            if last_exception:
                raise last_exception
            else:
                raise Exception("Function failed after all retry attempts")
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    """Function that fails randomly."""
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"

def cache_with_ttl(max_size: int = 128, ttl: float = 300):
    """Decorator that caches function results with time-to-live."""
    cache = {}

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key
            key = str(args) + str(sorted(kwargs.items()))

            # Check if result is cached and not expired
            current_time = time.time()
            if key in cache:
                cached_time, cached_result = cache[key]
                if current_time - cached_time < ttl:
                    print(f"Cache hit for {func.__name__}")
                    return cached_result
                else:
                    # Remove expired entry
                    del cache[key]

            # Compute result
            result = func(*args, **kwargs)

            # Cache result (keep only max_size entries)
            if len(cache) >= max_size:
                # Remove oldest entry (simple strategy)
                oldest_key = min(cache.keys(), key=lambda k: cache[k][0])
                del cache[oldest_key]

            cache[key] = (current_time, result)
            print(f"Computed and cached result for {func.__name__}")
            return result

        return wrapper
    return decorator

@cache_with_ttl(max_size=5, ttl=10)
def expensive_computation(n: int) -> int:
    """Simulate expensive computation."""
    time.sleep(0.1)  # Simulate work
    return sum(i**2 for i in range(n))

# CLASS DECORATORS
print("\n=== CLASS DECORATORS ===")

def add_method(cls):
    """Class decorator that adds a method to a class."""
    def new_method(self):
        return f"This is a new method added to {self.__class__.__name__}"

    cls.added_method = new_method
    return cls

def singleton(cls):
    """Singleton class decorator."""
    instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

def dataclass_with_validation(cls):
    """Class decorator that adds validation to dataclass-like behavior."""
    original_init = cls.__init__

    def validated_init(self, *args, **kwargs):
        # Call original init
        original_init(self, *args, **kwargs)

        # Validate attributes
        for attr_name, attr_value in self.__dict__.items():
            if hasattr(cls, f'_validate_{attr_name}'):
                validator = getattr(cls, f'_validate_{attr_name}')
                if not validator(attr_value):
                    raise ValueError(f"Invalid value for {attr_name}: {attr_value}")

    cls.__init__ = validated_init
    return cls

@add_method
class SimpleClass:
    """A simple class that will get an additional method."""
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

@singleton
class DatabaseConnection:
    """Singleton database connection."""
    def __init__(self, connection_string):
        self.connection_string = connection_string
        print(f"Creating database connection: {connection_string}")

@dataclass_with_validation
class User:
    """User class with validation."""
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    @staticmethod
    def _validate_name(name):
        return isinstance(name, str) and len(name.strip()) >= 2

    @staticmethod
    def _validate_email(email):
        return isinstance(email, str) and '@' in email

    @staticmethod
    def _validate_age(age):
        return isinstance(age, int) and 0 <= age <= 150

# MULTIPLE DECORATORS AND CHAINING
print("\n=== MULTIPLE DECORATORS AND CHAINING ===")

def uppercase_result(func: Callable) -> Callable:
    """Decorator that uppercases the result if it's a string."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

def add_prefix(prefix: str):
    """Parameterized decorator that adds a prefix."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix}{result}"
        return wrapper
    return decorator

@add_prefix(">>> ")
@uppercase_result
@timer_with_wraps
def get_message(name: str) -> str:
    """Function with multiple decorators."""
    time.sleep(0.05)  # Simulate some work
    return f"hello {name}"

# Decorator order matters!
@uppercase_result
@add_prefix(">>> ")
@timer_with_wraps
def get_message_different_order(name: str) -> str:
    """Same function with different decorator order."""
    time.sleep(0.05)
    return f"hello {name}"

# METHOD DECORATORS
print("\n=== METHOD DECORATORS ===")

class BankAccount:
    """Bank account with decorated methods."""

    def __init__(self, balance: float = 0):
        self._balance = balance
        self._transaction_log = []

    def log_transaction(method):
        """Method decorator that logs transactions."""
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            # Get method name and arguments for logging
            method_name = method.__name__
            args_str = ', '.join(str(arg) for arg in args[1:])  # Skip self

            # Call the method
            result = method(self, *args, **kwargs)

            # Log the transaction
            log_entry = f"{method_name}({args_str}) -> {result}"
            self._transaction_log.append(log_entry)
            print(f"Transaction logged: {log_entry}")

            return result
        return wrapper

    @log_transaction
    def deposit(self, amount: float) -> float:
        """Deposit money."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        return self._balance

    @log_transaction
    def withdraw(self, amount: float) -> float:
        """Withdraw money."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance

    def get_balance(self) -> float:
        """Get current balance."""
        return self._balance

    def get_transaction_log(self) -> List[str]:
        """Get transaction log."""
        return self._transaction_log.copy()

# PROPERTY DECORATORS AND DESCRIPTORS
print("\n=== PROPERTY DECORATORS AND DESCRIPTORS ===")

class Temperature:
    """Temperature class with property decorators."""

    def __init__(self, celsius: float = 0):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """Get temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Set temperature in Celsius."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Get temperature in Fahrenheit."""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """Set temperature in Fahrenheit."""
        self._celsius = (value - 32) * 5/9

    @property
    def kelvin(self) -> float:
        """Get temperature in Kelvin."""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float) -> None:
        """Set temperature in Kelvin."""
        self._celsius = value - 273.15

class ValidatedAttribute:
    """Descriptor for validated attributes."""

    def __init__(self, validator=None):
        self.validator = validator
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        if self.validator and not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        instance.__dict__[self.name] = value

def validate_positive(value):
    """Validator for positive numbers."""
    return isinstance(value, (int, float)) and value > 0

def validate_email(value):
    """Validator for email addresses."""
    return isinstance(value, str) and '@' in value and '.' in value

class Person:
    """Person class using descriptors for validation."""

    name = ValidatedAttribute()  # No validator, any value allowed
    age = ValidatedAttribute(validate_positive)
    height = ValidatedAttribute(validate_positive)
    email = ValidatedAttribute(validate_email)

    def __init__(self, name, age, height, email):
        self.name = name
        self.age = age
        self.height = height
        self.email = email

# ADVANCED DECORATOR PATTERNS
print("\n=== ADVANCED DECORATOR PATTERNS ===")

# Decorator factory for conditional decoration
def conditional_decorator(condition_func):
    """Decorator that applies another decorator conditionally."""
    def decorator(decorator_func):
        def conditional_wrapper(func):
            if condition_func():
                return decorator_func(func)
            return func
        return conditional_wrapper
    return decorator

def debug_enabled():
    """Check if debug mode is enabled."""
    return True  # Could check environment variable

@conditional_decorator(debug_enabled)
@timer_with_wraps
def some_function():
    """Function that may or may not be timed."""
    time.sleep(0.05)
    return "Function result"

# Context-aware decorators
class ContextAwareDecorator:
    """Decorator that adapts based on context."""

    def __init__(self, func):
        self.func = func
        self.call_count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.call_count += 1

        # Different behavior based on call count
        if self.call_count % 5 == 0:
            print(f"🎉 Call #{self.call_count} - Special milestone!")
        elif self.call_count % 3 == 0:
            print(f"⭐ Call #{self.call_count} - Triple milestone!")
        else:
            print(f"📞 Call #{self.call_count}")

        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()

        print(f"⏱️  Execution time: {end_time - start_time:.4f}s")
        return result

@ContextAwareDecorator
def milestone_function():
    """Function that celebrates milestones."""
    time.sleep(0.02)
    return "Milestone achieved!"

# Decorator for caching with different strategies
class Cache:
    """Advanced caching decorator with multiple strategies."""

    def __init__(self, strategy='lru', max_size=128):
        self.strategy = strategy
        self.max_size = max_size
        self.cache = {}
        self.access_order = []  # For LRU

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(sorted(kwargs.items()))

            if key in self.cache:
                if self.strategy == 'lru':
                    # Move to end (most recently used)
                    self.access_order.remove(key)
                    self.access_order.append(key)
                return self.cache[key]

            # Compute result
            result = func(*args, **kwargs)

            # Add to cache
            if len(self.cache) >= self.max_size:
                if self.strategy == 'lru':
                    # Remove least recently used
                    lru_key = self.access_order.pop(0)
                    del self.cache[lru_key]
                elif self.strategy == 'fifo':
                    # Remove first item
                    del self.cache[next(iter(self.cache))]

            self.cache[key] = result
            if self.strategy == 'lru':
                self.access_order.append(key)

            return result

        return wrapper

@Cache(strategy='lru', max_size=3)
def fibonacci_lru(n):
    """Fibonacci with LRU cache."""
    if n < 2:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)

@Cache(strategy='fifo', max_size=3)
def fibonacci_fifo(n):
    """Fibonacci with FIFO cache."""
    if n < 2:
        return n
    return fibonacci_fifo(n-1) + fibonacci_fifo(n-2)

# PRACTICAL APPLICATIONS
print("\n=== PRACTICAL APPLICATIONS ===")

# Authentication decorator
def require_auth(roles=None):
    """Decorator that requires authentication and role checking."""
    if roles is None:
        roles = []

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Simulate authentication check
            user_authenticated = True  # Would check session/token
            user_roles = ['user', 'admin']  # Would get from session

            if not user_authenticated:
                raise PermissionError("Authentication required")

            if roles and not any(role in user_roles for role in roles):
                raise PermissionError(f"Required roles: {roles}, user has: {user_roles}")

            # Log the access
            print(f"🔐 Authorized access to {func.__name__} by user with roles: {user_roles}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

class SecureAPI:
    """API class with authentication decorators."""

    @require_auth()
    def get_public_data(self):
        """Public endpoint."""
        return {"data": "This is public data"}

    @require_auth(roles=['user'])
    def get_user_data(self, user_id):
        """User-only endpoint."""
        return {"user_id": user_id, "data": "User-specific data"}

    @require_auth(roles=['admin'])
    def get_admin_data(self):
        """Admin-only endpoint."""
        return {"data": "Sensitive admin data"}

# Rate limiting decorator
class RateLimiter:
    """Rate limiting decorator."""

    def __init__(self, calls_per_minute=60):
        self.calls_per_minute = calls_per_minute
        self.calls = []

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()

            # Remove old calls
            self.calls = [call_time for call_time in self.calls
                         if current_time - call_time < 60]

            if len(self.calls) >= self.calls_per_minute:
                wait_time = 60 - (current_time - self.calls[0])
                raise Exception(f"Rate limit exceeded. Wait {wait_time:.1f} seconds")

            self.calls.append(current_time)
            return func(*args, **kwargs)

        return wrapper

@RateLimiter(calls_per_minute=3)
def api_call():
    """Simulated API call with rate limiting."""
    return f"API response at {time.strftime('%H:%M:%S')}"

# DEMONSTRATION
if __name__ == "__main__":
    print("Python Decorators Mastery Demo")
    print("=" * 50)

    # Basic decorators
    print("Testing basic decorators:")
    slow_function_without_wraps()
    slow_function_with_wraps()

    # Decorators with parameters
    print("\nTesting retry decorator:")
    try:
        unreliable_function()
    except ValueError:
        print("All retry attempts failed")

    print("\nTesting caching decorator:")
    print(f"First call: {expensive_computation(1000)}")
    print(f"Cached call: {expensive_computation(1000)}")

    # Class decorators
    print("\nTesting class decorators:")
    obj = SimpleClass("test")
    print(f"Simple class method: {obj.added_method()}")

    conn1 = DatabaseConnection("db://localhost:5432/mydb")
    conn2 = DatabaseConnection("db://localhost:5432/mydb")
    print(f"Singleton works: {conn1 is conn2}")

    try:
        user = User("Alice", "alice@example.com", 25)
        print(f"Validated user: {user.name}")
    except ValueError as e:
        print(f"Validation error: {e}")

    # Multiple decorators
    print("\nTesting multiple decorators:")
    result1 = get_message("Alice")
    result2 = get_message_different_order("Bob")
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")

    # Method decorators
    print("\nTesting method decorators:")
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Balance: ${account.get_balance()}")
    print("Transaction log:")
    for transaction in account.get_transaction_log():
        print(f"  {transaction}")

    # Property decorators
    print("\nTesting property decorators:")
    temp = Temperature(20)
    print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F = {temp.kelvin}K")

    temp.fahrenheit = 68
    print(f"After setting Fahrenheit to 68: {temp.celsius}°C")

    # Descriptors
    print("\nTesting descriptors:")
    try:
        person = Person("Alice", 25, 170, "alice@example.com")
        print(f"Validated person: {person.name}, {person.age} years old")
    except ValueError as e:
        print(f"Validation error: {e}")

    # Advanced patterns
    print("\nTesting advanced patterns:")
    some_function()

    print("\nMilestone function calls:")
    for i in range(6):
        milestone_function()

    print("\nCaching strategies:")
    print(f"LRU Fibonacci 10: {fibonacci_lru(10)}")
    print(f"FIFO Fibonacci 10: {fibonacci_fifo(10)}")

    # Practical applications
    print("\nTesting practical applications:")
    api = SecureAPI()
    try:
        print(f"Public data: {api.get_public_data()}")
        print(f"User data: {api.get_user_data('user123')}")
        print(f"Admin data: {api.get_admin_data()}")
    except PermissionError as e:
        print(f"Permission error: {e}")

    print("\nTesting rate limiting:")
    try:
        for i in range(5):
            print(api_call())
    except Exception as e:
        print(f"Rate limit error: {e}")

    print("\n" + "=" * 60)
    print("Decorators mastery demonstration completed!")
    print("Decorators are powerful tools for code reuse and behavior modification.")
    print("=" * 60)
