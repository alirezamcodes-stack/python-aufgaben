# Loops and Conditions Exercises
# Topic: if/elif/else, for loops, while loops, break, continue

# --- Exercise 1: if / elif / else ---
# Determine the grade based on a score.

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for score in [95, 83, 71, 65, 42]:
    print(f"Score {score}: Grade {grade(score)}")

# --- Exercise 2: for Loop ---
# Print the multiplication table for a given number.

number = 7
print(f"\nMultiplication table for {number}:")
for i in range(1, 11):
    print(f"  {number} x {i:2d} = {number * i}")

# --- Exercise 3: while Loop ---
# Use a while loop to find the first power of 2 greater than 1000.

power = 1
exponent = 0
while power <= 1000:
    exponent += 1
    power = 2 ** exponent

print(f"\nFirst power of 2 greater than 1000: 2^{exponent} = {power}")

# --- Exercise 4: break and continue ---
# Print only odd numbers from 1 to 20, stop if the number is 15.

print("\nOdd numbers from 1 to 20 (stop at 15):")
for n in range(1, 21):
    if n == 15:
        break
    if n % 2 == 0:
        continue
    print(n, end=" ")
print()

# --- Exercise 5: Nested Loops ---
# Print a simple number triangle.

print("\nNumber triangle:")
for row in range(1, 6):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()
