# Python program to demonstrate variables and different data types

# Integer
age = 20
print("Age:", age, "| Data Type:", type(age))

# Float
pi = 3.14159
print("Pi:", pi, "| Data Type:", type(pi))

# String
name = "Ashwin"
print("Name:", name, "| Data Type:", type(name))

# Boolean
is_student = True
print("Is Student:", is_student, "| Data Type:", type(is_student))

# List (ordered, mutable collection)
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits, "| Data Type:", type(fruits))

# Tuple (ordered, immutable collection)
coordinates = (10.5, 20.3)
print("Coordinates:", coordinates, "| Data Type:", type(coordinates))

# Set (unordered, unique elements)
unique_numbers = {1, 2, 3, 3, 4}
print("Unique Numbers:", unique_numbers, "| Data Type:", type(unique_numbers))

# Dictionary (key-value pairs)
student = {"name": "Ashwin", "age": 20, "grade": "A"}
print("Student:", student, "| Data Type:", type(student))

# NoneType
nothing = None
print("Nothing:", nothing, "| Data Type:", type(nothing))


# output
'''
Age: 20 | Data Type: <class 'int'>
Pi: 3.14159 | Data Type: <class 'float'>
Name: Ashwin | Data Type: <class 'str'>
Is Student: True | Data Type: <class 'bool'>
Fruits: ['apple', 'banana', 'cherry'] | Data Type: <class 'list'>
Coordinates: (10.5, 20.3) | Data Type: <class 'tuple'>
Unique Numbers: {1, 2, 3, 4} | Data Type: <class 'set'>
Student: {'name': 'Ashwin', 'age': 20, 'grade': 'A'} | Data Type: <class 'dict'>
Nothing: None | Data Type: <class 'NoneType'>
'''