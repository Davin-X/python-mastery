#!/usr/bin/env python3
"""
Python Modules & Packages Mastery: Imports, Organization, Distribution

This file demonstrates Python's module and package system:
- Importing modules and packages
- Creating custom modules
- Package structure and __init__.py
- Relative vs absolute imports
- Python path and module search
- Distributing packages with setup.py
"""

import sys
import os
from pathlib import Path
import importlib
import pkgutil

# BASIC MODULE IMPORTS
print("=== BASIC MODULE IMPORTS ===")

# Standard library imports
import math
import datetime
import json
import re

# Using imported modules
print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Current datetime: {datetime.datetime.now()}")
print(f"JSON data: {json.dumps({'name': 'Alice', 'age': 25})}")

# Regex example
pattern = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')  # Phone number pattern
text = "Call me at 555-123-4567 or 555-987-6543"
matches = pattern.findall(text)
print(f"Phone numbers found: {matches}")

# Selective imports
from collections import defaultdict, Counter, namedtuple
from typing import List, Dict, Optional, Union

# Using selective imports
word_counts = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(f"Word counts: {dict(word_counts)}")

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point: {p}, x-coordinate: {p.x}")

# Aliased imports
import numpy as np  # Common convention
import pandas as pd
import matplotlib.pyplot as plt

print("Note: numpy, pandas, matplotlib would be available if installed")
print("This demonstrates common import aliasing patterns")

# CREATING CUSTOM MODULES
print("\n=== CREATING CUSTOM MODULES ===")

# Let's create a simple custom module (in real scenarios, this would be separate files)
# For demonstration, we'll simulate module creation

# Creating a simple calculator module
class CalculatorModule:
    """Simulates a calculator module."""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Using the custom "module"
calc = CalculatorModule()
print(f"Calculator: 10 + 5 = {calc.add(10, 5)}")
print(f"Calculator: 10 - 3 = {calc.subtract(10, 3)}")
print(f"Calculator: 6 * 7 = {calc.multiply(6, 7)}")
print(f"Calculator: 15 / 3 = {calc.divide(15, 3)}")

# MODULE SEARCH PATH
print("\n=== MODULE SEARCH PATH ===")

# Python's module search path
print("Python module search path:")
for i, path in enumerate(sys.path, 1):
    print(f"{i}. {path}")

# Current working directory
print(f"\nCurrent working directory: {os.getcwd()}")

