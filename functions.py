# Functions Exercises
# Topic: Defining functions, parameters, default values, return values, recursion

# --- Exercise 1: Basic Function ---
# Greet a user by name.

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))

# --- Exercise 2: Default Parameters ---
# Calculate the area of a rectangle (default width = 1).

def rectangle_area(length, width=1):
    return length * width

print(f"\nRectangle area (5, 3): {rectangle_area(5, 3)}")
print(f"Rectangle area (5):    {rectangle_area(5)}")

# --- Exercise 3: Multiple Return Values ---
# Return both the quotient and remainder of a division.

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)
print(f"\n17 divided by 5: quotient = {q}, remainder = {r}")

# --- Exercise 4: Recursion ---
# Calculate the factorial of a number recursively.

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

for i in range(6):
    print(f"  {i}! = {factorial(i)}")

# --- Exercise 5: *args and **kwargs ---
# Sum any number of values.

def total(*args):
    return sum(args)

print(f"\ntotal(1, 2, 3):       {total(1, 2, 3)}")
print(f"total(10, 20, 30, 40): {total(10, 20, 30, 40)}")

# Print keyword arguments as a formatted profile.

def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nProfile:")
print_profile(name="Alice", age=20, city="Berlin")
