#!/usr/bin/env python3
"""
Python Functions Mastery: From Basics to Advanced Patterns

This file demonstrates Python function concepts:
- Function definition and calling
- Parameters (positional, keyword, *args, **kwargs)
- Return values and scope
- Lambda functions
- Function as first-class objects
- Recursion
"""

# BASIC FUNCTION DEFINITION AND CALLING
print("=== BASIC FUNCTIONS ===")

def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Add two numbers."""
    return a + b

def get_user_info():
    """Get basic user information."""
    return {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }

# Calling functions
greeting = greet("Alice")
print(f"Greeting: {greeting}")

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

user = get_user_info()
print(f"User info: {user}")

# FUNCTIONS WITH PARAMETERS
print("\n=== FUNCTION PARAMETERS ===")

# Positional parameters
def calculate_area(length, width):
    """Calculate rectangle area."""
    return length * width

area = calculate_area(10, 5)
print(f"Rectangle area: {area}")

# Default parameters
def greet_person(name, greeting="Hello", punctuation="!"):
    """Greet with customizable greeting and punctuation."""
    return f"{greeting}, {name}{punctuation}"

print(greet_person("Alice"))
print(greet_person("Bob", "Hi"))
print(greet_person("Charlie", "Hey", "..."))

# Keyword arguments
def create_profile(name, age, city="Unknown", occupation=None):
    """Create a person profile."""
    profile = {
        "name": name,
        "age": age,
        "city": city
    }
    if occupation:
        profile["occupation"] = occupation
    return profile

profile1 = create_profile("Alice", 25, city="New York", occupation="Engineer")
profile2 = create_profile("Bob", 30)  # Using defaults
print(f"Profile 1: {profile1}")
print(f"Profile 2: {profile2}")

# *args - Variable positional arguments
def sum_all(*args):
    """Sum all provided numbers."""
    return sum(args)

def concatenate_strings(separator, *strings):
    """Concatenate strings with separator."""
    return separator.join(strings)

print(f"Sum of 1,2,3,4,5: {sum_all(1,2,3,4,5)}")
print(f"Joined strings: {concatenate_strings(' | ', 'apple', 'banana', 'orange')}")

# **kwargs - Variable keyword arguments
def build_query(**kwargs):
    """Build a database query from keyword arguments."""
    conditions = []
    for key, value in kwargs.items():
        if isinstance(value, str):
            conditions.append(f"{key} = '{value}'")
        else:
            conditions.append(f"{key} = {value}")

    return " AND ".join(conditions)

query = build_query(name="Alice", age=25, active=True)
print(f"Query: WHERE {query}")

# Combining *args and **kwargs
def flexible_function(required_arg, *args, default_param="default", **kwargs):
    """Function demonstrating all parameter types."""
    result = {
        "required": required_arg,
        "args": list(args),
        "default": default_param,
        "kwargs": kwargs
    }
    return result

result = flexible_function(
    "required_value",           # required_arg
    "arg1", "arg2", "arg3",     # *args
    default_param="custom",     # keyword arg for default
    key1="value1", key2=42      # **kwargs
)
print(f"Flexible function result: {result}")

# RETURN VALUES
print("\n=== RETURN VALUES ===")

# Multiple return values (tuple unpacking)
def get_min_max(numbers):
    """Return minimum and maximum from a list."""
    return min(numbers), max(numbers)

def divide_and_remainder(a, b):
    """Return quotient and remainder."""
    return a // b, a % b

min_val, max_val = get_min_max([3, 1, 7, 2, 9, 4])
print(f"Min: {min_val}, Max: {max_val}")

quotient, remainder = divide_and_remainder(17, 5)
print(f"17 ÷ 5 = {quotient} remainder {remainder}")

# Returning different types
def process_data(data, operation):
    """Process data based on operation type."""
    if operation == "sum":
        return sum(data)
    elif operation == "average":
        return sum(data) / len(data)
    elif operation == "count":
        return len(data)
    elif operation == "sort":
        return sorted(data)
    else:
        return None

numbers = [3, 1, 7, 2, 9, 4]
print(f"Sum: {process_data(numbers, 'sum')}")
print(f"Average: {process_data(numbers, 'average')}")
print(f"Sorted: {process_data(numbers, 'sort')}")

# LAMBDA FUNCTIONS
print("\n=== LAMBDA FUNCTIONS ===")

# Basic lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
add = lambda a, b: a + b
print(f"3 + 4 = {add(3, 4)}")

# Lambda in list comprehensions
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Squares: {squares}")
print(f"Evens: {evens}")

# Lambda for sorting
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

# Sort by age
sorted_by_age = sorted(people, key=lambda person: person["age"])
print("Sorted by age:")
for person in sorted_by_age:
    print(f"  {person['name']}: {person['age']}")

# Lambda with conditional
grade_classifier = lambda score: "Pass" if score >= 60 else "Fail"
scores = [85, 45, 92, 38, 76]
grades = list(map(grade_classifier, scores))
print(f"Grades: {grades}")

# FUNCTION SCOPE AND CLOSURES
print("\n=== FUNCTION SCOPE ===")

# Global vs local scope
global_var = "I'm global"

def demonstrate_scope():
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}, Local: {local_var}")

demonstrate_scope()
# print(local_var)  # Would cause NameError - local_var not accessible here

# Modifying global variables
counter = 0

def increment_counter():
    global counter
    counter += 1
    return counter

print(f"Counter: {increment_counter()}")
print(f"Counter: {increment_counter()}")
print(f"Counter: {increment_counter()}")

# Closures
def create_multiplier(factor):
    """Create a function that multiplies by a specific factor."""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")
print(f"Quadruple 5: {quadruple(5)}")

# Accessing closure variables
def create_counter():
    count = 0
    def counter():
        nonlocal count  # Access enclosing scope variable
        count += 1
        return count
    return counter

my_counter = create_counter()
print(f"Counter calls: {my_counter()}, {my_counter()}, {my_counter()}")

# RECURSION
print("\n=== RECURSION ===")

# Factorial
def factorial(n):
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Fibonacci
def fibonacci(n):
    """Calculate nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci 8: {fibonacci(8)}")

# Sum of list (recursive)
def sum_list(numbers):
    """Sum list elements recursively."""
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])

numbers = [1, 2, 3, 4, 5]
print(f"Sum of {numbers}: {sum_list(numbers)}")

# Binary search (recursive)
def binary_search(arr, target, low=0, high=None):
    """Binary search implementation."""
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
index = binary_search(sorted_list, target)
print(f"Index of {target} in {sorted_list}: {index}")

# FUNCTION AS FIRST-CLASS OBJECTS
print("\n=== FUNCTIONS AS OBJECTS ===")

# Assigning functions to variables
def greet_formal(name):
    return f"Good day, {name}."

def greet_casual(name):
    return f"Hey {name}!"

greeter = greet_formal
print(f"Formal greeting: {greeter('Alice')}")

greeter = greet_casual
print(f"Casual greeting: {greeter('Alice')}")

# Functions in data structures
operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b if b != 0 else None
}

def calculate(operation, a, b):
    """Perform calculation using function from dictionary."""
    func = operations.get(operation)
    if func:
        return func(a, b)
    return None

print(f"5 + 3 = {calculate('add', 5, 3)}")
print(f"10 - 4 = {calculate('subtract', 10, 4)}")
print(f"6 * 7 = {calculate('multiply', 6, 7)}")

# Function as parameter
def apply_operation(operation, numbers):
    """Apply operation to list of numbers."""
    return [operation(num) for num in numbers]

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

numbers = [1, 2, 3, 4, 5]
squares = apply_operation(square, numbers)
cubes = apply_operation(cube, numbers)
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Cubes: {cubes}")

# PRACTICAL EXAMPLES
print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Data validation functions
def validate_email(email):
    """Simple email validation."""
    return "@" in email and "." in email and len(email) > 5

def validate_age(age):
    """Age validation."""
    return isinstance(age, int) and 0 <= age <= 150

def validate_name(name):
    """Name validation."""
    return isinstance(name, str) and len(name.strip()) >= 2

def create_user(name, email, age):
    """Create user with validation."""
    errors = []

    if not validate_name(name):
        errors.append("Invalid name")
    if not validate_email(email):
        errors.append("Invalid email")
    if not validate_age(age):
        errors.append("Invalid age")

    if errors:
        return {"success": False, "errors": errors}

    return {
        "success": True,
        "user": {
            "name": name.strip(),
            "email": email.lower(),
            "age": age
        }
    }

# Test user creation
user1 = create_user("Alice Johnson", "alice@example.com", 25)
user2 = create_user("", "invalid-email", -5)

print("User 1 creation:", user1)
print("User 2 creation:", user2)

# Example 2: Function factory for data processing
def create_filter(min_value=None, max_value=None, data_type=None):
    """Create a filtering function with specified criteria."""
    def filter_function(data):
        filtered = []
        for item in data:
            # Check data type
            if data_type and not isinstance(item, data_type):
                continue

            # Check min value
            if min_value is not None and item < min_value:
                continue

            # Check max value
            if max_value is not None and item > max_value:
                continue

            filtered.append(item)
        return filtered
    return filter_function

# Create specific filters
positive_integers = create_filter(min_value=1, data_type=int)
numbers_1_to_10 = create_filter(min_value=1, max_value=10, data_type=int)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3.14, "hello", -1, 0, 15]
print(f"Original data: {data}")
print(f"Positive integers: {positive_integers(data)}")
print(f"Numbers 1-10: {numbers_1_to_10(data)}")

# Example 3: Memoization decorator
def memoize(func):
    """Memoization decorator for expensive functions."""
    cache = {}

    def wrapper(*args, **kwargs):
        # Create a hashable key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

@memoize
def expensive_calculation(n):
    """Simulate expensive calculation."""
    print(f"Calculating for {n}...")
    result = sum(i**2 for i in range(n))
    return result

print("\nMemoization example:")
print(f"First call: {expensive_calculation(1000)}")
print(f"Second call (cached): {expensive_calculation(1000)}")
print(f"Different call: {expensive_calculation(500)}")

# SUMMARY
print("\n" + "="*60)
print("Python Functions Mastery Summary")
print("="*60)
print("✓ Basic function definition and calling")
print("✓ Parameters: positional, keyword, *args, **kwargs")
print("✓ Return values and multiple returns")
print("✓ Lambda functions and expressions")
print("✓ Scope and closures")
print("✓ Recursion and recursive patterns")
print("✓ Functions as first-class objects")
print("✓ Practical examples: validation, filtering, memoization")
print("="*60)

if __name__ == "__main__":
    print("Python functions examples completed successfully!")
