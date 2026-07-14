'''
data types:
- numeric : int, float, complex
- sequence : string, list, tuple, range
- mapping : dictionary
- set  : set, frozenset
- Boolean : true(1) and false(0)

'''
operators:
    - arithmetic : + - * / % ** //
    - assignment : = += -= *= /= %= **= //=  
    - comparison : == != < > <= >=
    - logical : and or not
    - bitwise : & | ^ ~ << >>
    - identity : is is not
    - membership : in not in
    '''

'''
why we use complex?


types of funtion:
 - built in
 - user defined
 - lambda or anonymous
 - Higher order function
 - genrator funtion
 - decorator funtion
'''
var = lambda a,b : a+b
print(var(2,3))

FiLe handaling:
1. opening  a file : open(file_name, mode)
2. operation on file : read read(), write, append write()
3. closing a file : close()

modes: 
   read, write , append
   read+writing(r+), writing+read(w+) reading header file, a+(append)
   binary file : rb, wb , ab
   rb+, wb+, ab+
   x
x stands for Exclusive Creation Mode.

It is used to create a new file only if it does not already exist.
   x mode is used to create a new file exclusively. If the file already exists, Python raises a FileExistsError. It is useful when you want to ensure that existing files are not overwritten accidentally.
   file_obj = open("filename.txt", 'w')

-------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
   . (Dot) Operator in Python

The dot operator (.) is used to access attributes and methods of an object.

The with keyword is used in file handling to manage files safely. It automatically closes the file after the block of code finishes execution, so there is no need to call close() manually. This makes the code cleaner and safer.

Example:

with open("data.txt", "r") as file:
    print(file.read())

---------------------
redline for one by one line reading.

readlines()
with open("data.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

 how to read file line by line in file methods --------------
To read a file line by line, the most common approach is to use a for loop with a file object. This is memory-efficient because it reads one line at a time instead of loading the entire file into memory.

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

This reads and processes each line individually.

------------------------

we are not handaling the error but handaling the termination state of the app

try:
    num = int(input("Enter number: "))
    print(num)

except ValueError:
    print("Please enter a valid integer")

    a = 10

try:
    print(a / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")

-----------------------------------
modules:
    A module is a Python file (.py) that contains functions, classes, variables, and executable code. Modules are used to organize code, promote reusability, and make large programs easier to maintain. Python supports built-in modules, user-defined modules, and third-party modules.
--------------------------------------------------------
namespace????
A namespace is a mapping between names and objects. It stores variables, functions, classes, and other identifiers. Python uses namespaces to avoid naming conflicts and follows the LEGB rule (Local, Enclosing, Global, Built-in) when searching for names.

-----------------------
import my_very_long_calculator_module as calc

print(calc.add(10, 20))
print(calc.sub(20, 10))

A module is a Python file containing reusable code such as functions, classes, and variables. To use a module in another file, we import it using the import statement. If the module name is long, we can create a short alias using the as keyword. This improves readability and reduces typing. After importing, module members can be accessed using the module name or alias.

xample:

import my_long_module_name as mlm

Then call:

mlm.function_name()

This allows code from one file to be reused in another file efficiently.


# Python Notes (Today's Complete Revision)

---

# 1. Dynamic Data Structures

## What are Dynamic Data Structures?

Dynamic data structures can grow or shrink during program execution.

Examples:

* List
* Linked List
* Stack
* Queue
* Dictionary
* Set

### Why Use Them?

* Memory is allocated when needed.
* Size is not fixed.
* Efficient insertion and deletion.

---

# 2. Garbage Collection

## What is Garbage Collection?

Garbage Collection automatically removes objects that are no longer used.

Example:

```python
a = [1, 2, 3]
a = None
```

The old list becomes unreachable and Python can free its memory.

### Why Use It?

* Prevents memory leaks.
* Automatically manages memory.

---

# 3. Classes and Objects

## Class

A blueprint for creating objects.

```python
class Student:
    pass
```

## Object

Instance of a class.

```python
s1 = Student()
```

---

# 4. Constructor (`__init__`)

A constructor runs automatically when an object is created.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

# 5. `self` Keyword

`self` refers to the current object.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

# 6. Data Types

## Numeric

```python
int
float
complex
```

Example:

```python
a = 10
b = 3.14
c = 2 + 3j
```

### Why Complex Numbers?

Used in:

* Signal Processing
* Electrical Engineering
* Scientific Computing

---

## Boolean

```python
True
False
```

Used in conditions.

```python
age = 18
print(age >= 18)
```

Output:

```text
True
```

---

## Sequence Types

### String

```python
name = "Python"
```

### List

```python
nums = [1, 2, 3]
```

### Tuple

```python
t = (1, 2, 3)
```

---

## Set Types

### Set

```python
s = {1, 2, 3}
```

### FrozenSet

Immutable set.

```python
fs = frozenset([1, 2, 3])
```

Cannot add or remove elements.

---

## Mapping Type

### Dictionary

Stores key-value pairs.

```python
student = {
    "name": "Amit",
    "age": 22
}
```

---

# 7. Indexing

Access elements using position.

```python
name = "Python"
print(name[0])
```

Output:

```text
P
```

---

## Positive Indexing

```python
name[0]
name[1]
```

---

## Negative Indexing

```python
name[-1]
name[-2]
```

---

# 8. Slicing

Extract multiple elements.

Syntax:

```python
sequence[start:end:step]
```

Example:

```python
name = "Python"

print(name[0:3])
```

Output:

```text
Pyt
```

---

# 9. Range Function

```python
range(start, stop, step)
```

Examples:

```python
range(5)
range(1, 10)
range(1, 10, 2)
```

---

# 10. Loops

## For Loop

```python
for i in range(5):
    print(i)
```

## While Loop

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

# 11. Control Flow

Controls execution of a program.

### Conditional Statements

```python
if
elif
else
```

### Loops

```python
for
while
```

### Loop Controls

```python
break
continue
pass
```

---

# 12. Leap Year Program

```python
year = int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
```

---

# 13. Functions

Reusable block of code.

```python
def greet():
    print("Hello")
```

Call:

```python
greet()
```

---

## Function Types

### No Parameters No Return

```python
def show():
    print("Hello")
```

### Parameters No Return

```python
def show(name):
    print(name)
```

### Parameters With Return

```python
def add(a, b):
    return a + b
```

---

# 14. Arguments

Actual values passed to functions.

```python
add(10, 20)
```

`10` and `20` are arguments.

---

## Types of Arguments

* Positional
* Keyword
* Default
* `*args`
* `**kwargs`

---

# 15. Lambda Function

Anonymous one-line function.

```python
square = lambda x: x*x

print(square(5))
```

Output:

```text
25
```

---

# 16. Higher Order Functions

Function that:

* Accepts another function.
* Returns a function.

Examples:

```python
map()
filter()
sorted()
```

---

# 17. Generator

Uses `yield`.

```python
def count():
    yield 1
    yield 2
```

### Why?

* Memory efficient
* Lazy evaluation

---

# 18. Decorator

Adds functionality without modifying original code.

```python
@decorator
def greet():
    pass
```

Uses:

* Logging
* Authentication
* Timing

---

# 19. Operators

## Arithmetic

```python
+
-
*
/
/
//
%
**
```

### Floor Division

```python
10 // 3
```

Output:

```text
3
```

Used when only whole numbers are needed.

---

## Comparison

```python
==
!=
>
<
>=
<=
```

Returns:

```python
True
False
```

---

## Logical

```python
and
or
not
```

---

## Bitwise

```python
&
|
^
~
<<
>>
```

Works on binary numbers.

Used in:

* Networking
* Embedded Systems
* Performance Optimization

---

## Identity

```python
is
is not
```

Checks memory identity.

```python
a = 10
c = 10

print(a is c)
```

Output:

```text
True
```

Python may reuse small integer objects.

---

## Membership

```python
in
not in
```

Example:

```python
5 in [1,2,3,4,5]
```

---

# 20. Nested For Loop

Loop inside another loop.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Used for:

* Matrix
* Patterns
* Tables
* Image Processing

---

# 21. File Handling

Used for permanent data storage.

```python
open()
```

---

## File Modes

| Mode | Meaning      |
| ---- | ------------ |
| r    | Read         |
| w    | Write        |
| a    | Append       |
| x    | Create       |
| r+   | Read/Write   |
| w+   | Write/Read   |
| a+   | Append/Read  |
| rb   | Read Binary  |
| wb   | Write Binary |

---

## Using `with`

```python
with open("data.txt", "r") as file:
    print(file.read())
```

Automatically closes file.

---

## Read Line by Line

```python
with open("data.txt") as file:
    for line in file:
        print(line.strip())
```

---

# 22. Error Handling

Handles runtime errors.

```python
try:
    pass

except:
    pass
```

### Keywords

```python
try
except
else
finally
```

Common Errors:

* ValueError
* TypeError
* ZeroDivisionError
* FileNotFoundError
* IndexError

---

# 23. Modules

Python file containing reusable code.

```python
calculator.py
```

Import:

```python
import calculator
```

Alias:

```python
import calculator as cal
```

Call:

```python
cal.add()
```

---

# 24. Namespace

Stores names and objects.

Example:

```python
x = 10
```

Namespace:

```text
"x" → 10
```

---

## LEGB Rule

```text
Local
Enclosing
Global
Built-in
```

Python searches names in this order.

---

# 25. Dot (`.`) Operator

Used to access:

* Attributes
* Methods
* Module members

Example:

```python
name.upper()
```

```python
math.sqrt()
```

```python
student.name
```

---

# 26. f-Strings

```python
name = "Amit"

print(f"Hello {name}")
```

Output:

```text
Hello Amit
```

### Why Use?

* Cleaner
* Faster
* Easy variable formatting

---

# Quick Interview Topics Checklist

✅ Dynamic Data Structures
✅ Garbage Collection
✅ Class & Object
✅ Constructor (`__init__`)
✅ `self` Keyword
✅ Data Types
✅ Complex Numbers
✅ FrozenSet
✅ Dictionary
✅ Indexing & Slicing
✅ Range
✅ Loops
✅ Control Flow
✅ Functions
✅ Arguments
✅ Lambda
✅ Higher Order Functions
✅ Generators
✅ Decorators
✅ Operators
✅ Nested Loops
✅ File Handling
✅ Error Handling
✅ Modules
✅ Namespace (LEGB)
✅ Dot Operator
✅ f-Strings

These notes cover the core Python fundamentals discussed today and are a solid revision sheet for interviews, coding rounds, and Python learning.
