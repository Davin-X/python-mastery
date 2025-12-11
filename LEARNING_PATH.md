# 🐍 Python Mastery Learning Path

## Overview

This 16-week comprehensive learning path will take you from Python beginner to expert. Each week includes:

- **📚 Theory**: Core concepts and explanations
- **💻 Practice**: Hands-on coding exercises
- **🛠️ Tools**: Essential tools and libraries
- **🎯 Projects**: Real-world applications
- **📝 Assessment**: Quizzes and challenges

---

## 🏗️ Phase 1: Python Foundations (Weeks 1-4)

### **Week 1: Python Basics**
**Goal**: Master fundamental Python syntax and concepts**

#### 📚 Theory (2-3 hours)
- Python installation and setup
- Interactive REPL (python/python3)
- Basic syntax: variables, data types, operators
- Comments and docstrings
- Print statements and string formatting

#### 💻 Practice (3-4 hours)
```python
# Variables and data types
name = "Alice"
age = 25
height = 5.7
is_student = True

# Basic operations
result = age + 5
message = f"Hello, {name}! You are {age} years old."

# Type conversion
age_str = str(age)
height_int = int(height)
```

#### 🛠️ Tools & Environment
- Install Python 3.8+
- Set up VS Code with Python extensions
- Learn virtual environments (`python -m venv venv`)
- Basic command line usage

#### 🎯 Deliverables
- [ ] Hello World program
- [ ] Simple calculator application
- [ ] Personal information formatter

#### 📝 Assessment
- Quiz: Python data types and operators
- Challenge: Build a unit converter

---

### **Week 2: Data Structures**
**Goal**: Master Python's built-in data structures**

#### 📚 Theory (2-3 hours)
- Lists: creation, indexing, slicing, methods
- Tuples: immutable sequences
- Dictionaries: key-value pairs, methods
- Sets: unique elements, operations
- List comprehensions and generators

#### 💻 Practice (3-4 hours)
```python
# Lists
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
first_fruit = fruits[0]
sliced_fruits = fruits[1:3]

# Dictionaries
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}
person['email'] = 'alice@example.com'

# List comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
even_squares = [x**2 for x in numbers if x % 2 == 0]
```

#### 🛠️ Tools & Libraries
- Python's built-in data structures
- `collections` module (Counter, defaultdict, namedtuple)
- Basic list/dict comprehensions

#### 🎯 Deliverables
- [ ] Student grade management system
- [ ] Word frequency counter
- [ ] Simple inventory management

#### 📝 Assessment
- Quiz: Data structure operations
- Challenge: Implement a basic shopping cart

---

### **Week 3: Control Flow**
**Goal**: Master conditional logic and loops**

#### 📚 Theory (2-3 hours)
- Conditional statements (if/elif/else)
- Loops (for/while)
- Loop control (break/continue)
- Ternary operators
- Exception handling basics

#### 💻 Practice (3-4 hours)
```python
# Conditional statements
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Loops
for i in range(5):
    print(f"Count: {i}")

# List iteration with conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# While loop with break
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
    if count == 3:
        break
```

#### 🛠️ Tools & Concepts
- Python's control flow syntax
- Basic exception handling (try/except)
- Loop optimizations

#### 🎯 Deliverables
- [ ] Number classifier program
- [ ] Basic calculator with error handling
- [ ] Simple game (guess the number)

#### 📝 Assessment
- Quiz: Control flow patterns
- Challenge: Build a menu-driven application

---

### **Week 4: Functions & OOP**
**Goal**: Master functions and object-oriented programming**

#### 📚 Theory (2-3 hours)
- Function definition and calling
- Parameters (positional, keyword, *args, **kwargs)
- Return values and scope
- Classes and objects
- Methods and attributes
- Inheritance and polymorphism

#### 💻 Practice (3-4 hours)
```python
# Functions
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def sum_numbers(*args):
    return sum(args)

def create_person(**kwargs):
    return {
        'name': kwargs.get('name', 'Unknown'),
        'age': kwargs.get('age', 0),
        'city': kwargs.get('city', 'Unknown')
    }

# Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name} and I'm {self.age} years old."

    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! You're now {self.age}."

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying with ID {self.student_id}."
```

#### 🛠️ Tools & Libraries
- Python's function syntax
- Class definitions and inheritance
- Basic OOP principles

#### 🎯 Deliverables
- [ ] Function-based calculator
- [ ] Simple banking system with classes
- [ ] Student management system

#### 📝 Assessment
- Quiz: Functions and OOP concepts
- Challenge: Build a library management system

---

## ⚡ Phase 2: Intermediate Python (Weeks 5-8)

### **Week 5: File Handling & Modules**
**Goal**: Master file I/O and modular programming**

#### 📚 Theory (2-3 hours)
- File operations (open/read/write/close)
- Context managers (with statement)
- File modes and encoding
- pathlib vs os.path
- Importing modules and packages
- Creating custom modules

#### 💻 Practice (3-4 hours)
```python
# File operations
# Writing to a file
with open('data.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.")

# Reading from a file
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Using pathlib
from pathlib import Path

file_path = Path('data.txt')
if file_path.exists():
    content = file_path.read_text()
    print(f"File size: {file_path.stat().st_size} bytes")

# Creating a custom module
# my_module.py
def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

# main.py
import my_module

result1 = my_module.add_numbers(5, 3)
result2 = my_module.multiply_numbers(5, 3)
```

#### 🛠️ Tools & Libraries
- Built-in file operations
- `pathlib` module
- Context managers
- Module creation and importing

#### 🎯 Deliverables
- [ ] File-based contact manager
- [ ] CSV data processor
- [ ] Custom utility module

#### 📝 Assessment
- Quiz: File operations and modules
- Challenge: Build a file-based database

---

### **Week 6: Error Handling & Logging**
**Goal**: Master robust error handling and debugging**

#### 📚 Theory (2-3 hours)
- Exception types and hierarchy
- Try/except/else/finally blocks
- Raising exceptions
- Custom exceptions
- Logging levels and handlers
- Debuggers and debugging techniques

#### 💻 Practice (3-4 hours)
```python
import logging

# Basic exception handling
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input types"
    finally:
        print("Division operation completed")

# Custom exceptions
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance {balance}, needed {amount}")

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)

logger = logging.getLogger(__name__)

def process_data(data):
    logger.info(f"Processing data: {len(data)} items")

    try:
        # Process data
        result = [x * 2 for x in data]
        logger.info(f"Successfully processed {len(result)} items")
        return result
    except Exception as e:
        logger.error(f"Error processing data: {e}")
        raise
```

#### 🛠️ Tools & Libraries
- Built-in exception handling
- `logging` module
- Custom exception classes
- PDB debugger

#### 🎯 Deliverables
- [ ] Robust file processor with error handling
- [ ] Logging system for applications
- [ ] Custom exception hierarchy

#### 📝 Assessment
- Quiz: Exception handling patterns
- Challenge: Build a resilient data processing pipeline

---

### **Week 7: Testing & Quality Assurance**
**Goal**: Master testing and code quality practices**

#### 📚 Theory (2-3 hours)
- Unit testing concepts
- Test-driven development (TDD)
- pytest framework
- Mocking and fixtures
- Code coverage
- PEP 8 and code formatting

#### 💻 Practice (3-4 hours)
```python
# Basic unit testing with unittest
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)

if __name__ == '__main__':
    unittest.main()

# pytest example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

# Mocking example
import pytest
from unittest.mock import Mock, patch

def fetch_data_from_api():
    # Simulates API call
    return {"data": "real data"}

def process_data():
    data = fetch_data_from_api()
    return data["data"].upper()

def test_process_data(mocker):
    # Mock the API call
    mock_api = mocker.patch('__main__.fetch_data_from_api')
    mock_api.return_value = {"data": "test data"}

    result = process_data()
    assert result == "TEST DATA"
    mock_api.assert_called_once()
```

#### 🛠️ Tools & Libraries
- `unittest` (built-in)
- `pytest` framework
- `unittest.mock` for mocking
- `black` for code formatting
- `flake8` for linting

#### 🎯 Deliverables
- [ ] Comprehensive test suite for a calculator
- [ ] Mocked API testing example
- [ ] Code formatting and linting setup

#### 📝 Assessment
- Quiz: Testing concepts and TDD
- Challenge: Achieve 90%+ test coverage on a small project

---

### **Week 8: Decorators & Advanced Patterns**
**Goal**: Master Python's advanced features and patterns**

#### 📚 Theory (2-3 hours)
- Function decorators
- Class decorators
- Decorators with parameters
- Closures and scope
- functools module
- Advanced function concepts

#### 💻 Practice (3-4 hours)
```python
import time
import functools
from typing import Callable, Any

# Simple decorator
def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# Decorator with parameters
def retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"

# Class decorator
class CountCalls:
    def __init__(self, func: Callable):
        self.func = func
        self.call_count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs) -> Any:
        self.call_count += 1
        print(f"Call {self.call_count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name: str) -> str:
    return f"Hello, {name}!"

# functools examples
from functools import lru_cache, partial

@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Partial function
def multiply(x: float, y: float) -> float:
    return x * y

double = partial(multiply, 2)
triple = partial(multiply, 3)

print(double(5))  # 10
print(triple(5))  # 15
```

#### 🛠️ Tools & Libraries
- `functools` module
- Function decorators
- Type hints with `typing`
- Advanced Python features

#### 🎯 Deliverables
- [ ] Performance monitoring decorator
- [ ] Authentication decorator
- [ ] Caching decorator with functools
- [ ] Advanced function utilities

#### 📝 Assessment
- Quiz: Decorator patterns and functools
- Challenge: Build a comprehensive decorator library

---

## 🚀 Phase 3: Advanced Python (Weeks 9-12)

### **Week 9: Async Programming**
**Goal**: Master asynchronous programming in Python**

#### 📚 Theory (2-3 hours)
- Synchronous vs asynchronous programming
- async/await syntax
- Event loops and coroutines
- asyncio module
- Concurrent vs parallel execution

#### 💻 Practice (3-4 hours)
```python
import asyncio
import aiohttp
from typing import List, Dict, Any
import time

# Basic async function
async def say_hello(name: str) -> str:
    await asyncio.sleep(1)  # Simulate I/O operation
    return f"Hello, {name}!"

async def main():
    # Run single coroutine
    result = await say_hello("Alice")
    print(result)

    # Run multiple coroutines concurrently
    tasks = [
        say_hello("Alice"),
        say_hello("Bob"),
        say_hello("Charlie")
    ]
    results = await asyncio.gather(*tasks)
    print(results)

# Async HTTP requests
async def fetch_url(session: aiohttp.ClientSession, url: str) -> Dict[str, Any]:
    async with session.get(url) as response:
        return {
            'url': url,
            'status': response.status,
            'content_length': len(await response.text())
        }

async def fetch_multiple_urls(urls: List[str]) -> List[Dict[str, Any]]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Producer-consumer pattern
async def producer(queue: asyncio.Queue, items: List[int]):
    for item in items:
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.1)

async def consumer(queue: asyncio.Queue, consumer_id: int):
    while True:
        item = await queue.get()
        print(f"Consumer {consumer_id} processing: {item}")
        await asyncio.sleep(0.2)
        queue.task_done()

async def main_producer_consumer():
    queue = asyncio.Queue(maxsize=10)

    # Start consumers
    consumers = [consumer(queue, i) for i in range(3)]
    consumer_tasks = [asyncio.create_task(c) for c in consumers]

    # Start producer
    producer_task = asyncio.create_task(producer(queue, list(range(20))))

    # Wait for producer to finish
    await producer_task

    # Wait for all items to be processed
    await queue.join()

    # Cancel consumer tasks
    for task in consumer_tasks:
        task.cancel()

# Running async code
if __name__ == "__main__":
    # Basic example
    asyncio.run(main())

    # HTTP example
    urls = [
        'https://httpbin.org/get',
        'https://httpbin.org/uuid',
        'https://httpbin.org/json'
    ]
    results = asyncio.run(fetch_multiple_urls(urls))
    for result in results:
        print(result)

    # Producer-consumer
    asyncio.run(main_producer_consumer())
```

#### 🛠️ Tools & Libraries
- `asyncio` module
- `aiohttp` for async HTTP
- Type hints with `typing`

#### 🎯 Deliverables
- [ ] Async web scraper
- [ ] Concurrent file processor
- [ ] Producer-consumer system

#### 📝 Assessment
- Quiz: Async programming concepts
- Challenge: Build an async API client

---

### **Week 10: Metaclasses & Meta Programming**
**Goal**: Master Python's metaclass system**

#### 📚 Theory (2-3 hours)
- Classes as objects
- The `type` metaclass
- Custom metaclasses
- `__new__` vs `__init__`
- Descriptor protocol
- Advanced OOP concepts

#### 💻 Practice (3-4 hours)
```python
# Understanding type metaclass
class MyClass:
    def __init__(self, value):
        self.value = value

# This is equivalent to:
# MyClass = type('MyClass', (), {'__init__': lambda self, value: setattr(self, 'value', value)})

# Custom metaclass
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Using the singleton
obj1 = SingletonClass(42)
obj2 = SingletonClass(100)
print(obj1 is obj2)  # True
print(obj1.value)    # 42 (first instance value)

# Metaclass for automatic attribute validation
class ValidatedMeta(type):
    def __new__(cls, name, bases, namespace, **kwargs):
        # Add validation to all attributes that have validators
        for attr_name, attr_value in namespace.items():
            if isinstance(attr_value, Validator):
                namespace[attr_name] = attr_value
        return super().__new__(cls, name, bases, namespace)

class Validator:
    def __init__(self, validation_func):
        self.validation_func = validation_func

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not self.validation_func(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        instance.__dict__[self.name] = value

def is_positive(value):
    return isinstance(value, (int, float)) and value > 0

def is_email(value):
    return '@' in str(value) and '.' in str(value)

class Person(metaclass=ValidatedMeta):
    age = Validator(is_positive)
    email = Validator(is_email)

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

# Using validated class
person = Person("Alice", 25, "alice@example.com")
# person.age = -5  # Raises ValueError

# Descriptor example
class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        setattr(instance, self.__name__, value)
        return value

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print("Computing area...")
        return 3.14159 * self.radius ** 2

    @LazyProperty
    def circumference(self):
        print("Computing circumference...")
        return 2 * 3.14159 * self.radius

# Using lazy properties
circle = Circle(5)
print(circle.area)        # Computed and cached
print(circle.area)        # Returned from cache
print(circle.circumference)  # Computed and cached

# __new__ method example
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = "Singleton instance"

# Using singleton with __new__
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

#### 🛠️ Tools & Libraries
- Built-in `type` metaclass
- Custom metaclass creation
- Descriptor protocol
- Advanced OOP concepts

#### 🎯 Deliverables
- [ ] Custom metaclass for API validation
- [ ] Descriptor-based property system
- [ ] Singleton and factory patterns

#### 📝 Assessment
- Quiz: Metaclass and descriptor concepts
- Challenge: Build a ORM-like system using metaclasses

---

### **Week 11: Performance & Optimization**
**Goal**: Master performance profiling and optimization**

#### 📚 Theory (2-3 hours)
- Profiling techniques (cProfile, line_profiler)
- Memory profiling
- Big O notation and algorithmic complexity
- Caching strategies (functools.lru_cache)
- Optimization techniques

#### 💻 Practice (3-4 hours)
```python
import cProfile
import time
import functools
from memory_profiler import profile
from typing import List

# Profiling with cProfile
def slow_function(n: int) -> int:
    if n <= 1:
        return n
    return slow_function(n-1) + slow_function(n-2)

def fast_fibonacci(n: int) -> int:
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Profile the functions
print("Profiling recursive Fibonacci:")
cProfile.run('slow_function(30)')

print("\nProfiling iterative Fibonacci:")
cProfile.run('fast_fibonacci(30)')

# Memory profiling
@profile
def memory_intensive():
    data = []
    for i in range(100000):
        data.append(i ** 2)
    return sum(data)

# Caching with functools.lru_cache
@functools.lru_cache(maxsize=128)
def cached_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return cached_fibonacci(n-1) + cached_fibonacci(n-2)

# Performance comparison
def benchmark_functions():
    n = 30

    # Uncached recursive
    start = time.time()
    result1 = slow_function(n)
    time1 = time.time() - start

    # Cached recursive
    start = time.time()
    result2 = cached_fibonacci(n)
    time2 = time.time() - start

    # Iterative
    start = time.time()
    result3 = fast_fibonacci(n)
    time3 = time.time() - start

    print(f"Recursive (uncached): {time1:.4f}s, result: {result1}")
    print(f"Recursive (cached): {time2:.4f}s, result: {result2}")
    print(f"Iterative: {time3:.4f}s, result: {result3}")

benchmark_functions()

# Optimizing list operations
def inefficient_list_ops(n: int) -> List[int]:
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i * 2)
    return result

def efficient_list_ops(n: int) -> List[int]:
    return [i * 2 for i in range(n) if i % 2 == 0]

# String concatenation optimization
def inefficient_string_concat(n: int) -> str:
    result = ""
    for i in range(n):
        result += str(i)
    return result

def efficient_string_concat(n: int) -> str:
    return "".join(str(i) for i in range(n))

# Memory-efficient generator
def memory_efficient_generator(n: int):
    for i in range(n):
        if i % 2 == 0:
            yield i * 2

def memory_inefficient_list(n: int) -> List[int]:
    return [i * 2 for i in range(n) if i % 2 == 0]

# Custom caching decorator
def timed_cache(max_age: float):
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            current_time = time.time()

            if key in cache:
                cached_time, cached_result = cache[key]
                if current_time - cached_time < max_age:
                    return cached_result

            result = func(*args, **kwargs)
            cache[key] = (current_time, result)
            return result

        return wrapper
    return decorator

@timed_cache(max_age=5.0)  # Cache for 5 seconds
def expensive_operation(n: int) -> int:
    time.sleep(1)  # Simulate expensive operation
    return n * 2

# Testing caching
print("First call (uncached):")
start = time.time()
result1 = expensive_operation(10)
print(f"Result: {result1}, Time: {time.time() - start:.2f}s")

print("Second call (cached):")
start = time.time()
result2 = expensive_operation(10)
print(f"Result: {result2}, Time: {time.time() - start:.2f}s")

time.sleep(6)  # Wait for cache to expire

print("Third call (cache expired):")
start = time.time()
result3 = expensive_operation(10)
print(f"Result: {result3}, Time: {time.time() - start:.2f}s")
```

#### 🛠️ Tools & Libraries
- `cProfile` for profiling
- `memory_profiler` for memory analysis
- `functools.lru_cache` for caching
- `time` module for benchmarking

#### 🎯 Deliverables
- [ ] Performance profiling report
- [ ] Optimized algorithm implementations
- [ ] Custom caching and optimization utilities

#### 📝 Assessment
- Quiz: Performance optimization techniques
- Challenge: Optimize a slow application by 10x

---

### **Week 12: Design Patterns**
**Goal**: Master software design patterns in Python**

#### 📚 Theory (2-3 hours)
- Creational patterns (Singleton, Factory, Builder)
- Structural patterns (Adapter, Decorator, Facade)
- Behavioral patterns (Observer, Strategy, Command)
- Pythonic patterns and idioms

#### 💻 Practice (3-4 hours)
```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Protocol
import functools

# Creational Patterns

# 1. Singleton Pattern
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.data = {}

# 2. Factory Pattern
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type.lower() == 'dog':
            return Dog()
        elif animal_type.lower() == 'cat':
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# 3. Builder Pattern
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.toppings = []

    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, and {', '.join(self.toppings)} toppings"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough: str) -> 'PizzaBuilder':
        self.pizza.dough = dough
        return self

    def set_sauce(self, sauce: str) -> 'PizzaBuilder':
        self.pizza.sauce = sauce
        return self

    def add_topping(self, topping: str) -> 'PizzaBuilder':
        self.pizza.toppings.append(topping)
        return self

    def build(self) -> Pizza:
        return self.pizza

# Structural Patterns

# 4. Adapter Pattern
class EuropeanSocket:
    def voltage(self) -> int:
        return 220

    def live(self) -> int:
        return 1

    def neutral(self) -> int:
        return -1

    def earth(self) -> int:
        return 0

class USASocket:
    def voltage(self) -> int:
        return 110

    def live(self) -> int:
        return 1

    def neutral(self) -> int:
        return -1

class Adapter:
    def __init__(self, socket: EuropeanSocket):
        self.socket = socket

    def voltage(self) -> int:
        return self.socket.voltage() // 2

    def live(self) -> int:
        return self.socket.live()

    def neutral(self) -> int:
        return self.socket.neutral()

# 5. Decorator Pattern
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 2.0

    def description(self) -> str:
        return "Simple coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()

class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.5

    def description(self) -> str:
        return self._coffee.description() + ", milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.2

    def description(self) -> str:
        return self._coffee.description() + ", sugar"

# Behavioral Patterns

# 6. Observer Pattern
class Observer(Protocol):
    def update(self, message: str) -> None:
        ...

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)

class NewsAgency(Subject):
    def __init__(self):
        super().__init__()
        self._news = ""

    def set_news(self, news: str) -> None:
        self._news = news
        self.notify(news)

class NewsChannel(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str) -> None:
        print(f"{self.name} received news: {message}")

# 7. Strategy Pattern
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using credit card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using PayPal"

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using Bitcoin"

class ShoppingCart:
    def __init__(self):
        self.items: List[Dict[str, Any]] = []
        self.payment_strategy: PaymentStrategy = None

    def add_item(self, item: Dict[str, Any]) -> None:
        self.items.append(item)

    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        self.payment_strategy = strategy

    def checkout(self) -> str:
        total = sum(item['price'] * item['quantity'] for item in self.items)
        if self.payment_strategy:
            return self.payment_strategy.pay(total)
        return "No payment method selected"

# 8. Command Pattern
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self) -> None:
        self.is_on = True
        print("Light is on")

    def turn_off(self) -> None:
        self.is_on = False
        print("Light is off")

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.turn_on()

    def undo(self) -> None:
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.turn_off()

    def undo(self) -> None:
        self.light.turn_on()

class RemoteControl:
    def __init__(self):
        self.command_history: List[Command] = []

    def execute_command(self, command: Command) -> None:
        command.execute()
        self.command_history.append(command)

    def undo_last_command(self) -> None:
        if self.command_history:
            last_command = self.command_history.pop()
            last_command.undo()

# Demonstration
if __name__ == "__main__":
    # Singleton
    s1 = Singleton()
    s2 = Singleton()
    print(f"Singleton works: {s1 is s2}")

    # Factory
    dog = AnimalFactory.create_animal('dog')
    cat = AnimalFactory.create_animal('cat')
    print(f"Dog says: {dog.speak()}")
    print(f"Cat says: {cat.speak()}")

    # Builder
    pizza = (PizzaBuilder()
             .set_dough("thin")
             .set_sauce("tomato")
             .add_topping("cheese")
             .add_topping("pepperoni")
             .build())
    print(pizza)

    # Adapter
    usa_adapter = Adapter(EuropeanSocket())
    print(f"USA voltage: {usa_adapter.voltage()}V")

    # Decorator
    coffee = SimpleCoffee()
    coffee_with_milk = MilkDecorator(coffee)
    fancy_coffee = SugarDecorator(coffee_with_milk)
    print(f"Cost: ${fancy_coffee.cost()}")
    print(f"Description: {fancy_coffee.description()}")

    # Observer
    news_agency = NewsAgency()
    cnn = NewsChannel("CNN")
    bbc = NewsChannel("BBC")

    news_agency.attach(cnn)
    news_agency.attach(bbc)
    news_agency.set_news("Breaking news!")

    # Strategy
    cart = ShoppingCart()
    cart.add_item({"name": "Book", "price": 20.0, "quantity": 2})

    cart.set_payment_strategy(CreditCardPayment())
    print(cart.checkout())

    # Command
    light = Light()
    remote = RemoteControl()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote.execute_command(light_on)
    remote.execute_command(light_off)
    remote.undo_last_command()
```

#### 🛠️ Tools & Libraries
- `abc` module for abstract base classes
- `typing` module for type hints
- Design pattern implementations

#### 🎯 Deliverables
- [ ] Complete design pattern library
- [ ] Refactored application using patterns
- [ ] Design pattern documentation

#### 📝 Assessment
- Quiz: Design pattern concepts
- Challenge: Refactor existing code using design patterns

---

## 🛠️ Phase 4: Framework Mastery (Weeks 13-16)

### **Week 13: Web Development**
**Goal**: Master modern web development with Python**

#### 📚 Theory (2-3 hours)
- Web frameworks comparison (Flask vs Django vs FastAPI)
- REST API design principles
- HTTP methods and status codes
- Authentication and authorization
- Database integration (SQLAlchemy)

#### 💻 Practice (3-4 hours)
```python
# Flask Example
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['JWT_SECRET_KEY'] = 'your-secret-key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400

    password_hash = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    new_user = User(
        username=data['username'],
        email=data['email'],
        password_hash=password_hash.decode('utf-8')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and bcrypt.checkpw(data['password'].encode('utf-8'), user.password_hash.encode('utf-8')):
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'email': user.email
    } for user in users]), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

#### 🛠️ Tools & Libraries
- Flask web framework
- SQLAlchemy ORM
- JWT for authentication
- bcrypt for password hashing

#### 🎯 Deliverables
- [ ] REST API with authentication
- [ ] User management system
- [ ] Database integration

#### 📝 Assessment
- Quiz: Web development concepts
- Challenge: Build a complete web application

---

### **Week 14: Data Science**
**Goal**: Master data manipulation and analysis**

#### 📚 Theory (2-3 hours)
- Pandas DataFrame operations
- NumPy array operations
- Data cleaning and preprocessing
- Exploratory data analysis
- Data visualization with Matplotlib

#### 💻 Practice (3-4 hours)
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Any

# Creating DataFrames
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'salary': [50000, 60000, 70000, 55000, 65000],
    'department': ['HR', 'IT', 'Finance', 'HR', 'IT']
}

df = pd.DataFrame(data)

# Basic operations
print("First 3 rows:")
print(df.head(3))

print("\nDataFrame info:")
print(df.info())

print("\nDescriptive statistics:")
print(df.describe())

# Filtering and selection
hr_employees = df[df['department'] == 'HR']
high_salary = df[df['salary'] > 60000]

# Grouping and aggregation
dept_stats = df.groupby('department').agg({
    'salary': ['mean', 'min', 'max', 'count'],
    'age': 'mean'
}).round(2)

print("\nDepartment statistics:")
print(dept_stats)

# Data visualization
plt.figure(figsize=(10, 6))

# Subplot 1: Salary distribution
plt.subplot(2, 2, 1)
plt.hist(df['salary'], bins=5, edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')

# Subplot 2: Age vs Salary scatter plot
plt.subplot(2, 2, 2)
plt.scatter(df['age'], df['salary'])
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')

# Subplot 3: Department distribution
plt.subplot(2, 2, 3)
df['department'].value_counts().plot(kind='bar')
plt.title('Employees by Department')
plt.xlabel('Department')
plt.ylabel('Count')

# Subplot 4: Correlation heatmap
plt.subplot(2, 2, 4)
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

plt.tight_layout()
plt.savefig('employee_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Advanced Pandas operations
# Handling missing data
df_with_missing = df.copy()
df_with_missing.loc[0, 'salary'] = np.nan

print("\nHandling missing data:")
print("Original:")
print(df_with_missing)

# Fill with mean
df_filled = df_with_missing.copy()
df_filled['salary'] = df_filled['salary'].fillna(df_filled['salary'].mean())
print("\nFilled with mean:")
print(df_filled)

# Merge operations
departments = pd.DataFrame({
    'department': ['HR', 'IT', 'Finance', 'Marketing'],
    'budget': [100000, 200000, 150000, 80000],
    'manager': ['Alice', 'Bob', 'Charlie', 'Diana']
})

merged_df = pd.merge(df, departments, on='department', how='left')
print("\nMerged with department info:")
print(merged_df)

# Time series operations
dates = pd.date_range('2023-01-01', periods=100, freq='D')
ts_data = pd.DataFrame({
    'date': dates,
    'value': np.random.randn(100).cumsum() + 100
})
ts_data.set_index('date', inplace=True)

# Resampling
monthly_data = ts_data.resample('M').mean()
print("\nMonthly resampled data:")
print(monthly_data.head())

# Rolling statistics
ts_data['rolling_mean'] = ts_data['value'].rolling(window=7).mean()
ts_data['rolling_std'] = ts_data['value'].rolling(window=7).std()

plt.figure(figsize=(12, 6))
plt.plot(ts_data.index, ts_data['value'], label='Original', alpha=0.7)
plt.plot(ts_data.index, ts_data['rolling_mean'], label='7-day Rolling Mean', linewidth=2)
plt.fill_between(ts_data.index,
                 ts_data['rolling_mean'] - ts_data['rolling_std'],
                 ts_data['rolling_mean'] + ts_data['rolling_std'],
                 alpha=0.2, label='Rolling Std Dev')
plt.title('Time Series Analysis with Rolling Statistics')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.savefig('time_series_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# NumPy advanced operations
# Array creation and manipulation
arr_2d = np.random.randint(1, 100, size=(5, 5))
print(f"\n2D Array:\n{arr_2d}")

print(f"\nArray shape: {arr_2d.shape}")
print(f"Array size: {arr_2d.size}")
print(f"Array dtype: {arr_2d.dtype}")

# Statistical operations
print(f"Mean: {arr_2d.mean():.2f}")
print(f"Standard deviation: {arr_2d.std():.2f}")
print(f"Sum: {arr_2d.sum()}")

# Matrix operations
matrix_a = np.random.randint(1, 10, size=(3, 3))
matrix_b = np.random.randint(1, 10, size=(3, 3))

print(f"\nMatrix A:\n{matrix_a}")
print(f"\nMatrix B:\n{matrix_b}")
print(f"\nMatrix multiplication:\n{np.dot(matrix_a, matrix_b)}")
print(f"\nElement-wise multiplication:\n{matrix_a * matrix_b}")

# Broadcasting
vector = np.array([1, 2, 3])
broadcasted = arr_2d[:3, :3] + vector
print(f"\nBroadcasting result:\n{broadcasted}")

# Boolean indexing and advanced selection
mask = arr_2d > 50
filtered_values = arr_2d[mask]
print(f"\nValues > 50: {filtered_values}")
print(f"Count of values > 50: {len(filtered_values)}")

# Sorting and searching
sorted_arr = np.sort(arr_2d, axis=1)
print(f"\nSorted array (by rows):\n{sorted_arr}")

# Unique values and counts
unique, counts = np.unique(arr_2d, return_counts=True)
print(f"\nUnique values: {unique}")
print(f"Counts: {counts}")

# Linear algebra
eigenvalues, eigenvectors = np.linalg.eig(matrix_a.astype(float))
print(f"\nEigenvalues: {eigenvalues}")
print(f"\nEigenvectors:\n{eigenvectors}")

# Random sampling
random_sample = np.random.choice(arr_2d.flatten(), size=10, replace=False)
print(f"\nRandom sample: {random_sample}")
```

#### 🛠️ Tools & Libraries
- `pandas` for data manipulation
- `numpy` for numerical computing
- `matplotlib` for plotting
- `seaborn` for statistical visualization

#### 🎯 Deliverables
- [ ] Data analysis report
- [ ] Visualization dashboard
- [ ] Data cleaning pipeline

#### 📝 Assessment
- Quiz: Data science concepts
- Challenge: Analyze a real dataset

---

### **Week 15: Machine Learning**
**Goal**: Master machine learning with Python**

#### 📚 Theory (2-3 hours)
- Supervised vs unsupervised learning
- Scikit-learn API
- Model evaluation metrics
- Feature engineering
- Cross-validation techniques

#### 💻 Practice (3-4 hours)
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Tuple, Dict, Any

# Load and explore data
def load_and_explore_data() -> pd.DataFrame:
    # Create sample dataset
    np.random.seed(42)
    n_samples = 1000

    data = {
        'age': np.random.normal(35, 10, n_samples).clip(18, 70),
        'income': np.random.normal(50000, 20000, n_samples).clip(0, 200000),
        'education_years': np.random.normal(16, 3, n_samples).clip(8, 25),
        'work_experience': np.random.normal(10, 5, n_samples).clip(0, 40),
        'savings': np.random.normal(20000, 15000, n_samples).clip(0, 100000),
        'credit_score': np.random.normal(650, 50, n_samples).clip(300, 850),
        'approved': np.random.choice([0, 1], n_samples, p=[0.3, 0.7])
    }

    df = pd.DataFrame(data)

    # Add some missing values
    mask = np.random.random(n_samples) < 0.05
    df.loc[mask, 'income'] = np.nan

    print("Dataset shape:", df.shape)
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nTarget distribution:")
    print(df['approved'].value_counts(normalize=True))

    return df

# Data preprocessing
def preprocess_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    # Separate features and target
    X = df.drop('approved', axis=1)
    y = df['approved']

    # Handle missing values
    imputer = SimpleImputer(strategy='median')
    X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

    return X_imputed, y

# Model training and evaluation
def train_and_evaluate_models(X: pd.DataFrame, y: pd.Series) -> Dict[str, Any]:
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Define models
    models = {
        'Logistic Regression': LogisticRegression(random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'SVM': SVC(probability=True, random_state=42)
    }

    results = {}

    for name, model in models.items():
        print(f"\nTraining {name}...")

        # Train model
        model.fit(X_train_scaled, y_train)

        # Make predictions
        y_pred = model.predict(X_test_scaled)
        y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]

        # Evaluate
        print(f"\n{name} Results:")
        print("Classification Report:")
        print(classification_report(y_test, y_pred))

        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        print("Confusion Matrix:")
        print(cm)

        # ROC AUC
        auc = roc_auc_score(y_test, y_pred_proba)
        print(f"ROC AUC Score: {auc:.3f}")

        # Cross-validation score
        cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
        print(f"Cross-validation scores: {cv_scores}")
        print(f"Mean CV score: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")

        results[name] = {
            'model': model,
            'predictions': y_pred,
            'probabilities': y_pred_proba,
            'auc': auc,
            'cv_scores': cv_scores
        }

    return results

# Hyperparameter tuning
def tune_hyperparameters(X: pd.DataFrame, y: pd.Series) -> Dict[str, Any]:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Define parameter grid for Random Forest
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    # Create pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(random_state=42))
    ])

    # Update parameter grid for pipeline
    param_grid_pipeline = {
        'classifier__' + key: value for key, value in param_grid.items()
    }

    # Grid search
    grid_search = GridSearchCV(
        pipeline,
        param_grid_pipeline,
        cv=5,
        scoring='roc_auc',
        n_jobs=-1,
        verbose=1
    )

    print("Performing grid search...")
    grid_search.fit(X_train, y_train)

    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best cross-validation score: {grid_search.best_score_:.3f}")

    # Evaluate best model
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    y_pred_proba = best_model.predict_proba(X_test)[:, 1]

    print("\nBest Model Results:")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print(f"ROC AUC Score: {roc_auc_score(y_test, y_pred_proba):.3f}")

    return {
        'best_model': best_model,
        'best_params': grid_search.best_params_,
        'best_score': grid_search.best_score_,
        'test_auc': roc_auc_score(y_test, y_pred_proba)
    }

# Feature importance analysis
def analyze_feature_importance(model, feature_names: list) -> None:
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]

        print("\nFeature Importances:")
        for i in range(len(feature_names)):
            print(f"{i+1}. {feature_names[indices[i]]}: {importances[indices[i]]:.4f}")

        # Plot feature importances
        plt.figure(figsize=(10, 6))
        plt.title("Feature Importances")
        plt.bar(range(len(feature_names)), importances[indices],
                align="center")
        plt.xticks(range(len(feature_names)), [feature_names[i] for i in indices],
                   rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('feature_importance.png', dpi=300, bbox_inches='tight')
        plt.show()

# Model interpretation and deployment
def create_prediction_function(model, scaler, feature_names: list) -> callable:
    def predict_loan_approval(features: Dict[str, float]) -> Dict[str, Any]:
        """
        Predict loan approval probability for new applicants.

        Args:
            features: Dictionary with keys: age, income, education_years,
                     work_experience, savings, credit_score

        Returns:
            Dictionary with prediction results
        """
        # Validate input
        required_features = set(feature_names)
        provided_features = set(features.keys())

        if not required_features.issubset(provided_features):
            missing = required_features - provided_features
            raise ValueError(f"Missing required features: {missing}")

        # Prepare input data
        input_data = np.array([[features[feature] for feature in feature_names]])
        input_scaled = scaler.transform(input_data)

        # Make prediction
        probability = model.predict_proba(input_scaled)[0][1]
        prediction = 1 if probability > 0.5 else 0

        # Calculate confidence
        confidence = abs(probability - 0.5) * 2  # Scale to 0-1 range

        return {
            'prediction': prediction,
            'probability': probability,
            'confidence': confidence,
            'approved': bool(prediction),
            'recommendation': 'Approve' if prediction else 'Reject'
        }

    return predict_loan_approval

# Main execution
if __name__ == "__main__":
    # Load and explore data
    df = load_and_explore_data()

    # Preprocess data
    X, y = preprocess_data(df)

    # Train and evaluate models
    model_results = train_and_evaluate_models(X, y)

    # Hyperparameter tuning
    tuning_results = tune_hyperparameters(X, y)

    # Analyze feature importance
    best_model = tuning_results['best_model']
    if hasattr(best_model.named_steps['classifier'], 'feature_importances_'):
        analyze_feature_importance(
            best_model.named_steps['classifier'],
            X.columns.tolist()
        )

    # Create prediction function
    scaler = best_model.named_steps['scaler']
    predict_function = create_prediction_function(
        best_model.named_steps['classifier'],
        scaler,
        X.columns.tolist()
    )

    # Test prediction function
    sample_applicant = {
        'age': 35,
        'income': 60000,
        'education_years': 18,
        'work_experience': 12,
        'savings': 25000,
        'credit_score': 720
    }

    result = predict_function(sample_applicant)
    print("
Sample Prediction:")
    print(f"Applicant: {sample_applicant}")
    print(f"Prediction: {result}")
```

#### 🛠️ Tools & Libraries
- `scikit-learn` for machine learning
- `pandas` for data manipulation
- `matplotlib` and `seaborn` for visualization
- `numpy` for numerical computing

#### 🎯 Deliverables
- [ ] Complete ML pipeline
- [ ] Model evaluation and comparison
- [ ] Prediction API

#### 📝 Assessment
- Quiz: Machine learning concepts
- Challenge: Build and deploy an ML model

---

### **Week 16: Automation & DevOps**
**Goal**: Master automation and deployment**

#### 📚 Theory (2-3 hours)
- Script automation with Python
- Task scheduling
- Docker containerization
- CI/CD pipelines
- Cloud deployment

#### 💻 Practice (3-4 hours)
```python
#!/usr/bin/env python3
"""
Automated File Organizer
Organizes files in a directory by type and date
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List
import argparse
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(level)s - %(message)s',
    handlers=[
        logging.FileHandler('file_organizer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class FileOrganizer:
    def __init__(self, source_dir: str, dest_dir: str):
        self.source_dir = Path(source_dir)
        self.dest_dir = Path(dest_dir)
        self.file_types = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
            'spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
            'presentations': ['.ppt', '.pptx', '.odp'],
            'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
            'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
            'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c'],
            'executables': ['.exe', '.msi', '.dmg', '.app'],
            'others': []  # Catch-all for unmatched files
        }

    def get_file_category(self, file_path: Path) -> str:
        """Determine the category of a file based on its extension."""
        extension = file_path.suffix.lower()

        for category, extensions in self.file_types.items():
            if extension in extensions:
                return category

        return 'others'

    def organize_files(self, by_date: bool = False) -> Dict[str, int]:
        """
        Organize files from source directory to destination directory.

        Args:
            by_date: If True, organize files by modification date

        Returns:
            Dictionary with counts of files moved per category
        """
        stats = {}

        if not self.source_dir.exists():
            logger.error(f"Source directory {self.source_dir} does not exist")
            return stats

        self.dest_dir.mkdir(parents=True, exist_ok=True)

        for file_path in self.source_dir.rglob('*'):
            if file_path.is_file():
                category = self.get_file_category(file_path)

                if by_date:
                    # Organize by date
                    mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
                    year_dir = self.dest_dir / category / str(mod_time.year) / f"{mod_time.month:02d}"
                else:
                    # Organize by type only
                    year_dir = self.dest_dir / category

                year_dir.mkdir(parents=True, exist_ok=True)

                # Handle duplicate filenames
                dest_file = year_dir / file_path.name
                counter = 1
                while dest_file.exists():
                    stem = file_path.stem
                    suffix = file_path.suffix
                    dest_file = year_dir / f"{stem}_{counter}{suffix}"
                    counter += 1

                try:
                    shutil.move(str(file_path), str(dest_file))
                    stats[category] = stats.get(category, 0) + 1
                    logger.info(f"Moved {file_path} to {dest_file}")
                except Exception as e:
                    logger.error(f"Failed to move {file_path}: {e}")

        return stats

    def generate_report(self, stats: Dict[str, int]) -> str:
        """Generate a summary report of the organization process."""
        total_files = sum(stats.values())
        report = f"""
File Organization Report
========================
Total files processed: {total_files}

Files by category:
"""

        for category, count in sorted(stats.items()):
            report += f"- {category}: {count} files\n"

        report += f"\nSource directory: {self.source_dir}\n"
        report += f"Destination directory: {self.dest_dir}\n"

        return report

def main():
    parser = argparse.ArgumentParser(description='Organize files by type and optionally by date')
    parser.add_argument('source', help='Source directory to organize')
    parser.add_argument('destination', help='Destination directory for organized files')
    parser.add_argument('--by-date', action='store_true', help='Organize files by modification date')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without moving files')

    args = parser.parse_args()

    organizer = FileOrganizer(args.source, args.destination)

    if args.dry_run:
        print("DRY RUN - No files will be moved")
        # You could implement a dry run method here
    else:
        print("Starting file organization...")
        stats = organizer.organize_files(by_date=args.by_date)

        report = organizer.generate_report(stats)
        print(report)

        # Save report to file
        report_file = Path(args.destination) / "organization_report.txt"
        report_file.write_text(report)
        print(f"Report saved to: {report_file}")

if __name__ == "__main__":
    main()
```

#### 🛠️ Tools & Libraries
- Built-in `os`, `shutil`, `pathlib`
- `argparse` for CLI arguments
- `logging` for monitoring

#### 🎯 Deliverables
- [ ] Automated file organizer
- [ ] Task scheduler
- [ ] Deployment pipeline

#### 📝 Assessment
- Quiz: Automation and DevOps concepts
- Challenge: Build a complete automation system

---

## 🎯 Final Assessment & Certification

### **Project Portfolio Requirements**
To complete the Python Mastery journey, build a portfolio with these projects:

1. **Command-Line Application** (Calculator, File Organizer, etc.)
2. **Web Application** (Flask/Django API with database)
3. **Data Analysis Project** (Pandas analysis with visualizations)
4. **Machine Learning Model** (Scikit-learn with evaluation)
5. **Automated System** (Script with scheduling/monitoring)

### **Code Quality Standards**
- ✅ **PEP 8** compliance (use `black` and `flake8`)
- ✅ **Type hints** throughout codebase
- ✅ **Comprehensive tests** (pytest with 80%+ coverage)
- ✅ **Documentation** (docstrings and READMEs)
- ✅ **Error handling** and logging

### **Performance Benchmarks**
- ✅ **Algorithm complexity** understanding
- ✅ **Memory profiling** experience
- ✅ **Optimization techniques** applied
- ✅ **Scalability considerations**

### **Industry Best Practices**
- ✅ **Version control** (Git with conventional commits)
- ✅ **Virtual environments** (venv/poetry)
- ✅ **Package management** (requirements.txt/poetry.lock)
- ✅ **Code reviews** and testing culture

**Upon completion, you will have the skills and portfolio to:**
- ✅ Pass Python coding interviews at top tech companies
- ✅ Build production-ready Python applications
- ✅ Contribute to open-source Python projects
- ✅ Lead Python development teams

**Congratulations! You've mastered Python! 🐍✨**
