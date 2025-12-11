#!/usr/bin/env python3
"""
Python File Handling Mastery: I/O Operations, Context Managers, Pathlib

This file demonstrates comprehensive file operations in Python:
- Reading and writing files
- Context managers
- Pathlib vs os.path
- File modes and encoding
- Binary file operations
- File system operations
"""

import os
import shutil
from pathlib import Path
from typing import List, Dict, Any, Optional
import json
import csv
import pickle
import tempfile

# BASIC FILE OPERATIONS
print("=== BASIC FILE OPERATIONS ===")

# Writing to a file (traditional way)
def write_basic_file():
    """Demonstrate basic file writing."""
    # Open file in write mode ('w')
    with open('example.txt', 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a text file.\n")
        file.write("Python file handling is powerful.\n")

    print("File 'example.txt' created successfully!")

# Reading from a file
def read_basic_file():
    """Demonstrate basic file reading."""
    try:
        with open('example.txt', 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found!")

# Reading line by line
def read_line_by_line():
    """Demonstrate reading file line by line."""
    try:
        with open('example.txt', 'r') as file:
            print("Reading line by line:")
            for line_number, line in enumerate(file, 1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print("File not found!")

# Appending to a file
def append_to_file():
    """Demonstrate appending to existing file."""
    with open('example.txt', 'a') as file:
        file.write("This line was appended.\n")
        file.write("File handling is essential for data persistence.\n")

    print("Content appended to 'example.txt'")

# File modes demonstration
def demonstrate_file_modes():
    """Show different file modes."""
    # Write mode ('w') - overwrites existing content
    with open('modes_demo.txt', 'w') as file:
        file.write("This overwrites any existing content.\n")

    # Append mode ('a') - adds to existing content
    with open('modes_demo.txt', 'a') as file:
        file.write("This appends to existing content.\n")

    # Read mode ('r') - default mode
    with open('modes_demo.txt', 'r') as file:
        print("Modes demo content:")
        print(file.read())

# USING PATHLIB (MODERN APPROACH)
print("\n=== PATHLIB OPERATIONS ===")

def pathlib_operations():
    """Demonstrate pathlib operations."""
    # Create Path objects
    current_dir = Path.cwd()
    example_file = Path('example.txt')
    data_dir = Path('data')

    print(f"Current directory: {current_dir}")
    print(f"Example file: {example_file}")
    print(f"Absolute path: {example_file.absolute()}")

    # Check file properties
    if example_file.exists():
        print(f"File exists: {example_file.exists()}")
        print(f"Is file: {example_file.is_file()}")
        print(f"File size: {example_file.stat().st_size} bytes")
        print(f"Last modified: {example_file.stat().st_mtime}")

    # Create directories
    data_dir.mkdir(exist_ok=True)
    sub_dir = data_dir / 'processed'
    sub_dir.mkdir(exist_ok=True)

    print(f"Created directories: {data_dir}, {sub_dir}")

    # List directory contents
    print("Current directory contents:")
    for item in current_dir.iterdir():
        if item.is_file():
            print(f"  📄 {item.name}")
        elif item.is_dir():
            print(f"  📁 {item.name}")

    # File operations with pathlib
    source = Path('example.txt')
    destination = data_dir / 'example_copy.txt'

    if source.exists():
        shutil.copy2(source, destination)
        print(f"Copied {source} to {destination}")

# WORKING WITH DIFFERENT FILE FORMATS
print("\n=== DIFFERENT FILE FORMATS ===")

def json_operations():
    """Demonstrate JSON file operations."""
    # Sample data
    person_data = {
        "name": "Alice Johnson",
        "age": 28,
        "city": "San Francisco",
        "skills": ["Python", "JavaScript", "SQL"],
        "projects": [
            {"name": "Web App", "status": "completed"},
            {"name": "API", "status": "in_progress"}
        ]
    }

    # Write JSON
    with open('person.json', 'w') as json_file:
        json.dump(person_data, json_file, indent=2)

    print("JSON file created: person.json")

    # Read JSON
    with open('person.json', 'r') as json_file:
        loaded_data = json.load(json_file)

    print(f"Loaded data: {loaded_data['name']} from {loaded_data['city']}")

def csv_operations():
    """Demonstrate CSV file operations."""
    # Sample data
    employees = [
        ["Name", "Department", "Salary", "Years"],
        ["Alice", "Engineering", "95000", "3"],
        ["Bob", "Marketing", "65000", "5"],
        ["Charlie", "Engineering", "85000", "2"],
        ["Diana", "HR", "55000", "7"]
    ]

    # Write CSV
    with open('employees.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in employees:
            writer.writerow(row)

    print("CSV file created: employees.csv")

    # Read CSV
    with open('employees.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        print("CSV content:")
        for row in reader:
            print(f"  {', '.join(row)}")

    # Using DictReader for better data handling
    with open('employees.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        engineering_employees = [
            row for row in reader
            if row['Department'] == 'Engineering'
        ]

    print(f"Engineering employees: {len(engineering_employees)}")

def pickle_operations():
    """Demonstrate pickle for Python object serialization."""
    # Complex Python object
    class Person:
        def __init__(self, name, age, skills):
            self.name = name
            self.age = age
            self.skills = skills

        def __repr__(self):
            return f"Person('{self.name}', {self.age}, {self.skills})"

    alice = Person("Alice", 28, ["Python", "ML", "Data Science"])
    bob = Person("Bob", 32, ["JavaScript", "React", "Node.js"])

    people = [alice, bob]

    # Serialize with pickle
    with open('people.pkl', 'wb') as pickle_file:
        pickle.dump(people, pickle_file)

    print("Pickle file created: people.pkl")

    # Deserialize with pickle
    with open('people.pkl', 'rb') as pickle_file:
        loaded_people = pickle.load(pickle_file)

    print(f"Loaded people: {loaded_people}")

# ADVANCED FILE OPERATIONS
print("\n=== ADVANCED FILE OPERATIONS ===")

def file_encoding_demo():
    """Demonstrate file encoding operations."""
    # Write with specific encoding
    text_with_unicode = "Hello 世界 🌍 Python is great!"

    with open('unicode_demo.txt', 'w', encoding='utf-8') as file:
        file.write(text_with_unicode)

    print("Unicode file created: unicode_demo.txt")

    # Read with specific encoding
    with open('unicode_demo.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"Unicode content: {content}")

def binary_file_operations():
    """Demonstrate binary file operations."""
    # Write binary data
    binary_data = bytes([0x41, 0x42, 0x43, 0x00, 0xFF, 0xFE])  # ABC + null + bytes

    with open('binary_demo.bin', 'wb') as binary_file:
        binary_file.write(binary_data)

    print("Binary file created: binary_demo.bin")

    # Read binary data
    with open('binary_demo.bin', 'rb') as binary_file:
        data = binary_file.read()
        print(f"Binary data: {data}")
        print(f"As hex: {data.hex()}")

def file_system_operations():
    """Demonstrate file system operations."""
    # Create directory structure
    project_dir = Path('my_project')
    project_dir.mkdir(exist_ok=True)

    # Create subdirectories
    dirs_to_create = [
        project_dir / 'src',
        project_dir / 'tests',
        project_dir / 'docs',
        project_dir / 'data'
    ]

    for dir_path in dirs_to_create:
        dir_path.mkdir(exist_ok=True)

    # Create some files
    (project_dir / 'src' / 'main.py').write_text('# Main application file\nprint("Hello from main.py")')
    (project_dir / 'src' / '__init__.py').write_text('# Package initialization')
    (project_dir / 'README.md').write_text('# My Project\n\nA sample Python project.')

    print(f"Project structure created at: {project_dir.absolute()}")

    # List directory tree
    def print_tree(path, prefix=""):
        if path.is_file():
            print(f"{prefix}📄 {path.name}")
        elif path.is_dir():
            print(f"{prefix}📁 {path.name}/")
            for item in sorted(path.iterdir()):
                print_tree(item, prefix + "  ")

    print("\nProject tree:")
    print_tree(project_dir)

    # File statistics
    total_files = sum(1 for _ in project_dir.rglob('*') if _.is_file())
    total_dirs = sum(1 for _ in project_dir.rglob('*') if _.is_dir())
    total_size = sum(f.stat().st_size for f in project_dir.rglob('*') if f.is_file())

    print("\nProject statistics:")
    print(f"  Directories: {total_dirs}")
    print(f"  Files: {total_files}")
    print(f"  Total size: {total_size} bytes")

# CONTEXT MANAGERS AND RESOURCE MANAGEMENT
print("\n=== CONTEXT MANAGERS ===")

class FileProcessor:
    """Custom context manager for file processing."""

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Enter the context - open the file."""
        self.file = open(self.filename, self.mode)
        print(f"Opened file: {self.filename}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context - close the file."""
        if self.file:
            self.file.close()
            print(f"Closed file: {self.filename}")
        return False  # Don't suppress exceptions

def context_manager_demo():
    """Demonstrate context manager usage."""
    # Using built-in context manager
    with open('context_demo.txt', 'w') as file:
        file.write("This file is managed by a context manager.\n")
        file.write("It will be automatically closed.\n")

    print("File automatically closed by context manager")

    # Using custom context manager
    with FileProcessor('context_demo.txt', 'r') as file:
        content = file.read()
        print(f"Content read: {content[:50]}...")

def multiple_file_operations():
    """Demonstrate working with multiple files simultaneously."""
    files_data = {
        'file1.txt': 'Content of file 1',
        'file2.txt': 'Content of file 2',
        'file3.txt': 'Content of file 3'
    }

    # Write multiple files
    for filename, content in files_data.items():
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Created: {filename}")

    # Read multiple files
    total_content = ""
    for filename in files_data.keys():
        with open(filename, 'r') as file:
            total_content += file.read() + "\n"

    print(f"Combined content length: {len(total_content)} characters")

# PRACTICAL APPLICATIONS
print("\n=== PRACTICAL APPLICATIONS ===")

def log_analyzer(log_file_path: str) -> Dict[str, Any]:
    """Analyze a log file and return statistics."""
    stats = {
        'total_lines': 0,
        'error_count': 0,
        'warning_count': 0,
        'info_count': 0,
        'lines_with_errors': [],
        'most_common_words': {}
    }

    try:
        with open(log_file_path, 'r') as log_file:
            for line_num, line in enumerate(log_file, 1):
                stats['total_lines'] += 1
                line_lower = line.lower()

                if 'error' in line_lower:
                    stats['error_count'] += 1
                    stats['lines_with_errors'].append(line_num)
                elif 'warning' in line_lower:
                    stats['warning_count'] += 1
                elif 'info' in line_lower:
                    stats['info_count'] += 1

                # Simple word frequency (basic implementation)
                words = line.split()
                for word in words:
                    word = word.strip('.,!?').lower()
                    if len(word) > 3:  # Only words longer than 3 chars
                        stats['most_common_words'][word] = stats['most_common_words'].get(word, 0) + 1

    except FileNotFoundError:
        print(f"Log file not found: {log_file_path}")
        return stats

    # Get top 5 most common words
    sorted_words = sorted(stats['most_common_words'].items(), key=lambda x: x[1], reverse=True)
    stats['most_common_words'] = dict(sorted_words[:5])

    return stats

def data_exporter(data: List[Dict], filename: str, format_type: str = 'json'):
    """Export data to different formats."""
    if format_type == 'json':
        with open(f'{filename}.json', 'w') as file:
            json.dump(data, file, indent=2)
        print(f"Data exported to {filename}.json")

    elif format_type == 'csv':
        if data:
            fieldnames = data[0].keys()
            with open(f'{filename}.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        print(f"Data exported to {filename}.csv")

def create_sample_log():
    """Create a sample log file for demonstration."""
    log_content = """2025-01-01 10:00:00 INFO Application started
2025-01-01 10:01:15 INFO User login: alice@example.com
2025-01-01 10:02:30 WARNING High memory usage detected
2025-01-01 10:03:45 ERROR Database connection failed
2025-01-01 10:04:00 INFO Retrying database connection
2025-01-01 10:05:15 ERROR Authentication failed for user bob
2025-01-01 10:06:30 WARNING Disk space running low
2025-01-01 10:07:45 INFO Backup completed successfully
2025-01-01 10:08:00 ERROR Network timeout occurred
2025-01-01 10:09:15 INFO Application shutdown"""

    with open('sample.log', 'w') as log_file:
        log_file.write(log_content)

    print("Sample log file created: sample.log")

# DEMONSTRATION
if __name__ == "__main__":
    print("Python File Handling Mastery Demo")
    print("=" * 50)

    # Basic operations
    write_basic_file()
    read_basic_file()
    read_line_by_line()
    append_to_file()
    demonstrate_file_modes()

    # Pathlib operations
    pathlib_operations()

    # Different file formats
    json_operations()
    csv_operations()
    pickle_operations()

    # Advanced operations
    file_encoding_demo()
    binary_file_operations()
    file_system_operations()

    # Context managers
    context_manager_demo()
    multiple_file_operations()

    # Practical applications
    create_sample_log()
    log_stats = log_analyzer('sample.log')
    print(f"\nLog analysis results: {log_stats}")

    # Data export
    sample_data = [
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "San Francisco"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]

    data_exporter(sample_data, 'people', 'json')
    data_exporter(sample_data, 'people', 'csv')

    print("\n" + "=" * 60)
    print("File handling demonstration completed!")
    print("All files created can be found in the current directory.")
    print("=" * 60)
