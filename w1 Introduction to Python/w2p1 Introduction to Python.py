#Example 1
print("Hello, World!")
#Example 2
print("""Welcome to Python programming.""")
#Example 3/
# This is a single-line comment.
#Example 4
x = input("Please enter a value: ") #Insert number 6
print("The value of x is:", x)
# Example 4
# Addition
print(3+2)
# Subtraction
print(3-2)
# Multiplication
print(3*2)
# Division
print(3/2)
# Exponential
print(3**2)
# Example 5
standard_order = 2+3*4
print(standard_order)
# Example 6
standard_order = (2+3)*4
print(standard_order)
# Example 7: Adding two decimal numbers
num = 0.1
print (num+num)
# Example 8
print(0.1+0.2)
# Test
3*0.1 == 0.3
# Example 9
print(round(5.6231))
# or
x= 5.645776
print(round(x, 2))

# Example 10
my_string_double = "This is a double-quoted string."
print("Using double quotes", my_string_double)
my_string_single = 'This is a single-quoted string.'
print("Using single quote", my_string_single)

# Example 11
quote = "Linus Torvalds once said, \
    'Any program is only as good as it is useful.'"
print(quote)

quote = "Linus Torvalds once said, \
    'Any program is only as good as it is useful.'"
print(quote)

if "Linus Torvalds once said, \
    'Any program is only as good as it is useful.'" == "Linus Torvalds once said, \
    'Any program is only as good as it is useful.'":
        print("The strings are equal.")

# Example 12
multiline_string = '''This is a string where I
can confortably write on multiple lines
without worring about to use the escape character "\\" as in the previsou example.
As youll see, the original string formatting is preserved.
'''
print(multiline_string)

# Example 13 

first_name = 'Jemmy and elesger'

print(first_name)
print(first_name.title())
print(first_name.upper())

# Example 14

first_name = 'emma'
print(first_name)
print(first_name.title()) 
#initiate with an Upper letter
print (first_name.upper()) 
#All the characters are in UPPER case
first_name_mixed = 'EmMa'
print(first_name_mixed.lower())
# All the characters are in lower case

# Example 15
print(first_name)
print(first_name_mixed)

# Example 16

first_name = 'Guido'
last_name = 'Van Rossum'
full_name = first_name + " " + last_name
print(full_name)

# Example 17

first_name = 'Guido'
last_name = 'Van Rossum'
full_name = first_name + " " + last_name

message = full_name.title() + ' ' + \
    "is the creator of Python programming language."
    
print(message)

print(f"{full_name.title()} is the creator of Python programming language.")#Using f-string to format the message

print("Hello everyone!")

print("\tHello everyone!")

print("Hello \teveryone!")

print("Hello everyone!")

print("\nHello everyone!")

print("Hello \neveryone!")

print("\n \n \nHello everyone!")

# Example 18

name = ' James '

print(name.lstrip()) #Remove whitespace from the left side of the string
print(name.rstrip()) #Remove whitespace from the right side of the string
print(name.strip()) #Remove whitespace from both sides of the string

# Example 19

name = ' James '

print('-'+ name.lstrip() + '-')

print('-'+ name.rstrip() + '-')

print('-'+ name.strip() + '-')

print('-'+ name.lstrip().title() + '-')

# Example 20

x = input("Please enter a value: ") #Insert number 6
print("The value of x is:", x)

# Example 21

x = input("x: ")
y = input("y: ")

print(x,"+",y,"=", x+y)

# Example 22

x = 17
print("The value of x was:", x)

x=x+2
print("The value of x is:", x)

# Example 23

a = 42
b = 3.14
c = "Hello, World!"

print(type(a))
print(type(b))
print(type(c))

# Example 24
x = int(input())
y = float(input())


print("x = ", x)
print("y = ", y)
print("x + y = ", x + y)
z = 'This is a string: "' + str(x+y) + '"'
print(z)

# Example 25

my_list = ["infomration", "data", "1", True, 5.6, "cherry"]
print(my_list)

# Or create an empty list with the list() function
my_list_2 = list()
print(my_list_2)

# Lists allow different data types
my_list_3 = [5, True, "apple"]
print(my_list_3)

# Lists allow duplicates
my_list_4 = [0, 0, 1, 1, "apple", "apple", "apple"]
print(my_list_4)

# Example 26
item = list_1[0]
print(item)
# You can also use negative indexing, e.g -1 refers to the last item,
# -2 to the second last item, and so on
item = list_1[-1]
print(item)

# Example 27: Lists can be altered after their creation
list_1[2] = "lemon"
print(list_1)

# Example 28
my_list = ["banana", "cherry", "apple"]
# len() : get the number of elements in a list
print("Length:", len(my_list))
# append() : adds an element to the end of the list
my_list.append("orange")
# insert() : adds an element at the specified position
my_list.insert(1, "blueberry")
print(my_list)
# pop() : removes and returns the item at the given position, default is the␣
֒→last item
item = my_list.pop()
print("Popped item: ", item)
# remove() : removes an item from the list
my_list.remove("cherry") # Value error if not in the list
print(my_list)
# clear() : removes all items from the list
my_list.clear()
print(my_list)

# reverse() : reverse the items
my_list = ["banana", "cherry", "apple"]
my_list.reverse()
print('Reversed: ', my_list)
# sort() : sort items in ascending order
my_list.sort()
print('Sorted: ', my_list)
# use sorted() to get a new list, and leave the original unaffected.
# sorted() works on any iterable type, not just lists
my_list = ["banana", "cherry", "apple"]
new_list = sorted(my_list)
# create list with repeated elements
list_with_zeros = [0] * 5
print(list_with_zeros)
# concatenation
list_concat = list_with_zeros + my_list
print(list_concat)

# Example 29
list_org = ["banana", "cherry", "apple"]
# this just copies the reference to the list, so be careful
list_copy = list_org
# now modifying the copy also affects the original
list_copy.append(True)
print(list_copy)
print(list_org)
# use copy(), or list(x) to actually copy the list
# slicing also works: list_copy = list_org[:]
list_org = ["banana", "cherry", "apple"]
list_copy = list_org.copy()
# list_copy = list(list_org)
# list_copy = list_org[:]
# now modifying the copy does not affect the original
list_copy.append(True)
print(list_copy)
print(list_org)

# Example 30: a[start:stop:step], default step is 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
a[0:3] = [0] # replace sub-parts, you need an iterable here
print(a)
b = a[::2] # start to end with every second item
print(b)
a = a[::-1] # reverse the list with a negative step:
print(a)
b = a[:] # copy a list with slicing
print(b)

# Example 31
number = [1,4,6,7,8,5,9]
min_number = print("This is tha minimum number ", min(number))
max_number = print("This is tha maximum number ", max(number))

# Example 32
dogs = ['border collie',
'australian cattle dog',
'labrador retriever']
dog = dogs[0]
print(dog.title())

# Example 33
dog = dogs[0]
print(dog.title())

# Example 34
dog = dogs[-1]
print(dog.title())

# Example 35
a = [[1, 2], [3, 4]]
print(a)
print(a[0])

# Example 36
person = {"name": "James", "age": 35, "city": "Sheffield"}
# Accessing values by key
print(person["name"]) # Output: James
print(person["age"]) # Output: 35
# Adding new key-value pair
person["occupation"] = "Data Scientist"
# Modifying existing value
person["age"] = 31
