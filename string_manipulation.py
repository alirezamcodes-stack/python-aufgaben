# String Manipulation Exercises
# Topic: String methods, slicing, f-strings, and common operations

# --- Exercise 1: Basic String Operations ---

text = "  Hello, Python World!  "
print("Original:  ", repr(text))
print("Stripped:  ", text.strip())
print("Upper:     ", text.strip().upper())
print("Lower:     ", text.strip().lower())
print("Title:     ", text.strip().title())

# --- Exercise 2: Searching and Replacing ---

sentence = "The quick brown fox jumps over the lazy dog"
print("\nSentence:", sentence)
print("Contains 'fox':", "fox" in sentence)
print("Index of 'fox':", sentence.index("fox"))
print("Count of 'the': ", sentence.lower().count("the"))
print("Replace 'fox' -> 'cat':", sentence.replace("fox", "cat"))

# --- Exercise 3: Splitting and Joining ---

csv_line = "Alice,30,Berlin,Engineer"
fields = csv_line.split(",")
print("\nCSV fields:", fields)
print("Joined with ' | ':", " | ".join(fields))

words = sentence.split()
print("Word count:", len(words))

# --- Exercise 4: String Slicing ---

s = "abcdefghij"
print("\nString:", s)
print("First 5 chars: ", s[:5])
print("Last 5 chars:  ", s[-5:])
print("Every 2nd char:", s[::2])
print("Reversed:      ", s[::-1])

# --- Exercise 5: String Formatting ---

name = "Alice"
score = 95.678

# f-string
print(f"\nf-string:  Hello, {name}! Your score is {score:.2f}.")

# str.format()
print("format():  Hello, {}! Your score is {:.2f}.".format(name, score))

# % formatting
print("%%-format: Hello, %s! Your score is %.2f." % (name, score))

# --- Exercise 6: Palindrome Check ---

def is_palindrome(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

test_words = ["racecar", "hello", "A man a plan a canal Panama", "Python"]
print("\nPalindrome check:")
for word in test_words:
    result = "YES" if is_palindrome(word) else "NO"
    print(f"  '{word}' -> {result}")
