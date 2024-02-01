# Program 1: Print a String
my_string = "Hello, World!"
print(my_string)

# Program 2: Concatenate Two Strings
string1 = "Hello"
string2 = "World"
result_string = string1 + " " + string2
print(result_string)

# Program 3: Find the Length of a String
my_string = "Python"
length = len(my_string)
print(f"Length of the string: {length}")

# Program 4: Convert String to Uppercase
my_string = "hello"
uppercase_string = my_string.upper()
print(f"Uppercase string: {uppercase_string}")

# Program 5: Convert String to Lowercase
my_string = "WORLD"
lowercase_string = my_string.lower()
print(f"Lowercase string: {lowercase_string}")

# Program 6: Access Individual Characters in a String
my_string = "Python"
for char in my_string:
    print(char)

# Program 7: Check if a Substring is Present in a String
main_string = "Hello, World!"
substring = "World"
if substring in main_string:
    print(f"{substring} is present in the string.")
else:
    print(f"{substring} is not present in the string.")

# Program 8: Replace a Substring in a String
original_string = "Hello, Universe!"
substring_to_replace = "Universe"
replacement = "World"
modified_string = original_string.replace(substring_to_replace, replacement)
print(f"Modified String: {modified_string}")

# Program 9: Count the Occurrences of a Character in a String
my_string = "programming"
char_to_count = "m"
count = my_string.count(char_to_count)
print(f"Occurrences of '{char_to_count}' in the string: {count}")

# Program 10: Check if a String is a Palindrome
word = input("Enter a word: ")
reversed_word = word[::-1]
if word == reversed_word:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
