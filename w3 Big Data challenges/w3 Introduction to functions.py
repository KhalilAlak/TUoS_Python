# =========================================================
# Introduction-to-functions—Part 2 (PDF Code + Exercises)
# NOTE: The PDF code blocks below are copied EXACTLY as written.
# =========================================================


# -----------------------------
# PDF: Function template (appears early)
# -----------------------------
# Let's define a function.
def function_name(argument_1, argument_2):
# Do whatever we want this function to do,
# using argument_1 and argument_2
# Use function_name to call the function, (used outside the function)
function_name(value_1, value_2)


# -----------------------------
# PDF: Function template (repeated in syntax section)
# -----------------------------
# Let's define a function.
def function_name(argument_1, argument_2):
# Do whatever we want this function to do,
# using argument_1 and argument_2
# Use function_name to call the function.
function_name(value_1, value_2)


# -----------------------------
# PDF: Basic example (thank_you, no args)
# -----------------------------
def thank_you():
# This function prints "hello world" only.
print("Hello")
print("\nYou are doing good work")
print("\nThank you very much for your efforts on this project.")


# -----------------------------
# PDF: Calling thank_you()
# -----------------------------
thank_you()


# -----------------------------
# PDF: Personalised thank_you(name)
# -----------------------------
def thank_you(name):
# This function prints a two-line personalized thank you message.
print(f"Hello {name}")
print(f"\nYou are doing good work, {name}!" )
print("Thank you very much for your efforts on this project.")


# -----------------------------
# PDF: Calling thank_you('Adriana') and thank_you('Billy')
# -----------------------------
thank_you('Adriana')
thank_you('Billy')


# -----------------------------
# PDF: Using a variable as argument
# -----------------------------
student ='Caroline'
thank_you(student)


# -----------------------------
# PDF: Common error example (calling before defining)
# -----------------------------
thank_you_with('Adriana')
thank_you_with('Billy')
thank_you_with('Caroline')
def thank_you_with(name):
# This function prints a two-line personalized thank you message.
print("\nYou are doing good work, %s!" % name)
print("Thank you very much for your efforts on this project.")


# -----------------------------
# PDF: Correct order (define then call)
# -----------------------------
# define the function first
def thank_you_with(name):
# This function prints a two-line personalized thank you message.
print("\nYou are doing good work, %s!" % name)
print("Thank you very much for your efforts on this project.")
# call the function
thank_you_with('Adriana')
thank_you_with('Billy')
thank_you_with('Caroline')


# -----------------------------
# PDF: Positional arguments example
# -----------------------------
# This function takes in a person's first and last name, and their age.
def describe_person(first_name, last_name, age):
print(f"{first_name} {last_name} is a {age} years old")


# -----------------------------
# PDF: Calling describe_person correctly
# -----------------------------
# This line calls the function and pass three arguments
describe_person('brian', 'kernighan', 71)


# -----------------------------
# PDF: Calling describe_person with wrong order
# -----------------------------
# Mess up the order of the arguments
describe_person(71, 'brian', 'kernighan')


# -----------------------------
# PDF: Global variable example
# -----------------------------
# Example of global variable
global_variable = "I am accessible anywhere in the program."
def print_global():
# Accessing a global variable
print(global_variable)
def modify_global():
global global_variable
# Modifying a global variable
global_variable = "I have been modified."
print_global() # Outputs: I am accessible anywhere in the program.
modify_global()
print_global() # Outputs: I have been modified.


# -----------------------------
# PDF: Local variable example
# -----------------------------
# Example of local variable
def function_with_local_variable():
local_variable = "I am only accessible within this function."
print(local_variable)
function_with_local_variable() # Outputs: I am only accessible within this
# print(local_variable) # This would raise an error: NameError: name
# 'local_variable' is not defined


# -----------------------------
# PDF: Return value example (format_date)
# -----------------------------
# Example:
def format_date(day, month, year):
formatted = str(month) + "/" + str(day) + "/" + str(year)
return(formatted)
date = format_date(1,2,2022)
print("The formatted date is:", date ) # Used outside the function to call the
# function


# -----------------------------
# PDF: get_number_word (first version, incomplete mapping)
# -----------------------------
# Example:
def get_number_word(number):
# Takes in a numerical value, and returns
# the word corresponding to that number.
if number == 1:
return 'one'
elif number == 2:
return 'two'
elif number == 3:
return 'three'
# ...
# Let's try out our function.
for current_number in range(0,4):
number_word = get_number_word(current_number)
print(current_number, number_word)


# -----------------------------
# PDF: get_number_word (improved version with else)
# -----------------------------
def get_number_word(number):
# Takes in a numerical value, and returns
# the word corresponding to that number.
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
# Let's try out our function.
for current_number in range(0,6):
number_word = get_number_word(current_number)
print(current_number, number_word)


# -----------------------------
# PDF: Return stops execution example (line after return never runs)
# -----------------------------
def get_number_word(number):
# Takes in a numerical value, and returns
# the word corresponding to that number.
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
# This line will never execute, because the function has already
# returned a value and stopped executing.
print("This message will never be printed.")
# Let's try out our function.
for current_number in range(0,6):
number_word = get_number_word(current_number)
print(current_number, number_word)


# -----------------------------
# PDF: Lambda example (square)
# -----------------------------
# Example
z = lambda x: x * x
z(8)


# -----------------------------
# PDF: Lambda example (add)
# -----------------------------
# Example: a simple lambda function that adds two numbers:
add = lambda x, y: x + y
print(add(5, 3))


# =========================================================
# EXERCISES (SOLUTIONS)
# =========================================================

# -----------------------------
# Exercise 1
# Write a function that takes a list of numbers as input and returns the sum
# of all positive numbers in the list. Stop and return current sum if a
# negative number is encountered.
# -----------------------------
def sum_positive_until_negative(numbers):
    total = 0
    for n in numbers:
        if n < 0:
            return total
        if n > 0:
            total += n
    return total

numbers = [1, 2, 3, -1, 4, 5, 6, 9, -4, -5]
print("Exercise 1:", sum_positive_until_negative(numbers))


# -----------------------------
# Exercise 2
# Create a Python script that counts the number of vowels in a string.
# -----------------------------
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print("Exercise 2:", count_vowels("Hello Khalil"))


# -----------------------------
# Exercise 3
# Write a program that counts the number of words in a string.
# Words are separated by spaces.
# -----------------------------
def count_words(text):
    # split() handles multiple spaces nicely
    return len(text.split())

print("Exercise 3:", count_words("Words are separated by spaces"))


# -----------------------------
# Exercise 4
# Write a Python function that counts how many times a specific character
# (given by the user) appears in a string.
# -----------------------------
def count_char(text, char):
    return text.count(char)

print("Exercise 4:", count_char("banana", "a"))


# -----------------------------
# Exercise 5
# Function that returns the longest word in a string of words separated by spaces.
# If multiple words have same max length, return the first encountered.
# -----------------------------
def longest_word(text):
    words = text.split()
    if len(words) == 0:
        return ""
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

print("Exercise 5:", longest_word("data science machine learning python"))


# -----------------------------
# Exercise 6
# Function that takes a single string argument and returns the number of words
# in the paragraph.
# -----------------------------
def paragraph_word_count(paragraph):
    return len(paragraph.split())

print("Exercise 6:", paragraph_word_count("This is a paragraph with several words."))


# -----------------------------
# Exercise 7
# 1) lambda count words
# 2) lambda endswith substring (e.g. "solved!")
# 3) lambda first 6 chars
# 4) lambda count spaces
# 5) lambda split into list of words
# 6) for list in (5), print length of each word
# -----------------------------

# IMPORTANT: Replace this with your exact text_1 copied from Blackboard
text_1 = "Replace this with the exact Blackboard text_1 so it ends solved!"

count_words_l = lambda t: len(t.split())
ends_with_l = lambda t, sub: t.endswith(sub)
first_6_l = lambda t: t[:6]
count_spaces_l = lambda t: t.count(" ")
split_words_l = lambda t: t.split()

print("Exercise 7.1:", count_words_l(text_1))
print("Exercise 7.2:", ends_with_l(text_1, "solved!"))
print("Exercise 7.3:", first_6_l(text_1))
print("Exercise 7.4:", count_spaces_l(text_1))

words_list = split_words_l(text_1)
print("Exercise 7.5:", words_list)

for w in words_list:
    print("Exercise 7.6:", w, "->", len(w))# =========================================================
# Introduction-to-functions—Part 2 (PDF Code + Exercises)
# NOTE: The PDF code blocks below are copied EXACTLY as written.
# =========================================================


# -----------------------------
# PDF: Function template (appears early)
# -----------------------------
# Let's define a function.
def function_name(argument_1, argument_2):
# Do whatever we want this function to do,
# using argument_1 and argument_2
# Use function_name to call the function, (used outside the function)
function_name(value_1, value_2)


# -----------------------------
# PDF: Function template (repeated in syntax section)
# -----------------------------
# Let's define a function.
def function_name(argument_1, argument_2):
# Do whatever we want this function to do,
# using argument_1 and argument_2
# Use function_name to call the function.
function_name(value_1, value_2)


# -----------------------------
# PDF: Basic example (thank_you, no args)
# -----------------------------
def thank_you():
# This function prints "hello world" only.
print("Hello")
print("\nYou are doing good work")
print("\nThank you very much for your efforts on this project.")


# -----------------------------
# PDF: Calling thank_you()
# -----------------------------
thank_you()


# -----------------------------
# PDF: Personalised thank_you(name)
# -----------------------------
def thank_you(name):
# This function prints a two-line personalized thank you message.
print(f"Hello {name}")
print(f"\nYou are doing good work, {name}!" )
print("Thank you very much for your efforts on this project.")


# -----------------------------
# PDF: Calling thank_you('Adriana') and thank_you('Billy')
# -----------------------------
thank_you('Adriana')
thank_you('Billy')


# -----------------------------
# PDF: Using a variable as argument
# -----------------------------
student ='Caroline'
thank_you(student)


# -----------------------------
# PDF: Common error example (calling before defining)
# -----------------------------
thank_you_with('Adriana')
thank_you_with('Billy')
thank_you_with('Caroline')
def thank_you_with(name):
# This function prints a two-line personalized thank you message.
print("\nYou are doing good work, %s!" % name)
print("Thank you very much for your efforts on this project.")


# -----------------------------
# PDF: Correct order (define then call)
# -----------------------------
# define the function first
def thank_you_with(name):
# This function prints a two-line personalized thank you message.
print("\nYou are doing good work, %s!" % name)
print("Thank you very much for your efforts on this project.")
# call the function
thank_you_with('Adriana')
thank_you_with('Billy')
thank_you_with('Caroline')


# -----------------------------
# PDF: Positional arguments example
# -----------------------------
# This function takes in a person's first and last name, and their age.
def describe_person(first_name, last_name, age):
print(f"{first_name} {last_name} is a {age} years old")


# -----------------------------
# PDF: Calling describe_person correctly
# -----------------------------
# This line calls the function and pass three arguments
describe_person('brian', 'kernighan', 71)


# -----------------------------
# PDF: Calling describe_person with wrong order
# -----------------------------
# Mess up the order of the arguments
describe_person(71, 'brian', 'kernighan')


# -----------------------------
# PDF: Global variable example
# -----------------------------
# Example of global variable
global_variable = "I am accessible anywhere in the program."
def print_global():
# Accessing a global variable
print(global_variable)
def modify_global():
global global_variable
# Modifying a global variable
global_variable = "I have been modified."
print_global() # Outputs: I am accessible anywhere in the program.
modify_global()
print_global() # Outputs: I have been modified.


# -----------------------------
# PDF: Local variable example
# -----------------------------
# Example of local variable
def function_with_local_variable():
local_variable = "I am only accessible within this function."
print(local_variable)
function_with_local_variable() # Outputs: I am only accessible within this
# print(local_variable) # This would raise an error: NameError: name
# 'local_variable' is not defined


# -----------------------------
# PDF: Return value example (format_date)
# -----------------------------
# Example:
def format_date(day, month, year):
formatted = str(month) + "/" + str(day) + "/" + str(year)
return(formatted)
date = format_date(1,2,2022)
print("The formatted date is:", date ) # Used outside the function to call the
# function


# -----------------------------
# PDF: get_number_word (first version, incomplete mapping)
# -----------------------------
# Example:
def get_number_word(number):
# Takes in a numerical value, and returns
# the word corresponding to that number.
if number == 1:
return 'one'
elif number == 2:
return 'two'
elif number == 3:
return 'three'
# ...
# Let's try out our function.
for current_number in range(0,4):
number_word = get_number_word(current_number)
print(current_number, number_word)


# -----------------------------
# PDF: get_number_word (improved version with else)
# -----------------------------
def get_number_word(number):
# Takes in a numerical value, and returns
# the word corresponding to that number.
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
# Let's try out our function.
for current_number in range(0,6):
number_word = get_number_word(current_number)
print(current_number, number_word)


# -----------------------------
# PDF: Return stops execution example (line after return never runs)
# -----------------------------
def get_number_word(number):
# Takes in a numerical value, and returns
# the word corresponding to that number.
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
# This line will never execute, because the function has already
# returned a value and stopped executing.
print("This message will never be printed.")
# Let's try out our function.
for current_number in range(0,6):
number_word = get_number_word(current_number)
print(current_number, number_word)


# -----------------------------
# PDF: Lambda example (square)
# -----------------------------
# Example
z = lambda x: x * x
z(8)


# -----------------------------
# PDF: Lambda example (add)
# -----------------------------
# Example: a simple lambda function that adds two numbers:
add = lambda x, y: x + y
print(add(5, 3))


# =========================================================
# EXERCISES (SOLUTIONS)
# =========================================================

# -----------------------------
# Exercise 1
# Write a function that takes a list of numbers as input and returns the sum
# of all positive numbers in the list. Stop and return current sum if a
# negative number is encountered.
# -----------------------------
def sum_positive_until_negative(numbers):
    total = 0
    for n in numbers:
        if n < 0:
            return total
        if n > 0:
            total += n
    return total

numbers = [1, 2, 3, -1, 4, 5, 6, 9, -4, -5]
print("Exercise 1:", sum_positive_until_negative(numbers))


# -----------------------------
# Exercise 2
# Create a Python script that counts the number of vowels in a string.
# -----------------------------
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print("Exercise 2:", count_vowels("Hello Khalil"))


# -----------------------------
# Exercise 3
# Write a program that counts the number of words in a string.
# Words are separated by spaces.
# -----------------------------
def count_words(text):
    # split() handles multiple spaces nicely
    return len(text.split())

print("Exercise 3:", count_words("Words are separated by spaces"))


# -----------------------------
# Exercise 4
# Write a Python function that counts how many times a specific character
# (given by the user) appears in a string.
# -----------------------------
def count_char(text, char):
    return text.count(char)

print("Exercise 4:", count_char("banana", "a"))


# -----------------------------
# Exercise 5
# Function that returns the longest word in a string of words separated by spaces.
# If multiple words have same max length, return the first encountered.
# -----------------------------
def longest_word(text):
    words = text.split()
    if len(words) == 0:
        return ""
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

print("Exercise 5:", longest_word("data science machine learning python"))


# -----------------------------
# Exercise 6
# Function that takes a single string argument and returns the number of words
# in the paragraph.
# -----------------------------
def paragraph_word_count(paragraph):
    return len(paragraph.split())

print("Exercise 6:", paragraph_word_count("This is a paragraph with several words."))


# -----------------------------
# Exercise 7
# 1) lambda count words
# 2) lambda endswith substring (e.g. "solved!")
# 3) lambda first 6 chars
# 4) lambda count spaces
# 5) lambda split into list of words
# 6) for list in (5), print length of each word
# -----------------------------

# IMPORTANT: Replace this with your exact text_1 copied from Blackboard
text_1 = "Replace this with the exact Blackboard text_1 so it ends solved!"

count_words_l = lambda t: len(t.split())
ends_with_l = lambda t, sub: t.endswith(sub)
first_6_l = lambda t: t[:6]
count_spaces_l = lambda t: t.count(" ")
split_words_l = lambda t: t.split()

print("Exercise 7.1:", count_words_l(text_1))
print("Exercise 7.2:", ends_with_l(text_1, "solved!"))
print("Exercise 7.3:", first_6_l(text_1))
print("Exercise 7.4:", count_spaces_l(text_1))

words_list = split_words_l(text_1)
print("Exercise 7.5:", words_list)

for w in words_list:
    print("Exercise 7.6:", w, "->", len(w))