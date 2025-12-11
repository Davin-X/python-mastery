#!/usr/bin/env python3
"""
Python Control Flow: Loops, Conditionals, and Logic

This file demonstrates Python's control flow structures:
- Conditional statements (if/elif/else)
- Loops (for/while)
- Loop control (break/continue)
- Nested structures
- Logical operators
"""

# CONDITIONAL STATEMENTS
print("=== CONDITIONAL STATEMENTS ===")

# Basic if statement
age = 25
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# if-elif-else chain
score = 85
if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Satisfactory"
elif score >= 60:
    grade = "D"
    message = "Needs improvement"
else:
    grade = "F"
    message = "Failed"

print(f"Score: {score}, Grade: {grade}, Message: {message}")

# Nested conditionals
temperature = 75
weather = "sunny"
is_weekend = True

if temperature > 80:
    if weather == "sunny":
        activity = "Go swimming"
    else:
        activity = "Stay indoors with AC"
elif temperature > 60:
    if is_weekend:
        activity = "Have a picnic"
    else:
        activity = "Go for a walk"
else:
    activity = "Stay warm inside"

print(f"Temperature: {temperature}°F, Weather: {weather}, Weekend: {is_weekend}")
print(f"Suggested activity: {activity}")

# Ternary operator (conditional expression)
status = "adult" if age >= 18 else "minor"
print(f"Ternary result: {status}")

# Logical operators
has_license = True
is_sober = True
age_18_plus = age >= 18

can_drive = has_license and is_sober and age_18_plus
print(f"Can drive: {can_drive}")

# Complex conditions with logical operators
income = 75000
credit_score = 720
employment_years = 3

# Loan approval logic
loan_approved = (
    income >= 50000 and
    credit_score >= 650 and
    (employment_years >= 2 or income >= 80000)
)

print(f"Loan approved: {loan_approved}")

# FOR LOOPS
print("\n=== FOR LOOPS ===")

# Basic for loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

# For loop with list
fruits = ["apple", "banana", "orange", "grape", "pineapple"]
print("\nFruits in my basket:")
for fruit in fruits:
    print(f"- {fruit}")

# For loop with index using enumerate
print("\nFruits with indices:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# For loop with dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "occupation": "Engineer"
}

print("\nPerson details:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")

# Nested for loops (multiplication table)
print("\nMultiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()  # New line after each row

# List comprehensions (for loop alternatives)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"\nEven numbers: {even_numbers}")

# Transform numbers (square them)
squares = [num ** 2 for num in numbers]
print(f"Squares: {squares}")

# Filter and transform
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehensions
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"\n3x3 multiplication matrix: {matrix}")

# WHILE LOOPS
print("\n=== WHILE LOOPS ===")

# Basic while loop
print("Countdown from 5:")
count = 5
while count > 0:
    print(f"{count}...")
    count -= 1
print("Blast off! 🚀")

# While loop with condition
print("\nGuessing game simulation:")
secret_number = 42
guess = 0
attempts = 0

while guess != secret_number and attempts < 5:
    # Simulate user input (in real code, use input())
    guess = [35, 50, 40, 45, 42][attempts]  # Pre-defined guesses
    attempts += 1

    if guess < secret_number:
        print(f"Guess #{attempts}: {guess} - Too low!")
    elif guess > secret_number:
        print(f"Guess #{attempts}: {guess} - Too high!")
    else:
        print(f"Guess #{attempts}: {guess} - Correct! 🎉")

if guess != secret_number:
    print(f"Sorry, you didn't guess it. The number was {secret_number}.")

# Infinite loop with break
print("\nFinding first number divisible by 7 and 13:")
number = 1
while True:
    if number % 7 == 0 and number % 13 == 0:
        print(f"Found: {number}")
        break
    number += 1

# LOOP CONTROL: break and continue
print("\n=== LOOP CONTROL ===")

# Using break
print("Finding first even number in mixed list:")
mixed_numbers = [1, 3, 5, 6, 8, 9, 11]
for num in mixed_numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
    print(f"Checking: {num} (odd)")

# Using continue
print("\nSkipping odd numbers:")
for num in range(1, 11):
    if num % 2 != 0:
        continue
    print(f"Even number: {num}")

# Practical example: Processing a list with error handling
data = [1, 2, "invalid", 4, 5, None, 7]
processed_data = []

print("\nProcessing data with error handling:")
for item in data:
    try:
        # Try to process the item
        if item is None:
            continue  # Skip None values

        result = item * 2
        processed_data.append(result)
        print(f"Processed {item} → {result}")

    except TypeError:
        print(f"Skipping invalid item: {item}")
        continue

print(f"Final processed data: {processed_data}")

# PASS STATEMENT
print("\n=== PASS STATEMENT ===")

# Pass as placeholder
def future_function():
    pass  # TODO: Implement this function later

class FutureClass:
    pass  # TODO: Implement this class later

# Pass in conditional blocks
status = "pending"
if status == "pending":
    pass  # Do nothing for now
elif status == "approved":
    print("Order approved!")
elif status == "rejected":
    print("Order rejected!")

# PRACTICAL EXAMPLES
print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Grade calculator
def calculate_grade(score):
    """Calculate letter grade from numeric score."""
    if score >= 90:
        return "A", "Excellent"
    elif score >= 80:
        return "B", "Good"
    elif score >= 70:
        return "C", "Satisfactory"
    elif score >= 60:
        return "D", "Needs improvement"
    else:
        return "F", "Failed"

# Test the function
scores = [95, 85, 75, 65, 55]
for score in scores:
    grade, message = calculate_grade(score)
    print(f"Score: {score} → Grade: {grade} ({message})")

# Example 2: FizzBuzz (classic programming problem)
print("\nFizzBuzz (1-20):")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# Example 3: Finding prime numbers
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print("\nPrime numbers between 1-50:")
primes = [num for num in range(1, 51) if is_prime(num)]
print(f"Found {len(primes)} primes: {primes}")

# Example 4: Menu-driven program simulation
def display_menu():
    print("\n=== Calculator Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def calculator():
    """Simple calculator with menu-driven interface."""
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice == 5:
                print("Goodbye!")
                break

            if choice in [1, 2, 3, 4]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                result = 0.0
                operation = ""

                if choice == 1:
                    result = num1 + num2
                    operation = "addition"
                elif choice == 2:
                    result = num1 - num2
                    operation = "subtraction"
                elif choice == 3:
                    result = num1 * num2
                    operation = "multiplication"
                elif choice == 4:
                    if num2 == 0:
                        print("Error: Division by zero!")
                        continue
                    result = num1 / num2
                    operation = "division"

                print(f"Result of {operation}: {result}")
            else:
                print("Invalid choice! Please select 1-5.")

        except ValueError:
            print("Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break

# Uncomment to test the calculator (requires user input)
# calculator()

# SUMMARY
print("\n" + "="*60)
print("Python Control Flow Summary")
print("="*60)
print("✓ Conditional statements: if/elif/else")
print("✓ Loops: for loops with range(), lists, dicts")
print("✓ While loops with conditions")
print("✓ Loop control: break, continue, pass")
print("✓ List comprehensions for concise loops")
print("✓ Error handling in loops")
print("✓ Practical examples: grades, FizzBuzz, primes, menus")
print("="*60)

if __name__ == "__main__":
    print("Control flow examples completed successfully!")
