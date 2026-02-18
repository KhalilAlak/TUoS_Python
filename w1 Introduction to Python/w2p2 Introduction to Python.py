# EXAMPLE 1
y = 1
if y == 1:
    print("y still equals 1, I was just checking")


# EXAMPLE 2
a = 1
if a > 5:
    print("This shouldn't happen.")
else:
    print("This should happen.")


# EXAMPLE 3
z = 4
if z > 70:
    print("Something is very wrong")
elif z < 7:
    print("This is normal")


# EXAMPLE 4
a = 0
while a < 10:
    a = a + 1
    print(a)


# EXAMPLE 5
x = 10
while x != 0:
    print(x)
    x = x - 1
print("wow, we've counted x down, and now it equals", x)
print("And now the loop has ended.")


# EXAMPLE 6
print("We will show the even numbers up to 20")
n = 1
while n <= 20:
    if n % 2 == 0:
        print(n)
    n = n + 1
print("there, done.")


# Indentation example
a = 10
while a > 0:
    print(a)
    if a > 5:
        print("Big number!")
    elif a % 2 != 0:
        print("This is an odd number")
        print("It isn't greater than five, either")
    else:
        print("this number isn't greater than 5")
        print("nor is it odd")
        print("feeling special?")
    a = a - 1
    print("we just made 'a' one less than what it was!")
    print("and unless a is not greater than 0, we'll do the loop again.")
print("well, it seems as if 'a' is now no bigger than 0!")
print("the loop is now over, and without furthur adue, so is this program!")


# EXAMPLE 8
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print("I love ", fruit)

fruits = ["apple", "banana", "orange"]
for x in fruits:
    print("I love ", x)


# EXAMPLE 9
for char in "hello":
    print(char.upper())

for i in range(5):
    print(i**2)


# EXAMPLE 10
newList = [
    45,
    'eat me',
    90210,
    "The day has come, the walrus said, \
to speak of many things",
    -67
]

for value in newList:
    print(value)


# EXAMPLE 12
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element)


# EXAMPLE 13
student_data = {
    "Alice": {"age": 20, "subjects": ["Math", "Physics"]},
    "Bob": {"age": 22, "subjects": ["English", "History"]}
}

for name, info in student_data.items():
    print(f"Name: {name}")
    for key, value in info.items():
        print(f"{key.title()}: {value}")


# Function examples
len()
round
print(round(3.14))
len(round(3.14))
print(max(len('hi', len('hello'))))


# Default arguments
round(3.712)
round(3.712, 1)

round(3.000, 2)
round(2, 3.000)


# Help function
help(round)


# Databricks dataset examples
display(dbutils.fs.ls("/databricks-datasets"))

display(dbutils.fs.ls("/databricks-datasets/Rdatasets/"))

df = spark.read.csv(
    "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv",
    header=True,
    inferSchema=True
)
display(df)

df_1 = spark.read.format('csv') \
    .options(header='true', inferSchema='true') \
    .load('/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv')
display(df_1)
