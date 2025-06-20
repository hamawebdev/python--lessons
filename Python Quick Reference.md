---
title: "Python Quick Reference"
tags: [reference, cheatsheet, python-basics, quick-guide]
type: reference
---

# 🚀 Python Quick Reference

## 📋 Basic Syntax

### Variables and Data Types
```python
# Variables
name = "Python"
age = 30
height = 5.9
is_student = True

# Data Types
str_type = "Hello"          # String
int_type = 42               # Integer
float_type = 3.14           # Float
bool_type = True            # Boolean
list_type = [1, 2, 3]       # List
tuple_type = (1, 2, 3)      # Tuple
dict_type = {"key": "value"} # Dictionary
set_type = {1, 2, 3}        # Set
```

### Operators
```python
# Arithmetic
+ - * / % ** //

# Comparison
== != < > <= >=

# Logical
and or not

# Assignment
= += -= *= /= %=
```

### Control Flow
```python
# If statements
if condition:
    # code
elif another_condition:
    # code
else:
    # code

# For loops
for item in iterable:
    # code

# While loops
while condition:
    # code
```

### Functions
```python
# Basic function
def function_name(parameter):
    return value

# Function with default parameters
def greet(name="World"):
    return f"Hello, {name}!"

# Lambda functions
square = lambda x: x ** 2
```

## 📚 Data Structures

### Lists
```python
# Creation
my_list = [1, 2, 3]
my_list = list()

# Methods
my_list.append(4)       # Add to end
my_list.insert(0, 0)    # Insert at index
my_list.remove(2)       # Remove first occurrence
my_list.pop()           # Remove and return last
my_list.sort()          # Sort in place
my_list.reverse()       # Reverse in place
```

### Dictionaries
```python
# Creation
my_dict = {"key": "value"}
my_dict = dict()

# Methods
my_dict["new_key"] = "new_value"  # Add/update
value = my_dict.get("key")        # Get value
my_dict.pop("key")                # Remove and return
my_dict.keys()                    # Get keys
my_dict.values()                  # Get values
my_dict.items()                   # Get key-value pairs
```

### Strings
```python
# Methods
text.upper()           # Uppercase
text.lower()           # Lowercase
text.strip()           # Remove whitespace
text.split(",")        # Split by delimiter
text.replace("old", "new")  # Replace substring
text.find("substring") # Find index
len(text)              # Length
```

## 🔧 Built-in Functions

```python
# Type conversion
int(), float(), str(), bool(), list(), tuple(), dict(), set()

# Math
abs(), min(), max(), sum(), round()

# Iteration
len(), range(), enumerate(), zip()

# Input/Output
print(), input()

# Type checking
type(), isinstance()
```

## 📁 File Operations

```python
# Reading files
with open("file.txt", "r") as file:
    content = file.read()

# Writing files
with open("file.txt", "w") as file:
    file.write("content")

# File modes
"r"  # Read
"w"  # Write (overwrites)
"a"  # Append
"r+" # Read and write
```

## 🎯 List Comprehensions

```python
# Basic syntax
[expression for item in iterable]

# With condition
[expression for item in iterable if condition]

# Examples
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

## 🚨 Exception Handling

```python
try:
    # risky code
    pass
except SpecificError:
    # handle specific error
    pass
except Exception as e:
    # handle any error
    print(f"Error: {e}")
else:
    # runs if no exception
    pass
finally:
    # always runs
    pass
```

## 📦 Modules and Packages

```python
# Import entire module
import math
result = math.sqrt(16)

# Import specific function
from math import sqrt
result = sqrt(16)

# Import with alias
import numpy as np
```

## 🔗 Related Topics

### 🎯 Core Concepts
- [[01_Day_Introduction/01_introduction|Introduction]] - Getting started
- [[02_Day_Variables_builtin_functions/02_variables_builtin_functions|Variables & Built-in Functions]] - Basic data handling
- [[03_Day_Operators/03_operators|Operators]] - Working with data

### 📊 Data Structures
- [[04_Day_Strings/04_strings|Strings]] - Text processing
- [[05_Day_Lists/05_lists|Lists]] - Ordered collections
- [[06_Day_Tuples/06_tuples|Tuples]] - Immutable sequences
- [[07_Day_Sets/07_sets|Sets]] - Unique collections
- [[08_Day_Dictionaries/08_dictionaries|Dictionaries]] - Key-value pairs

### 🔄 Control Flow
- [[09_Day_Conditionals/09_conditionals|Conditionals]] - Decision making
- [[10_Day_Loops/10_loops|Loops]] - Repetition
- [[13_Day_List_comprehension/13_list_comprehension|List Comprehension]] - Efficient list creation

### 🛠️ Functions & Organization
- [[11_Day_Functions/11_functions|Functions]] - Code organization
- [[12_Day_Modules/12_modules|Modules]] - Code reusability
- [[14_Day_Higher_order_functions/14_higher_order_functions|Higher Order Functions]] - Advanced functions

### 🚨 Error Handling
- [[15_Day_Python_type_errors/15_python_type_errors|Type Errors]] - Understanding errors
- [[16_Day_Exception_handling/16_exception_handling|Exception Handling]] - Graceful error management

### 📁 File & Data Operations
- [[17_Day_File_handling/17_file_handling|File Handling]] - Working with files
- [[20_Day_Web_scraping/20_web_scraping|Web Scraping]] - Data extraction

### 🏗️ Advanced Topics
- [[18_Day_Python_package_manager/18_python_package_manager|Package Manager]] - Dependencies
- [[19_Day_Classes_and_objects/19_classes_and_objects|Classes & Objects]] - Object-oriented programming
- [[21_Day_Virtual_environment/21_virtual_environment|Virtual Environment]] - Project isolation

### 🌐 Web Development
- [[22_Day_Python_web/22_python_web|Python for Web]] - Web basics
- [[23_Day_Python_with_mongodb/23_python_with_mongodb|Python with MongoDB]] - Database operations
- [[24_Day_API/24_API|APIs]] - Working with APIs
- [[25_Day_Building_API/25_building_API|Building APIs]] - Creating APIs

### 📚 Learning Resources
- [[readme|Course Overview]] - Main course index
- [[Learning Progress Tracker|Progress Tracker]] - Track your learning
- [[Python Concepts Map|Concepts Map]] - Visual topic relationships
