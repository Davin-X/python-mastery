#!/usr/bin/env python3
"""
Python Object-Oriented Programming Fundamentals

This file demonstrates core OOP concepts in Python:
- Classes and objects
- Attributes and methods
- Inheritance
- Polymorphism
- Encapsulation
- Magic methods (dunder methods)
"""

# BASIC CLASSES AND OBJECTS
print("=== BASIC CLASSES AND OBJECTS ===")

class Person:
    """A simple Person class demonstrating basic OOP."""

    # Class attribute (shared by all instances)
    species = "Human"

    def __init__(self, name, age):
        """Initialize a Person object."""
        # Instance attributes
        self.name = name
        self.age = age
        self.created_at = __import__('datetime').datetime.now()

    def greet(self):
        """Return a greeting message."""
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

    def have_birthday(self):
        """Increase age by 1."""
        self.age += 1
        return f"Happy birthday! You're now {self.age}."

    def __str__(self):
        """String representation of the object."""
        return f"Person(name='{self.name}', age={self.age})"

    def __repr__(self):
        """Official string representation."""
        return f"Person('{self.name}', {self.age})"

# Creating objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(f"Person 1: {person1}")
print(f"Person 2: {person2}")
print(f"Species (class attribute): {Person.species}")
print(f"Person 1 greeting: {person1.greet()}")
print(f"Person 2 birthday: {person2.have_birthday()}")

# Accessing attributes
print(f"Person 1 name: {person1.name}")
print(f"Person 2 age: {person2.age}")

# Modifying attributes
person1.name = "Alice Johnson"
person2.age = 31
print(f"Updated person 1: {person1}")
print(f"Updated person 2: {person2}")

# INHERITANCE
print("\n=== INHERITANCE ===")

class Employee(Person):
    """Employee class inheriting from Person."""

    def __init__(self, name, age, employee_id, department, salary):
        # Call parent constructor
        super().__init__(name, age)

        # Employee-specific attributes
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def get_employee_info(self):
        """Return employee information."""
        return {
            "id": self.employee_id,
            "department": self.department,
            "salary": self.salary,
            "annual_salary": self.salary * 12
        }

    def give_raise(self, percentage):
        """Give a salary raise."""
        old_salary = self.salary
        self.salary *= (1 + percentage / 100)
        return f"Salary increased from ${old_salary:.2f} to ${self.salary:.2f}"

    def greet(self):
        """Override parent greeting to be more professional."""
        return f"Hello, I'm {self.name}, a {self.age}-year-old {self.department} employee."

class Manager(Employee):
    """Manager class inheriting from Employee."""

    def __init__(self, name, age, employee_id, department, salary, team_size):
        super().__init__(name, age, employee_id, department, salary)
        self.team_size = team_size
        self.budget = salary * team_size * 0.1  # Simple budget calculation

    def manage_team(self):
        """Return team management info."""
        return f"Managing a team of {self.team_size} people with budget ${self.budget:.2f}"

    def give_raise(self, percentage, bonus_percentage=0):
        """Override to include bonus for managers."""
        base_raise = super().give_raise(percentage)
        if bonus_percentage > 0:
            bonus = self.salary * (bonus_percentage / 100)
            self.salary += bonus
            return f"{base_raise} (plus ${bonus:.2f} bonus)"
        return base_raise

# Creating instances of different classes
employee1 = Employee("Charlie", 28, "EMP001", "Engineering", 75000)
manager1 = Manager("Diana", 35, "MGR001", "Engineering", 95000, 8)

print(f"Employee: {employee1}")
print(f"Manager: {manager1}")
print(f"Employee info: {employee1.get_employee_info()}")
print(f"Manager team: {manager1.manage_team()}")

# Polymorphism - same method name, different behavior
people = [person1, employee1, manager1]
print("\nPolymorphism demonstration:")
for person in people:
    print(f"{person.name}: {person.greet()}")

# Method overriding with different behavior
print(f"\nRaise examples:")
print(f"Employee raise: {employee1.give_raise(5)}")
print(f"Manager raise: {manager1.give_raise(5, 2)}")

# Checking inheritance relationships
print(f"\nInheritance checks:")
print(f"Is Employee a Person? {issubclass(Employee, Person)}")
print(f"Is person1 a Person? {isinstance(person1, Person)}")
print(f"Is employee1 an Employee? {isinstance(employee1, Employee)}")
print(f"Is manager1 a Person? {isinstance(manager1, Person)}")

# MRO (Method Resolution Order)
print(f"\nMethod Resolution Order for Manager:")
for cls in Manager.__mro__:
    print(f"  {cls.__name__}")

# ENCAPSULATION
print("\n=== ENCAPSULATION ===")

class BankAccount:
    """Bank account with encapsulation."""

    def __init__(self, account_number, owner, initial_balance=0):
        # Public attributes
        self.account_number = account_number
        self.owner = owner

        # Private attributes (name mangling)
        self._balance = initial_balance
        self._transaction_history = []

    @property
    def balance(self):
        """Get current balance."""
        return self._balance

    def deposit(self, amount):
        """Deposit money into account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount
        self._transaction_history.append(f"Deposit: +${amount:.2f}")
        return f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}"

    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount
        self._transaction_history.append(f"Withdrawal: -${amount:.2f}")
        return f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}"

    def get_transaction_history(self):
        """Get transaction history."""
        return self._transaction_history.copy()

    def _calculate_interest(self, rate=0.02):
        """Private method to calculate interest (not meant for external use)."""
        return self._balance * rate

    def apply_interest(self, rate=0.02):
        """Apply interest to balance."""
        interest = self._calculate_interest(rate)
        self._balance += interest
        self._transaction_history.append(f"Interest: +${interest:.2f}")
        return f"Applied interest: ${interest:.2f}"

# Using encapsulated class
account = BankAccount("123456789", "Alice", 1000)
print(f"Account: {account.account_number} owned by {account.owner}")
print(f"Initial balance: ${account.balance}")

try:
    print(account.deposit(500))
    print(account.withdraw(200))
    print(account.apply_interest())

    # This would fail - can't withdraw more than balance
    # print(account.withdraw(2000))

except ValueError as e:
    print(f"Error: {e}")

print(f"Transaction history: {account.get_transaction_history()}")

# MAGIC METHODS (DUNDER METHODS)
print("\n=== MAGIC METHODS ===")

class Vector:
    """2D vector class demonstrating magic methods."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """String representation for print()."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Official string representation."""
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        """Addition operator."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """Subtraction operator."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        """Multiplication by scalar."""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __rmul__(self, scalar):
        """Right multiplication (scalar * vector)."""
        return self.__mul__(scalar)

    def __eq__(self, other):
        """Equality comparison."""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __len__(self):
        """Length of vector (magnitude)."""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __getitem__(self, index):
        """Indexing support."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

    def __setitem__(self, index, value):
        """Item assignment support."""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range")

# Using magic methods
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Addition: {v1 + v2}")
print(f"Subtraction: {v1 - v2}")
print(f"Scalar multiplication: {v1 * 2}")
print(f"Scalar multiplication (reverse): {3 * v1}")
print(f"Equality: {v1 == v2}")
print(f"Magnitude (len): {len(v1)}")
print(f"Indexing: v1[0] = {v1[0]}, v1[1] = {v1[1]}")

# Modifying via indexing
v1[0] = 10
print(f"After modification: {v1}")

# CLASS METHODS AND STATIC METHODS
print("\n=== CLASS METHODS AND STATIC METHODS ===")

class MathUtils:
    """Utility class with class and static methods."""

    PI = 3.14159

    @staticmethod
    def is_even(number):
        """Check if number is even (static method)."""
        return number % 2 == 0

    @staticmethod
    def factorial(n):
        """Calculate factorial (static method)."""
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

    @classmethod
    def create_circle_area_calculator(cls, pi_value=None):
        """Create a circle area calculator with custom PI (class method)."""
        pi = pi_value or cls.PI

        def calculate_area(radius):
            return pi * radius ** 2

        return calculate_area

# Using static methods
print(f"Is 4 even? {MathUtils.is_even(4)}")
print(f"Is 7 even? {MathUtils.is_even(7)}")
print(f"Factorial of 5: {MathUtils.factorial(5)}")

# Using class method
circle_area = MathUtils.create_circle_area_calculator()
print(f"Circle area (r=5): {circle_area(5):.2f}")

# With custom PI
precise_area = MathUtils.create_circle_area_calculator(pi_value=3.14159265359)
print(f"Precise circle area (r=5): {precise_area(5):.2f}")

# PRACTICAL EXAMPLES
print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Library Management System
class Book:
    """Book class for library management."""

    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f"'{self.title}' by {self.author} ({status})"

    def check_out(self):
        if not self.available:
            raise ValueError("Book is already checked out")
        self.available = False
        return f"Checked out: {self}"

    def return_book(self):
        if self.available:
            raise ValueError("Book is already available")
        self.available = True
        return f"Returned: {self}"

class Library:
    """Library class to manage books."""

    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book):
        """Add a book to the library."""
        self.books[book.isbn] = book
        return f"Added: {book}"

    def find_book(self, isbn):
        """Find a book by ISBN."""
        return self.books.get(isbn, None)

    def list_available_books(self):
        """List all available books."""
        available = [book for book in self.books.values() if book.available]
        return available

# Using the library system
library = Library("City Library")

book1 = Book("Python Crash Course", "Eric Matthes", "978-1593279288")
book2 = Book("Clean Code", "Robert C. Martin", "978-0132350884")

print("Library operations:")
print(library.add_book(book1))
print(library.add_book(book2))

print(f"\nAvailable books: {len(library.list_available_books())}")
for book in library.list_available_books():
    print(f"  {book}")

print(f"\nChecking out '{book1.title}':")
print(book1.check_out())

print(f"\nAvailable books now: {len(library.list_available_books())}")
print(f"Returning '{book1.title}':")
print(book1.return_book())

# Example 2: Shape Hierarchy with Polymorphism
class Shape:
    """Base class for shapes."""

    def __init__(self, color="blue"):
        self.color = color

    def area(self):
        """Calculate area (to be overridden)."""
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        """Calculate perimeter (to be overridden)."""
        raise NotImplementedError("Subclasses must implement perimeter()")

    def __str__(self):
        return f"{self.__class__.__name__}(color='{self.color}')"

class Rectangle(Shape):
    def __init__(self, width, height, color="blue"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius, color="blue"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Polymorphism in action
shapes = [
    Rectangle(10, 5, "red"),
    Circle(7, "green"),
    Rectangle(6, 8, "blue"),
    Circle(3, "yellow")
]

print(f"\nShape calculations:")
for shape in shapes:
    print(f"{shape}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")

# SUMMARY
print("\n" + "="*60)
print("Python OOP Fundamentals Summary")
print("="*60)
print("✓ Classes and objects (attributes, methods)")
print("✓ Inheritance (single, method overriding, super())")
print("✓ Polymorphism (same method, different behavior)")
print("✓ Encapsulation (private attributes, properties)")
print("✓ Magic methods (__str__, __add__, __eq__, etc.)")
print("✓ Class methods, static methods, properties")
print("✓ Practical examples: Library system, Shape hierarchy")
print("="*60)

if __name__ == "__main__":
    print("Python OOP fundamentals completed successfully!")
