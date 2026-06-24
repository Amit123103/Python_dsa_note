with keyword:
The with statement is used for resource management in Python. It automatically handles setup and cleanup operations, such as opening and closing files, making code safer, cleaner, and easier to read.

Global Scope:
A variable declared outside all functions is called a global variable. It belongs to the global scope and can be accessed throughout the program. To modify it inside a function, the global keyword must be used.

A namespace is a container that stores variable names and their values.

Python mainly has:

Built-in Namespace
Global Namespace
Local Namespace

LEGB Rule

Python searches for variables in this order:

L → Local Namespace
E → Enclosing Namespace
G → Global Namespace
B → Built-in Namespace


Global Namespace:
The global namespace is a dictionary-like structure that stores all names (variables, functions, classes, imported modules) defined at the top level of a Python program. It exists throughout the program's execution and can be accessed using the globals() function.




OOPs (Object-Oriented Programming)
# OOPs (Object-Oriented Programming) in Python

**OOP (Object-Oriented Programming)** is a programming paradigm that organizes code using **Classes** and **Objects**.

It helps in:

* Code reusability
* Better organization
* Easy maintenance
* Real-world modeling

---

# 1. Class

A **Class** is a blueprint or template for creating objects.

### Example

```python
class Student:
    pass
```

Here, `Student` is a class.

---

# 2. Object

An **Object** is an instance of a class.

```python
class Student:
    pass

s1 = Student()
s2 = Student()
```

Here:

* `s1` and `s2` are objects.

---

# Real-Life Example

### Class = Car Blueprint

```text
Class  → Car
Object → BMW, Audi, Tesla
```

### Class = Student Template

```text
Class  → Student
Object → Amit, Rahul, Priya
```

---

# Constructor (`__init__()`)

A constructor is a special method that runs automatically when an object is created.

```python
class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Amit")

print(s1.name)
```

Output:

```text
Amit
```

---

# What is `self`?

`self` refers to the current object.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

When:

```python
s1 = Student("Amit")
```

Python internally does:

```python
Student.__init__(s1, "Amit")
```

So:

```python
self = s1
```

---

# Attributes (Variables)

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Amit", 22)

print(s1.name)
print(s1.age)
```

Output:

```text
Amit
22
```

---

# Methods (Functions Inside Class)

```python
class Student:

    def greet(self):
        print("Hello Student")

s1 = Student()

s1.greet()
```

Output:

```text
Hello Student
```

---

# Four Pillars of OOP

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

---

# 1. Encapsulation

Binding data and methods together into a single unit (class).

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

Data and methods are wrapped together.

---

# 2. Inheritance

One class acquires properties of another class.

```python
class Parent:

    def show(self):
        print("Parent Class")

class Child(Parent):
    pass

c = Child()
c.show()
```

Output:

```text
Parent Class
```

### Benefit

Code reuse.

---

# 3. Polymorphism

One method behaves differently in different situations.

```python
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()
```

Output:

```text
Bark
Meow
```

Same method name → different behavior.

---

# 4. Abstraction

Hiding implementation details and showing only essential features.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")
```

User only knows:

```python
car.start()
```

Implementation is hidden.

---

# Types of Inheritance

## Single Inheritance

```python
class A:
    pass

class B(A):
    pass
```

---

## Multilevel Inheritance

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

---

## Multiple Inheritance

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

---

# Method Overriding

Child class provides its own implementation.

```python
class Parent:

    def show(self):
        print("Parent")

class Child(Parent):

    def show(self):
        print("Child")

c = Child()
c.show()
```

Output:

```text
Child
```

---

# `super()` Function

Used to call parent class methods.

```python
class Parent:

    def __init__(self):
        print("Parent Constructor")

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child Constructor")

c = Child()
```

Output:

```text
Parent Constructor
Child Constructor
```

---

# Interview Definitions

### Class

A class is a blueprint used to create objects.

### Object

An object is an instance of a class.

### Constructor

A special method (`__init__`) that initializes an object.

### Inheritance

A mechanism where one class acquires properties and methods of another class.

### Polymorphism

The ability of the same method to perform different actions.

### Encapsulation

Wrapping data and methods into a single unit.

### Abstraction

Hiding implementation details and showing only essential functionality.

---

# Quick Revision

```text
Class        → Blueprint
Object       → Instance of Class
self         → Current Object
__init__()   → Constructor

OOP Pillars:
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

Inheritance Types:
1. Single
2. Multilevel
3. Multiple

super()      → Call Parent Class
Overriding   → Redefine Parent Method
```

This covers the core OOP concepts typically asked in Python interviews and exams.

Why do we need OOP?

Object-Oriented Programming is used to organize code into classes and objects. It improves code reusability, maintainability, security, and scalability. OOP models real-world entities and provides features such as encapsulation, inheritance, polymorphism, and abstraction, making large applications easier to develop and manage.

One-Line Answer

We use OOP to make programs modular, reusable, secure, and easier to maintain, especially for large applications.

In OOP interviews, **physical and logical objects** are often explained like this:

## 1. Physical Objects

Physical objects are things that exist in the real world and have a physical presence.

### Examples

```text
Car
Mobile Phone
Laptop
Fan
Book
Chair
```

### OOP Representation

```python
class Car:
    color = "Red"
    
    def start(self):
        print("Car Started")
```

Here, a car is a physical object.

---

## 2. Logical Objects

Logical objects do not physically exist. They are concepts, processes, or software entities.

### Examples

```text
Bank Account
Student Record
Order
Employee Record
Shopping Cart
ATM Transaction
```

You cannot touch them physically, but they exist in software.

### OOP Representation

```python
class BankAccount:
    
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

A bank account is a logical object.

---

## Comparison

| Physical Object | Logical Object  |
| --------------- | --------------- |
| Car             | Bank Account    |
| Mobile          | Shopping Cart   |
| Book            | Student Record  |
| Laptop          | Employee Record |
| Fan             | Online Order    |

---

## Interview Answer

**Physical Objects:** Real-world entities that have a physical existence, such as a car, laptop, or mobile phone.

**Logical Objects:** Software-based entities that do not physically exist but represent concepts or processes, such as a bank account, student record, or shopping cart.

### Memory Trick

```text
Can I touch it?
Yes  → Physical Object
No   → Logical Object
```

Examples:

```text
Car            → Physical
Mobile          → Physical

Bank Account    → Logical
Student Record  → Logical
Online Order    → Logical
```
OOP Workflow

Problem
   ↓
Objects
   ↓
Attributes (Data)
   ↓
Methods (Behavior)
   ↓
Class
   ↓
Object
   ↓
Method Calls


---- class varibales
# Class Variables in Python

A **class variable** is a variable that belongs to the **class itself**, not to individual objects.

* Shared by all objects of the class.
* Defined inside the class but outside methods.

---

## Example

```python
class Student:
    school = "ABC School"   # Class Variable

s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)
```

Output:

```text
ABC School
ABC School
```

Both objects use the same `school` variable.

---

## Why Use Class Variables?

Use class variables when a value is common to all objects.

Examples:

```text
School Name
Company Name
College Name
Interest Rate
Employee Count
```

---

## Class Variable vs Instance Variable

### Class Variable

```python
class Student:
    school = "ABC School"
```

Shared by all students.

### Instance Variable

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Each student has a different name.

---

## Example

```python
class Student:
    school = "ABC School"   # Class Variable

    def __init__(self, name):
        self.name = name    # Instance Variable

s1 = Student("Amit")
s2 = Student("Rahul")

print(s1.name)
print(s2.name)

print(s1.school)
print(s2.school)
```

Output:

```text
Amit
Rahul
ABC School
ABC School
```

---

## Changing a Class Variable

```python
class Student:
    school = "ABC School"

Student.school = "XYZ School"

s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)
```

Output:

```text
XYZ School
XYZ School
```

All objects see the updated value.

---

## Accessing Class Variables

### Using Class Name (Preferred)

```python
print(Student.school)
```

### Using Object

```python
print(s1.school)
```

Both work, but using the class name is clearer.

---

## Real-Life Example

```python
class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

e1 = Employee("Amit")
e2 = Employee("Rahul")

print(e1.company)
print(e2.company)
```

Output:

```text
Google
Google
```

The company is the same for every employee.

---

## Interview Answer

**Class Variable:**
A class variable is a variable that is shared by all instances (objects) of a class. It is declared inside the class and outside any method. Class variables are used to store data common to all objects.

### Example

```python
class Student:
    school = "ABC School"
```

Here, `school` is a class variable shared by all `Student` objects.

### Memory Trick

```text
Class Variable    → Shared by all objects
Instance Variable → Separate copy for each object
```

Example:

```text
school = ABC School  → Class Variable

Amit's name          → Instance Variable
Rahul's name         → Instance Variable
```
# `__init__()` Method and `self` in Python

These are two of the most important OOP concepts.

---

# 1. What is `__init__()`?

`__init__()` is a **special method (constructor)** that runs automatically when an object is created.

### Example

```python
class Student:

    def __init__(self):
        print("Constructor Called")

s1 = Student()
```

### Output

```text
Constructor Called
```

When:

```python
s1 = Student()
```

Python automatically calls:

```python
Student.__init__(s1)
```

---

# Why Use `__init__()`?

To initialize object data.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Amit", 22)
```

Now every object gets its own data.

---

# 2. What is `self`?

`self` refers to the **current object**.

When an object calls a method, Python automatically passes that object as the first argument.

### Example

```python
class Student:

    def show(self):
        print("Hello")

s1 = Student()

s1.show()
```

Python internally does:

```python
Student.show(s1)
```

So:

```python
self = s1
```

---

# Why Do We Need `self`?

Without `self`, Python cannot know which object's data you are referring to.

### Example

```python
class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Amit")
s2 = Student("Rahul")
```

Object data:

```text
s1.name = Amit
s2.name = Rahul
```

`self` helps Python access the correct object's data.

---

# Visual Understanding

```python
class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Amit")
```

Internally:

```python
Student.__init__(s1, "Amit")
```

Therefore:

```text
self = s1
name = "Amit"
```

And:

```python
self.name = name
```

becomes:

```python
s1.name = "Amit"
```

---

# Complete Example

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student("Amit", 22)
s2 = Student("Rahul", 21)

s1.display()
s2.display()
```

Output:

```text
Amit 22
Rahul 21
```

### Internally

```python
s1.display()
```

becomes:

```python
Student.display(s1)
```

and

```python
s2.display()
```

becomes:

```python
Student.display(s2)
```

---

# Important Rule

Inside a class:

```python
self.variable
```

means:

```text
variable belonging to the current object
```

Example:

```python
self.name
self.age
self.salary
```

---

# Interview Definitions

### `__init__()`

`__init__()` is a special constructor method that is automatically called when an object is created. It is used to initialize object attributes.

### `self`

`self` is a reference to the current object. It allows access to the object's attributes and methods inside the class.

---

# Memory Trick

```text
Student()      → Create Object

__init__()     → Runs Automatically

self           → Current Object

self.name      → Current Object's Name
self.age       → Current Object's Age
```

### Example

```python
class Student:

    def __init__(self, name):
        self.name = name
```

For:

```python
s1 = Student("Amit")
```

Think:

```text
self = s1
self.name = "Amit"
```

So the object `s1` stores the value `"Amit"` in its `name` attribute.




# Python OOP (Object-Oriented Programming) Notes

## 1. What is OOP?

OOP (Object-Oriented Programming) is a programming approach that organizes code using Classes and Objects.

Benefits:

* Code Reusability
* Easy Maintenance
* Better Organization
* Real-world Modeling
* Security through Encapsulation

---

# 2. Class

A Class is a blueprint or template used to create objects.

Example:

class Student:
pass

Think:

Class → Student
Object → Amit, Rahul, Priya

---

# 3. Object

An Object is an instance of a class.

Example:

class Student:
pass

s1 = Student()
s2 = Student()

Here:

* Student = Class
* s1, s2 = Objects

---

# 4. Why Do We Need OOP?

Without OOP:

* Too many variables
* Difficult maintenance
* Code duplication

With OOP:

* Organized code
* Reusable code
* Easier debugging

Example:

class Student:
pass

class Teacher:
pass

class Course:
pass

---

# 5. Constructor (**init**)

A constructor runs automatically when an object is created.

Example:

class Student:

```
def __init__(self, name):
    self.name = name
```

s1 = Student("Amit")

Purpose:

* Initialize object data
* Assign values to variables

---

# 6. What is self?

self refers to the current object.

Example:

class Student:

```
def __init__(self, name):
    self.name = name
```

s1 = Student("Amit")

Internally:

Student.**init**(s1, "Amit")

self = s1

Therefore:

self.name = name

becomes:

s1.name = "Amit"

---

# 7. Instance Variable

Variables belonging to an object.

Example:

class Student:

```
def __init__(self, name):
    self.name = name
```

Each object gets its own copy.

Example:

s1 = Student("Amit")
s2 = Student("Rahul")

s1.name = Amit
s2.name = Rahul

---

# 8. Class Variable

Shared by all objects.

Example:

class Student:

```
school = "ABC School"

def __init__(self, name):
    self.name = name
```

Here:

school = Class Variable
name = Instance Variable

---

# 9. Methods

Functions inside a class.

Example:

class Student:

```
def greet(self):
    print("Hello")
```

s1 = Student()
s1.greet()

---

# 10. Inheritance

Inheritance allows one class to acquire properties and methods of another class.

Example:

class Shape:
pass

class Circle(Shape):
pass

Shape = Parent Class
Circle = Child Class

Benefits:

* Code Reuse
* Less Duplication

Types:

1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance

---

# 11. Encapsulation

Wrapping data and methods together into one unit.

Example:

class Student:

```
def __init__(self, name):
    self.name = name

def display(self):
    print(self.name)
```

---

# 12. Polymorphism

Same method name, different behavior.

Example:

class Dog:
def sound(self):
print("Bark")

class Cat:
def sound(self):
print("Meow")

---

# 13. Abstraction

Hiding implementation details and showing only essential features.

Example:

ATM Machine

You know:

* Withdraw
* Deposit

You don't know:

* Internal coding

---

# 14. Circle Class Example

class Circle:

```
def __init__(self, radius):
    self.radius = radius

def area(self):
    return 3.14 * self.radius * self.radius

def perimeter(self):
    return 2 * 3.14 * self.radius
```

Object:

c = Circle(5)

Formulas:
Area = πr²
Perimeter = 2πr

---

# 15. Person Class Example

from datetime import date

class Person:

```
def __init__(self, name, country, birth_year):
    self.name = name
    self.country = country
    self.birth_year = birth_year

def age(self):
    return date.today().year - self.birth_year
```

Purpose:

* Store personal details
* Calculate age

---

# 16. Calculator Class Example

class Calculator:

```
def add(self, a, b):
    return a + b

def subtract(self, a, b):
    return a - b

def multiply(self, a, b):
    return a * b

def divide(self, a, b):
    return a / b
```

Operations:

* Addition
* Subtraction
* Multiplication
* Division

---

# 17. Shape Class with Inheritance

class Shape:
pass

class Circle(Shape):
pass

class Square(Shape):
pass

Architecture:

Shape
|
|-- Circle
|
|-- Square

Inheritance Example.

---

# 18. Binary Search Tree (BST)

Definition:

A Binary Search Tree is a binary tree where:

Left Child < Parent
Right Child > Parent

Example:

```
    10
   /  \
  5    20
 / \
3   7
```

Rules:

Smaller → Left
Greater → Right

---

# BST Node Example

class Node:

```
def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
```

root = Node(10)

root.left = Node(5)
root.right = Node(20)

---

# BST Operations

1. Insert
2. Search

Example:

root.insert(5)
root.insert(20)
root.insert(3)

Tree:

```
    10
   /  \
  5    20
 /
3
```

Search:

root.search(20)

Output:
Found

---

# Interview Quick Revision

Class        → Blueprint

Object       → Instance of Class

Constructor  → **init**()

self         → Current Object

Method       → Function inside Class

Instance Variable → Object Specific

Class Variable → Shared by All Objects

Inheritance  → Reuse Parent Class

Encapsulation → Bind Data + Methods

Polymorphism → Same Method Different Behavior

Abstraction  → Hide Internal Details

BST Rule:
Smaller → Left
Greater → Right
