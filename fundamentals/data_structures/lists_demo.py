#!/usr/bin/env python3
"""
Python Data Structures: Lists, Tuples, Dictionaries, Sets

This file demonstrates Python's built-in data structures and their operations.
"""

# LISTS - Mutable, ordered sequences
print("=== LISTS ===")

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange", "grape"]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]

print(f"Empty list: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")

# List operations
fruits.append("pineapple")  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "mango")  # Insert at index
print(f"After insert: {fruits}")

fruits.remove("banana")  # Remove by value
print(f"After remove: {fruits}")

last_fruit = fruits.pop()  # Remove and return last item
print(f"Popped: {last_fruit}, Remaining: {fruits}")

# List indexing and slicing
print(f"\nFirst fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"First three: {fruits[:3]}")
print(f"Every other: {fruits[::2]}")
print(f"Reversed: {fruits[::-1]}")

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nOriginal: {numbers}")
numbers.sort()
print(f"Sorted: {numbers}")
numbers.reverse()
print(f"Reversed: {numbers}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 5: {numbers.index(5)}")

# List comprehensions
squares = [x**2 for x in range(10)]
print(f"\nSquares: {squares}")

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# TUPLES - Immutable sequences
print("\n=== TUPLES ===")

# Creating tuples
empty_tuple = ()
single_item = (42,)  # Note the comma!
coordinates = (10, 20, 30)
person = ("Alice", 25, "Engineer")

print(f"Empty tuple: {empty_tuple}")
print(f"Single item: {single_item}")
print(f"Coordinates: {coordinates}")
print(f"Person: {person}")

# Tuple operations (limited due to immutability)
print(f"Length: {len(coordinates)}")
print(f"Index of 20: {coordinates.index(20)}")
print(f"Count of 10: {coordinates.count(10)}")

# Tuple unpacking
x, y, z = coordinates
print(f"Unpacked: x={x}, y={y}, z={z}")

# Named tuples (from collections)
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
p2 = Point(30, 40)

print(f"Point 1: {p1}")
print(f"Point 1 x-coordinate: {p1.x}")
print(f"Point 1 y-coordinate: {p1.y}")
print(f"Are they equal? {p1 == p2}")

# DICTIONARIES - Key-value pairs
print("\n=== DICTIONARIES ===")

# Creating dictionaries
empty_dict = {}
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"]
}

print(f"Empty dict: {empty_dict}")
print(f"Person: {person}")

# Dictionary operations
person["email"] = "alice@example.com"  # Add new key-value
print(f"After adding email: {person}")

person["age"] = 26  # Update existing value
print(f"After updating age: {person}")

del person["city"]  # Remove key-value
print(f"After removing city: {person}")

# Dictionary methods
print(f"\nKeys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

print(f"Has 'name' key: {'name' in person}")
print(f"Get 'age' (default 0): {person.get('age', 0)}")
print(f"Get 'salary' (default 0): {person.get('salary', 0)}")

# Dictionary comprehensions
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dict: {squares_dict}")

# SETS - Unordered collections of unique elements
print("\n=== SETS ===")

# Creating sets
empty_set = set()  # Note: {} creates dict, not set
numbers_set = {1, 2, 3, 4, 5}
fruits_set = {"apple", "banana", "orange"}

print(f"Empty set: {empty_set}")
print(f"Numbers set: {numbers_set}")
print(f"Fruits set: {fruits_set}")

# Set operations
numbers_set.add(6)  # Add element
print(f"After add 6: {numbers_set}")

numbers_set.remove(3)  # Remove element
print(f"After remove 3: {numbers_set}")

# Set operations (mathematical)
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference (A-B): {set_a - set_b}")
print(f"Difference (B-A): {set_b - set_a}")
print(f"Symmetric difference: {set_a ^ set_b}")

# ADVANCED DATA STRUCTURE PATTERNS
print("\n=== ADVANCED PATTERNS ===")

# Nested data structures
company = {
    "name": "TechCorp",
    "departments": {
        "engineering": {
            "employees": ["Alice", "Bob", "Charlie"],
            "budget": 500000
        },
        "sales": {
            "employees": ["Diana", "Eve"],
            "budget": 300000
        }
    },
    "projects": [
        {"name": "AI Assistant", "status": "active", "team": ["Alice", "Bob"]},
        {"name": "Mobile App", "status": "planning", "team": ["Diana"]}
    ]
}

print("Company structure:")
print(f"Company: {company['name']}")
print(f"Engineering employees: {company['departments']['engineering']['employees']}")
print(f"Active projects: {[p['name'] for p in company['projects'] if p['status'] == 'active']}")

# Default dictionaries
from collections import defaultdict

word_counts = defaultdict(int)
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

for word in words:
    word_counts[word] += 1

print(f"\nWord counts: {dict(word_counts)}")

# Ordered dictionaries (Python 3.7+ dicts are ordered by default)
from collections import OrderedDict

# Regular dicts maintain insertion order in Python 3.7+
ordered_dict = {}
ordered_dict['first'] = 1
ordered_dict['second'] = 2
ordered_dict['third'] = 3

print(f"Ordered dict: {ordered_dict}")

# PRACTICAL EXAMPLES
print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Student grade management
students = [
    {"name": "Alice", "grades": [85, 92, 78]},
    {"name": "Bob", "grades": [75, 88, 91]},
    {"name": "Charlie", "grades": [95, 87, 93]}
]

# Calculate average grades
for student in students:
    avg_grade = sum(student["grades"]) / len(student["grades"])
    student["average"] = round(avg_grade, 2)

print("Student averages:")
for student in students:
    print(f"{student['name']}: {student['average']}")

# Example 2: Word frequency counter
text = "the quick brown fox jumps over the lazy dog the fox is quick"
words = text.split()
word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print(f"\nWord frequency: {word_freq}")

# Example 3: Unique items from list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = list(set(numbers))
print(f"Original: {numbers}")
print(f"Unique: {unique_numbers}")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("Python Data Structures Demo Complete!")
    print("You've mastered lists, tuples, dictionaries, and sets.")
    print("="*60)
