#!/usr/bin/env python3
"""
Python Basics: Hello World and Fundamental Concepts

This file demonstrates the most basic Python concepts:
- Printing output
- Variables and data types
- Basic operations
- Comments and docstrings
"""

# This is a single-line comment

"""
This is a multi-line comment (docstring)
It can span multiple lines and is often used for documentation
"""

# Hello World - the traditional first program
print("Hello, World!")
print("Welcome to Python Mastery!")

# Variables - storing data
name = "Alice"
age = 25
height = 5.7
is_student = True

# Printing variables
print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My height is {height} feet")
print(f"Am I a student? {is_student}")

# Basic data types
# Strings (text)
greeting = "Hello"
message = 'Welcome to Python!'

# Numbers (integers and floats)
whole_number = 42
decimal_number = 3.14159
negative_number = -10

# Booleans (True/False)
is_raining = False
is_sunny = True

# Basic operations
# Arithmetic
a = 10
b = 3

print(f"\nArithmetic Operations:")
print(f"a + b = {a + b}")    # Addition
print(f"a - b = {a - b}")    # Subtraction
print(f"a * b = {a * b}")    # Multiplication
print(f"a / b = {a / b}")    # Division (float)
print(f"a // b = {a // b}")  # Floor division (integer)
print(f"a % b = {a % b}")    # Modulus (remainder)
print(f"a ** b = {a ** b}")  # Exponentiation

# String operations
first_name = "Ada"
last_name = "Lovelace"
full_name = first_name + " " + last_name

print(f"\nString Operations:")
print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"Full name: {full_name}")
print(f"Name length: {len(full_name)}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")

# Type checking
print(f"\nData Types:")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print(f"Type of is_student: {type(is_student)}")

# Type conversion (casting)
print(f"\nType Conversion:")
number_string = "42"
string_number = 42

# String to int
converted_int = int(number_string)
print(f"String '{number_string}' to int: {converted_int} (type: {type(converted_int)})")

# Int to string
converted_string = str(string_number)
print(f"Int {string_number} to string: '{converted_string}' (type: {type(converted_string)})")

# Float to int (truncates)
float_number = 3.9
converted_to_int = int(float_number)
print(f"Float {float_number} to int: {converted_to_int}")

# Input from user (uncomment to test)
# user_name = input("What is your name? ")
# user_age = int(input("How old are you? "))
# print(f"Hello {user_name}, you are {user_age} years old!")

# Constants (by convention, uppercase)
PI = 3.14159
GRAVITY = 9.81
MAX_USERS = 1000

print(f"\nConstants:")
print(f"PI: {PI}")
print(f"Gravity: {GRAVITY} m/s²")
print(f"Max users: {MAX_USERS}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"\nMultiple assignment: x={x}, y={y}, z={z}")

# Swapping values
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# F-strings (Python 3.6+)
product = "laptop"
price = 999.99
quantity = 2

print(f"\nF-string formatting:")
print(f"Product: {product}")
print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print(f"Total: ${price * quantity}")
print(f"Product name in uppercase: {product.upper()}")

# Escape sequences
print("\nEscape sequences:")
print("Quotes: \"Hello\" and 'World'")
print("New line: First line\nSecond line")
print("Tab:\tIndented text")
print("Backslash: \\\\")
print("Unicode: \\u03A0 (Pi symbol)")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("Python Basics Demo Complete!")
    print("You've learned the fundamentals of Python.")
    print("="*50)
