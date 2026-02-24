# =========================================================
# Introduction to Functions — Part 2
# Combined Code Sheet (with Exercises Solved)
# =========================================================

# -----------------------------
# Basic Function Template
# -----------------------------
def function_name(argument_1, argument_2):
    # Do whatever we want this function to do,
    # using argument_1 and argument_2
    return None

function_name("value_1", "value_2")


# -----------------------------
# Example 1: Simple Function
# -----------------------------
def thank_you():
    print("Hello")
    print("\nYou are doing good work")
    print("\nThank you very much for your efforts on this project.")

thank_you()


# -----------------------------
# Example 2: Function with Argument
# -----------------------------
def thank_you(name):
    print(f"Hello {name}")
    print(f"\nYou are doing good work, {name}!")
    print("Thank you very much for your efforts on this project.")

thank_you('Adriana')
thank_you('Billy')

student = 'Caroline'
thank_you(student)


# -----------------------------
# Common Error Example (Correct Order)
# -----------------------------
def thank_you_with(name):
    print("\nYou are doing good work, %s!" % name)
    print("Thank you very much for your efforts on this project.")

thank_you_with('Adriana')
thank_you_with('Billy')
thank_you_with('Caroline')


# -----------------------------
# Positional Arguments
# -----------------------------
def describe_person(first_name, last_name, age):
    print(f"{first_name} {last_name} is a {age} years old")

describe_person('brian', 'kernighan', 71)

# Incorrect order (example)
describe_person(71, 'brian', 'kernighan')


# -----------------------------
# Global and Local Variables
# -----------------------------
global_variable = "I am accessible anywhere in the program."

def print_global():
    print(global_variable)

def modify_global():
    global global_variable
    global_variable = "I have been modified."

print_global()
modify_global()
print_global()


def function_with_local_variable():
    local_variable = "I am only accessible within this function."
    print(local_variable)

function_with_local_variable()
# print(local_variable)  # This would raise an error


# -----------------------------
# Returning a Value
# -----------------------------
def format_date(day, month, year):
    formatted = str(month) + "/" + str(day) + "/" + str(year)
    return formatted

date = format_date(1, 2, 2022)
print("The formatted date is:", date)


# -----------------------------
# Number to Word Function (Improved)
# -----------------------------
def get_number_word(number):
    if number == 0:
        return 'zero'
    elif number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'
    else:
        return "I'm sorry, I don't know that number."

for current_number in range(0, 6):
    number_word = get_number_word(current_number)
    print(current_number, number_word)


# =========================================================
# EXERCISES
# =========================================================

# -----------------------------
# Exercise 1
# Sum of positive numbers until a negative appears
# -----------------------------
def sum_positive_numbers(numbers):
    total = 0
    for num in numbers:
        if num < 0:
            return total
        total += num
    return total

numbers = [1, 2, 3, -1, 4, 5, 6, 9, -4, -5]
print(sum_positive_numbers(numbers))


# -----------------------------
# Exercise 2
# Count number of vowels in a string
# -----------------------------
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Introduction to Python"))


# -----------------------------
# Exercise 3
# Count number of words in a string
# -----------------------------
def count_words(text):
    return len(text.split())

print(count_words("This is a simple sentence"))


# -----------------------------
# Exercise 4
# Count how many times a character appears in a string
# -----------------------------
def count_character(text, character):
    return text.count(character)

print(count_character("banana", "a"))


# -----------------------------
# Exercise 5
# Return the longest word in a string
# -----------------------------
def longest_word(text):
    words = text.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("data science machine learning python"))


# -----------------------------
# Exercise 6
# Count number of words in a paragraph
# -----------------------------
def count_words_in_paragraph(paragraph):
    return len(paragraph.split())

paragraph = "Python functions make code reusable and clean."
print(count_words_in_paragraph(paragraph))


# =========================================================
# Lambda Functions
# =========================================================

# Basic lambda example
z = lambda x: x * x
print(z(8))

# Lambda adding two numbers
add = lambda x, y: x + y
print(add(5, 3))


# -----------------------------
# Exercise 7 (Lambda Functions)
# -----------------------------

text_1 = "Lambda functions are powerful tools when problems are solved!"

# 1. Count number of words
count_words_lambda = lambda text: len(text.split())
print(count_words_lambda(text_1))

# 2. Check if text ends with "solved!"
ends_with_solved = lambda text: text.endswith("solved!")
print(ends_with_solved(text_1))

# 3. Extract first 6 characters
first_six_chars = lambda text: text[:6]
print(first_six_chars(text_1))

# 4. Count number of spaces
count_spaces = lambda text: text.count(" ")
print(count_spaces(text_1))

# 5. Split text into list of words
split_words = lambda text: text.split()
words_list = split_words(text_1)
print(words_list)

# 6. Print length of each word
word_lengths = lambda words: [len(word) for word in words]
print(word_lengths(words_list))