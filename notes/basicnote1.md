Python Complete Quick Notes (Based on Our Discussion)
1. What is Python?
Python is a high-level, interpreted, object-oriented programming language.
Easy to learn and widely used in AI, ML, Data Science, Web Development, and Automation.
print("Hello World")
2. Data Types
Numeric Types
x = 10      # int
y = 3.14    # float
z = 2 + 3j  # complex
Complex Number
x = 3 + 4j

print(x.real)
print(x.imag)

Output:

3.0
4.0
String
name = "Amit"
Boolean
is_student = True
List
numbers = [10,20,30]
Tuple
data = (10,20,30)
Set
s = {1,2,3}
Frozen Set

Immutable version of set.

fs = frozenset([1,2,3])

Cannot add or remove elements.

Dictionary
student = {
    "name":"Amit",
    "age":22
}
None Type
x = None
3. Variables
name = "Amit"
age = 22
4. Indexing

Accessing a single element.

name = "Python"

print(name[0])

Output:

P
Positive Indexing
P  y  t  h  o  n
0  1  2  3  4  5
Negative Indexing
P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
print(name[-1])

Output:

n
5. Slicing

Extracting part of a sequence.

Syntax
sequence[start:stop:step]

Example:

name = "Python"

print(name[1:4])

Output:

yth

Common:

s[:3]
s[2:]
s[::2]
s[::-1]
6. Control Flow

Controls program execution.

If Else
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
7. Loops
For Loop
for i in range(5):
    print(i)
While Loop
i = 1

while i <= 5:
    print(i)
    i += 1
8. Loop Control Statements
Break
for i in range(10):
    if i == 5:
        break
Continue
for i in range(5):
    if i == 2:
        continue
Pass
if True:
    pass
9. range() Function
Syntax
range(start, stop, step)

Examples:

range(5)
range(1,6)
range(1,11,2)

Descending:

range(10,0,-1)

Create List:

numbers = list(range(1,101))
10. Functions

Reusable block of code.

Creating Function
def greet():
    print("Hello")

Calling:

greet()
Function with Parameters
def greet(name):
    print(name)
Function with Return
def add(a,b):
    return a+b
11. Parameter vs Argument
def add(a,b):
    return a+b
a,b → Parameters
add(10,20)
10,20 → Arguments
12. Multiple Values
Multiple Parameters
def add(a,b,c):
    return a+b+c
Return Multiple Values
def info():
    return "Amit",22
*args

Variable positional arguments.

def add(*args):
    return sum(args)
**kwargs

Variable keyword arguments.

def student(**kwargs):
    print(kwargs)
13. Generator and Yield

Generator produces values one by one.

def numbers():
    yield 1
    yield 2
    yield 3

Using:

g = numbers()

print(next(g))
Yield vs Return
Return	Yield
Ends Function	Pauses Function
Returns Once	Returns Many Times
More Memory	Less Memory
14. Object Oriented Programming (OOP)
Class

Blueprint for creating objects.

class Student:
    pass
Object
s = Student()
15. Constructor

Special method automatically called during object creation.

class Student:

    def __init__(self,name):
        self.name = name
16. self Keyword

Represents current object.

class Student:

    def __init__(self,name):
        self.name = name
s = Student("Amit")

Here:

self.name = "Amit"
17. Linked List Node

Node contains:

Data Part

Stores value.

Link Part

Stores reference.

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

Visualization:

+---------+---------+
|  Data   |  Next   |
+---------+---------+
18. Dynamic Data Structure

Memory allocated at runtime.

Examples:

Linked List
Stack
Queue
Tree
Graph

Advantages:

Flexible Size
Efficient Memory
Easy Insertion & Deletion
19. Garbage Collection

Automatically removes unused objects from memory.

Example:

x = [1,2,3]

x = None

Object becomes unreachable and can be garbage collected.

20. Dictionary (Mapping)

Stores key-value pairs.

student = {
    "name":"Amit",
    "age":22
}

Access:

student["name"]

Methods:

student.keys()
student.values()
student.items()
21. Set Theory
Union
A | B
Intersection
A & B
Difference
A - B
Symmetric Difference
A ^ B
22. Leap Year Program
year = int(input())

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
23. Create List 1 to 100
numbers = list(range(1,101))

Ascending Order:

1,2,3,4,...,100
Python Interview Revision Sheet
Data Types
int
float
complex
str
bool
list
tuple
set
frozenset
dict
NoneType
OOP
Class
Object
Constructor (__init__)
self
Functions
Parameters
Arguments
Return
*args
**kwargs
yield
Control Flow
if
elif
else
for
while
break
continue
pass
Collections
List
Tuple
Set
FrozenSet
Dictionary
Important Concepts
Indexing
Slicing
Dynamic Memory
Garbage Collection
Linked List Node
Set Theory
Leap Year Logic

These notes cover all the Python concepts discussed in this conversation in a structured interview-friendly format.
>>>>>>>>>
by deafault user data type in string 

typcasting
Type Casting in Python

Type Casting means converting one data type into another data type.

Why Type Casting?

Sometimes data is in one format, but we need it in another.

Example:

x = "10"
y = 20

# Error:
# print(x + y)

Convert string to integer:

x = int("10")
y = 20

print(x + y)

Output:

30
Types of Type Casting
1. Implicit Type Casting

Python automatically converts one data type to another.

a = 10
b = 2.5

c = a + b

print(c)
print(type(c))

Output:

12.5
<class 'float'>

Python automatically converts int to float.

2. Explicit Type Casting

The programmer manually converts the data type.

int()
x = "100"

y = int(x)

print(y)
print(type(y))

Output:

100
<class 'int'>
float()
x = "10.5"

y = float(x)

print(y)

Output:

10.5
str()
x = 100

y = str(x)

print(y)
print(type(y))

Output:

100
<class 'str'>
bool()
print(bool(1))
print(bool(0))

Output:

True
False
list()
name = "Python"

print(list(name))

Output:

['P', 'y', 't', 'h', 'o', 'n']
tuple()
nums = [1, 2, 3]

print(tuple(nums))

Output:

(1, 2, 3)
set()
nums = [1, 2, 2, 3]

print(set(nums))

Output:

{1, 2, 3}
dict()
data = [('name', 'Amit'), ('age', 22)]

print(dict(data))

Output:

{'name': 'Amit', 'age': 22}
Common Examples
User Input
age = int(input("Enter Age: "))

input() always returns a string, so we convert it to int.

Float to Int
x = 10.9

print(int(x))

Output:

10

Note: Decimal part is removed, not rounded.

Quick Conversion Table
Function	Converts To
int()	Integer
float()	Float
str()	String
bool()	Boolean
list()	List
tuple()	Tuple
set()	Set
dict()	Dictionary
Interview Answer

Type Casting is the process of converting a value from one data type to another. Python supports:

Implicit Type Casting (automatic conversion by Python)
Explicit Type Casting (manual conversion using functions like int(), float(), str(), etc.)

Example:

x = "10"
y = int(x)

print(y + 5)

Output:

15


