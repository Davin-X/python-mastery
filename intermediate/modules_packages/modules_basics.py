#!/usr/bin/env python3
"""
Python Modules and Packages: Organization and Reuse

This file demonstrates Python's module and package system:
- Importing modules
- Creating custom modules
- Packages and __init__.py
- Module search path
- Relative imports
- Standard library modules
"""

import os
import sys
import math
import datetime
from collections import Counter, defaultdict
from typing import List, Dict, Any, Optional

# BASIC MODULE IMPORTS
print("=== BASIC MODULE IMPORTS ===")

# Import entire modules
print(f"Current working directory: {os.getcwd()}")
print(f"Python version: {sys.version}")

# Import specific functions/classes
print(f"PI constant: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Current date/time: {datetime.datetime.now()}")

# Import with aliases
import numpy as np  # Would work if numpy was installed
from math import sqrt as square_root

print(f"Square root using alias: {square_root(25)}")

# CREATING CUSTOM MODULES
print("\n=== CREATING CUSTOM MODULES ===")

# Let's create a simple custom module inline for demonstration
# In real code, this would be in a separate file

# Create a sample module content (we'll simulate this)
module_content = '''
"""Sample math utilities module."""

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def power(base, exponent):
    """Calculate base raised to exponent."""
    return base ** exponent

PI = 3.14159
GRAVITY = 9.81

class Calculator:
    """Simple calculator class."""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def get_history(self):
        return self.history.copy()
'''

# Write the module to a file
with open('math_utils.py', 'w') as f:
    f.write(module_content)

print("Created custom module: math_utils.py")

# Import our custom module
import math_utils

print(f"Custom PI: {math_utils.PI}")
print(f"Custom GRAVITY: {math_utils.GRAVITY}")
print(f"Add function: {math_utils.add(5, 3)}")
print(f"Multiply function: {math_utils.multiply(4, 7)}")
print(f"Power function: {math_utils.power(2, 8)}")

# Use the custom class
calc = math_utils.Calculator()
result1 = calc.add(10, 5)
result2 = calc.add(20, 8)
print(f"Calculator history: {calc.get_history()}")

# MODULE SEARCH PATH
print("\n=== MODULE SEARCH PATH ===")

print("Python module search path:")
for i, path in enumerate(sys.path, 1):
    print(f"{i}. {path}")

# Add current directory to path if not already there
current_dir = os.getcwd()
if current_dir not in sys.path:
    sys.path.append(current_dir)
    print(f"Added current directory to sys.path: {current_dir}")

# PACKAGES AND __init__.py
print("\n=== PACKAGES AND __init__.py ===")

# Create a package structure
package_structure = {
    'mypackage/__init__.py': '''
"""My Package - A sample Python package."""

__version__ = "1.0.0"
__author__ = "Python Mastery"

print("MyPackage initialized!")

# Import key functions to make them available at package level
from .math_operations import add, multiply
from .string_operations import reverse_string, capitalize_words

__all__ = ['add', 'multiply', 'reverse_string', 'capitalize_words']
''',

    'mypackage/math_operations.py': '''
"""Mathematical operations module."""

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(n):
    """Calculate factorial."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)
''',

    'mypackage/string_operations.py': '''
"""String operations module."""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def capitalize_words(text):
    """Capitalize first letter of each word."""
    return text.title()

def count_words(text):
    """Count words in text."""
    return len(text.split())

def remove_punctuation(text):
    """Remove punctuation from text."""
    import string
    return text.translate(str.maketrans('', '', string.punctuation))
'''
}

# Create the package structure
os.makedirs('mypackage', exist_ok=True)

for file_path, content in package_structure.items():
    with open(file_path, 'w') as f:
        f.write(content)

print("Created package structure:")
print("- mypackage/")
print("  ├── __init__.py")
print("  ├── math_operations.py")
print("  └── string_operations.py")

# Import from package
import mypackage

print(f"\nPackage version: {mypackage.__version__}")
print(f"Package author: {mypackage.__author__}")

# Functions imported in __init__.py are available at package level
print(f"Add from package: {mypackage.add(7, 3)}")
print(f"Multiply from package: {mypackage.multiply(6, 9)}")
print(f"Reverse string: {mypackage.reverse_string('hello world')}")
print(f"Capitalize words: {mypackage.capitalize_words('hello world from python')}")

# Import specific modules from package
from mypackage import math_operations, string_operations

print(f"Factorial: {math_operations.factorial(5)}")
print(f"Word count: {string_operations.count_words('This is a test sentence')}")

# RELATIVE IMPORTS
print("\n=== RELATIVE IMPORTS ===")

# Create a subpackage to demonstrate relative imports
subpackage_content = {
    'mypackage/subpackage/__init__.py': '''
"""Subpackage for advanced operations."""
''',

    'mypackage/subpackage/advanced_math.py': '''
"""Advanced math operations using relative imports."""

# Relative import - import from parent package
from ..math_operations import factorial
from ..string_operations import count_words

def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-1)

def factorial_with_words(text):
    """Combine factorial calculation with word counting."""
    fact_result = factorial(len(text.split()))
    word_count = count_words(text)
    return {
        'text': text,
        'word_count': word_count,
        'factorial_of_word_count': fact_result
    }
'''
}

# Create subpackage
os.makedirs('mypackage/subpackage', exist_ok=True)

for file_path, content in subpackage_content.items():
    with open(file_path, 'w') as f:
        f.write(content)

print("Created subpackage with relative imports")

# Import from subpackage
from mypackage.subpackage import advanced_math

print(f"Fibonacci 8: {advanced_math.fibonacci(8)}")
result = advanced_math.factorial_with_words("This is a sample text for testing")
print(f"Combined operation result: {result}")

# STANDARD LIBRARY MODULES DEMO
print("\n=== STANDARD LIBRARY MODULES ===")

# Collections module
print("Collections module:")
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

counter = Counter(data)
print(f"Counter: {counter}")
print(f"Most common: {counter.most_common(2)}")

# Defaultdict
word_groups = defaultdict(list)
words = ['apple', 'banana', 'cherry', 'apricot', 'blueberry']

for word in words:
    key = word[0]  # First letter
    word_groups[key].append(word)

print(f"Grouped by first letter: {dict(word_groups)}")

# OS module
print(f"\nOS module:")
print(f"Current directory: {os.getcwd()}")
print(f"Directory contents: {os.listdir('.')[:5]}...")  # Show first 5 items
print(f"Path separator: '{os.sep}'")
print(f"Environment variable PATH exists: {'PATH' in os.environ}")

# SYS module
print(f"\nSYS module:")
print(f"Python executable: {sys.executable}")
print(f"Platform: {sys.platform}")
print(f"Max recursion limit: {sys.getrecursionlimit()}")

# MATH module
print(f"\nMATH module:")
print(f"Euler's number: {math.e}")
print(f"GCD of 48 and 18: {math.gcd(48, 18)}")
print(f"Sine of 90 degrees: {math.sin(math.radians(90)):.2f}")

# DATETIME module
print(f"\nDATETIME module:")
now = datetime.datetime.now()
print(f"Current time: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Day of week: {now.strftime('%A')}")

# PRACTICAL APPLICATIONS
print("\n=== PRACTICAL APPLICATIONS ===")

# Example 1: File Organizer using modules
def organize_files_by_extension(directory: str = ".") -> Dict[str, List[str]]:
    """Organize files by extension using os and collections."""
    files_by_ext = defaultdict(list)

    try:
        for item in os.listdir(directory):
            if os.path.isfile(item):
                _, ext = os.path.splitext(item)
                ext = ext.lower() or 'no_extension'
                files_by_ext[ext].append(item)
    except PermissionError:
        print(f"Permission denied accessing directory: {directory}")

    return dict(files_by_ext)

file_organization = organize_files_by_extension()
print("Files organized by extension:")
for ext, files in sorted(file_organization.items()):
    print(f"  {ext}: {files}")

# Example 2: Configuration Manager
class ConfigManager:
    """Simple configuration manager using modules."""

    def __init__(self):
        self._config = {}

    def load_from_dict(self, config_dict: Dict[str, Any]) -> None:
        """Load configuration from dictionary."""
        self._config.update(config_dict)

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set configuration value."""
        self._config[key] = value

    def save_to_file(self, filename: str) -> None:
        """Save configuration to file."""
        import json
        with open(filename, 'w') as f:
            json.dump(self._config, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load configuration from file."""
        import json
        try:
            with open(filename, 'r') as f:
                self._config.update(json.load(f))
        except FileNotFoundError:
            print(f"Configuration file not found: {filename}")

# Use configuration manager
config = ConfigManager()
config.load_from_dict({
    'app_name': 'Python Mastery',
    'version': '1.0.0',
    'debug': True,
    'max_connections': 100
})

print(f"\nConfiguration loaded: {config.get('app_name')}")
print(f"Debug mode: {config.get('debug')}")
print(f"Max connections: {config.get('max_connections')}")
print(f"Missing config (with default): {config.get('timeout', 30)}")

# Example 3: Data Processor Pipeline
class DataProcessor:
    """Data processing pipeline using multiple modules."""

    def __init__(self):
        self.processors = []

    def add_processor(self, processor_func):
        """Add a processing function to the pipeline."""
        self.processors.append(processor_func)

    def process(self, data):
        """Process data through the pipeline."""
        result = data
        for processor in self.processors:
            result = processor(result)
        return result

# Create processing functions
def remove_whitespace(text):
    """Remove extra whitespace."""
    import re
    return re.sub(r'\s+', ' ', text.strip())

def capitalize_sentences(text):
    """Capitalize first letter of sentences."""
    import re
    return re.sub(r'(^|[.!?]\s+)([a-z])', lambda m: m.group(1) + m.group(2).upper(), text)

def count_stats(text):
    """Count statistics about the text."""
    words = text.split()
    sentences = text.split('.')
    return {
        'text': text,
        'word_count': len(words),
        'sentence_count': len([s for s in sentences if s.strip()]),
        'avg_word_length': sum(len(word) for word in words) / len(words) if words else 0
    }

# Use the pipeline
pipeline = DataProcessor()
pipeline.add_processor(remove_whitespace)
pipeline.add_processor(capitalize_sentences)
pipeline.add_processor(count_stats)

sample_text = "hello world.   this is a test.   multiple   spaces here."
result = pipeline.process(sample_text)

print(f"\nData processing pipeline result:")
print(f"Original: {sample_text}")
print(f"Processed: {result['text']}")
print(f"Word count: {result['word_count']}")
print(f"Sentence count: {result['sentence_count']}")
print(f"Average word length: {result['avg_word_length']:.1f}")

# CLEANUP
print("\n=== CLEANUP ===")

# Clean up created files and directories
import shutil

cleanup_items = [
    'math_utils.py',
    'mypackage'
]

for item in cleanup_items:
    if os.path.exists(item):
        if os.path.isfile(item):
            os.remove(item)
            print(f"Removed file: {item}")
        elif os.path.isdir(item):
            shutil.rmtree(item)
            print(f"Removed directory: {item}")

print("\nCleanup completed!")

# SUMMARY
print("\n" + "="*60)
print("Python Modules and Packages Summary")
print("="*60)
print("✓ Importing: import module, from module import item, as alias")
print("✓ Custom modules: Create .py files with functions/classes")
print("✓ Packages: Directory with __init__.py file")
print("✓ Module search path: sys.path controls where Python looks")
print("✓ Relative imports: from . import, from .. import")
print("✓ Standard library: os, sys, math, datetime, collections")
print("✓ Practical applications: File organizers, config managers, pipelines")
print("="*60)

if __name__ == "__main__":
    print("Python modules and packages examples completed successfully!")
