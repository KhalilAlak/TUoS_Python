# =========================================================
# Week 3: High-Order Functions
# Combined Code Sheet (with Exercises Solved)
# =========================================================


# -----------------------------
# MAP FUNCTION
# -----------------------------

# Define a function to square a number
def square(x):
    return x ** 2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to square each element
squared_numbers = map(square, numbers)
result_list = list(squared_numbers)
print(result_list)


# -----------------------------
# FILTER FUNCTION (Lambda)
# -----------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

is_even = lambda x: x % 2 == 0
filtered_numbers = filter(is_even, numbers)
result = list(filtered_numbers)
print(result)


# Same using inline lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = filter(lambda x: x % 2 == 0, numbers)
result = list(filtered_numbers)
print(result)


# Same using named function
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(is_even, numbers)
result_list = list(filtered_numbers)
print(result_list)


# -----------------------------
# REDUCE FUNCTION
# -----------------------------

from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)


# -----------------------------
# FILTER + REDUCE TOGETHER
# -----------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filtered_numbers = filter(lambda x: x % 2 == 0, numbers)
sum_of_filtered = reduce(lambda x, y: x + y, filtered_numbers)
print(sum_of_filtered)


# =========================================================
# EXERCISES
# =========================================================

paragraph = "High order functions make Python code concise and expressive."


# ---------------------------------------------------------
# Exercise 1
# Map: generate list of word lengths
# ---------------------------------------------------------
def word_lengths(paragraph):
    words = paragraph.split()
    return list(map(len, words))

print(word_lengths(paragraph))


# ---------------------------------------------------------
# Exercise 2
# Map: convert words to uppercase
# ---------------------------------------------------------
def uppercase_words(paragraph):
    words = paragraph.split()
    return list(map(str.upper, words))

print(uppercase_words(paragraph))


# ---------------------------------------------------------
# Exercise 3
# Map: count number of words in each paragraph
# ---------------------------------------------------------
def count_words(paragraph):
    return len(paragraph.split())

paragraphs = [
    "Python is powerful",
    "High order functions simplify complex logic"
]

word_counts = list(map(count_words, paragraphs))
print(word_counts)


# ---------------------------------------------------------
# Exercise 4
# Filter sentences longer than a threshold
# ---------------------------------------------------------
def filter_long_sentences(paragraph, threshold):
    sentences = paragraph.split(".")
    return list(filter(lambda s: len(s.split()) > threshold, sentences))

paragraph2 = "Python is great. It is widely used in data science and AI."
print(filter_long_sentences(paragraph2, 4))


# ---------------------------------------------------------
# Exercise 5
# Filter words shorter than a given length
# ---------------------------------------------------------
def filter_short_words(paragraph, min_length):
    words = paragraph.split()
    return list(filter(lambda word: len(word) >= min_length, words))

print(filter_short_words(paragraph, 5))


# ---------------------------------------------------------
# Exercise 6
# Reduce: total number of characters in a paragraph
# ---------------------------------------------------------
def total_characters(paragraph):
    return reduce(lambda x, y: x + y, map(len, paragraph))

print(total_characters(paragraph))