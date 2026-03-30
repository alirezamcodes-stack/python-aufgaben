# Basic Syntax Exercises
# Topic: Variables, data types, arithmetic operators, and basic input/output

# --- Exercise 1: Variables and Data Types ---
# Declare variables of different types and print them.

name = "Alice"
age = 20
height = 1.75
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# --- Exercise 2: Arithmetic Operators ---
# Calculate and print the results of basic arithmetic.

x = 15
y = 4

print("\nArithmetic with x =", x, "and y =", y)
print("Addition:       ", x + y)
print("Subtraction:    ", x - y)
print("Multiplication: ", x * y)
print("Division:       ", x / y)
print("Floor division: ", x // y)
print("Modulo:         ", x % y)
print("Exponentiation: ", x ** y)

# --- Exercise 3: Type Conversion ---
# Convert between types and show the results.

number_str = "42"
number_int = int(number_str)
number_float = float(number_str)

print("\nType conversions:")
print("Original string:", number_str, "->", type(number_str))
print("As integer:     ", number_int, "->", type(number_int))
print("As float:       ", number_float, "->", type(number_float))

# --- Exercise 4: User Input ---
# Uncomment the lines below to run an interactive version.

# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# print(f"Hello, {user_name}! You are {user_age} years old.")
