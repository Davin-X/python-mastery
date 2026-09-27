> Migrated from Davin-X/tech-notes@a1e8fb480b45d6e7f32735f69337c10be32f04a9 (python/python_essentials.md) — standalone handout; for the path-aligned quick reference see python_syntax.md.

# Python Essentials

**Core concepts for practical programming**

---

## 1. Variables & Data Types

```python
# Variables
name = "Alice"
age = 25
price = 19.99
is_active = True

# Data types
my_list = [1, 2, 3]        # List (mutable)
my_tuple = (1, 2, 3)       # Tuple (immutable)
my_dict = {"a": 1, "b": 2} # Dictionary
my_set = {1, 2, 3}         # Set (unique values)

print(type(name))  # <class 'str'>
```

## 2. Control Flow

```python
# If statements
age = 20
if age < 18:
    status = "minor"
elif age < 65:
    status = "adult"
else:
    status = "senior"

# Loops
for i in range(3):              # 0, 1, 2
    print(i)

fruits = ["apple", "banana"]
for fruit in fruits:            # Iterate over list
    print(fruit.upper())

# List comprehensions
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

## 3. Functions

```python
# Function definition
def greet(name="World"):
    """Simple greeting function"""
    return f"Hello, {name}!"

# Function with multiple parameters
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b

# Lambda functions (anonymous)
square = lambda x: x ** 2
is_even = lambda x: x % 2 == 0

print(square(5))      # 25
print(is_even(4))     # True
```

## 4. Classes & OOP

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"

    def is_adult(self):
        return self.age >= 18

# Usage
person = Person("Alice", 25)
print(person.greet())       # Hi, I'm Alice
print(person.is_adult())    # True

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying"

student = Student("Bob", 20, "S123")
print(student.study())      # Bob is studying
```

## 5. File Operations

```python
# Writing to file
with open("data.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a text file.")

# Reading from file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

## 6. Error Handling

```python
try:
    # Risky operation
    result = 10 / 0
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError as e:
    print(f"Value error: {e}")

finally:
    print("This always executes")

# Custom exceptions
class CustomError(Exception):
    pass

def risky_function(x):
    if x < 0:
        raise CustomError("Negative values not allowed")
    return x * 2
```

## 7. Essential Libraries

```python
import json
import os
from datetime import datetime

# JSON handling
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)        # Serialize to string
parsed = json.loads('{"name": "Alice", "age": 25}')  # Parse from string

# File system operations
files = os.listdir('.')             # List current directory
os.path.exists("file.txt")          # Check if file exists

# Date/time
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # 2024-01-15 14:30:45
```

---

## Quick Reference

**Data Types:**
- `int`: Integers
- `float`: Decimals
- `str`: Text
- `bool`: True/False
- `list`: Mutable sequences
- `tuple`: Immutable sequences
- `dict`: Key-value pairs

**Common Operations:**
- `len(obj)` - Get length
- `type(obj)` - Get type
- `range(n)` - Generate 0 to n-1
- `enumerate(items)` - Index pairs
- `zip(a, b)` - Combine iterables

**File Modes:**
- `'r'` - Read
- `'w'` - Write (overwrite)
- `'a'` - Append
- `'r+'` - Read/write
