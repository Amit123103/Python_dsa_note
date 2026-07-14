# Python Notes (Today's Complete Revision)

# 1. Lambda Function

## What is Lambda?

A lambda function is a small anonymous function.

### Syntax

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x ** 2

print(square(5))
```

Output:

```text
25
```

---

## Why Use Lambda?

* Small one-line functions
* Temporary functions
* Used with `map()`, `filter()`, `sorted()`
* Avoid writing full `def`

Example:

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

---

# 2. Lambda with map()

### Purpose

Apply a function to every element.

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x ** 2, numbers))

print(result)
```

Output:

```text
[1, 4, 9, 16]
```

---

# 3. Lambda with filter()

### Purpose

Filter elements based on condition.

```python
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)
```

Output:

```text
[2, 4, 6]
```

---

# 4. Lambda with sorted()

### Example

```python
students = [
    ("Amit", 80),
    ("Rahul", 95),
    ("Priya", 85)
]

students.sort(key=lambda x: x[1])
```

Sorts by marks.

---

# 5. Understanding x[0], x[1], x[2]

Tuple:

```python
student = ("Amit", 80, "Red")
```

| Index | Value |
| ----- | ----- |
| 0     | Amit  |
| 1     | 80    |
| 2     | Red   |

Access:

```python
student[0]
student[1]
student[2]
```

Output:

```text
Amit
80
Red
```

---

# 6. Why x[1] in Lambda?

```python
students.sort(key=lambda x: x[1])
```

Each x is:

```python
("Amit",80)
```

Python takes:

```python
x[1]
```

which means:

```python
80
95
85
```

and sorts according to marks.

---

# 7. If Color Exists

```python
items = [
    ("Apple",50,"Red"),
    ("Banana",20,"Yellow"),
    ("Grapes",80,"Green")
]
```

| Index | Meaning |
| ----- | ------- |
| 0     | Name    |
| 1     | Price   |
| 2     | Color   |

Sort by color:

```python
items.sort(key=lambda x: x[2])
```

---

# 8. Tuple vs Dictionary

### Tuple

```python
("Amit",80,"Red")
```

Access:

```python
x[0]
x[1]
x[2]
```

---

### Dictionary

```python
{
    "name":"Amit",
    "marks":80,
    "color":"Red"
}
```

Access:

```python
x["name"]
x["marks"]
x["color"]
```

---

# 9. Why KeyError: 2 Happened?

Your data:

```python
phones = [
 {'make':'Nokia','model':216,'color':'Black'}
]
```

Wrong:

```python
lambda x: x[2]
```

Because dictionary has keys, not indexes.

Correct:

```python
lambda x: x['color']
```

---

# 10. startswith()

Checks whether a string begins with a character.

```python
name = "Python"

print(name.startswith("P"))
```

Output:

```text
True
```

---

# 11. Lambda with startswith()

```python
check = lambda x: x.startswith('P')

print(check("Python"))
```

Output:

```text
True
```

---

# 12. **init**() Method

## What is **init**()?

Special method automatically called when an object is created.

### Example

```python
class Student:

    def __init__(self,name):
        self.name = name

s1 = Student("Amit")
```

Python automatically calls:

```python
Student.__init__(s1,"Amit")
```

---

## **init** is

* Constructor
* Special Method
* Instance Method

---

# 13. Polymorphism

## Meaning

One Name, Many Forms

Same method behaves differently.

### Example

```python
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")
```

```python
Dog().sound()
Cat().sound()
```

Output:

```text
Bark
Meow
```

---

# 14. Method Overriding

Parent method is replaced by child method.

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")
```

```python
obj = Child()

obj.show()
```

Output:

```text
Child
```

---

# 15. Overriding vs Overloading

## Overriding

Uses inheritance.

```python
class Parent:
    def show(self):
        pass

class Child(Parent):
    def show(self):
        pass
```

---

## Overloading

Same function name, different parameters.

Python does not support true overloading.

Wrong:

```python
def abc(a,b):
    pass

def abc(a,b,c):
    pass
```

Second function replaces first.

---

# 16. Why abc(2,3) Gives Error?

Code:

```python
def abc(a,b):
    pass

def abc(a,b,c):
    pass
```

Python keeps only:

```python
def abc(a,b,c):
    pass
```

Now:

```python
abc(2,3)
```

Error:

```text
TypeError
missing argument c
```

---

# 17. Correct Way for Overloading-Like Behavior

### Using Default Arguments

```python
def abc(a,b,c=None):

    if c is None:
        print(a+b)

    else:
        print(a+b+c)
```

```python
abc(2,3)
abc(2,3,4)
```

Output:

```text
5
9
```

---

# 18. *args

Accept multiple arguments.

```python
def abc(*args):
    print(sum(args))
```

```python
abc(2,3)
abc(2,3,4)
abc(2,3,4,5)
```

Output:

```text
5
9
14
```

---

# 19. Scope

Scope = Region where variable can be used.

---

## Local Scope

```python
def show():
    x = 10
```

Accessible only inside function.

---

## Global Scope

```python
x = 100
```

Accessible throughout file.

---

## Enclosing Scope

```python
def outer():

    x = 20

    def inner():
        print(x)
```

---

## Built-in Scope

```python
print()
len()
max()
```

Built into Python.

---

# 20. LEGB Rule

Python searches variables in this order:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

---

# 21. Namespace

Namespace stores variable names and values.

Example:

```python
x = 10
name = "Amit"
```

Namespace:

```python
{
    "x":10,
    "name":"Amit"
}
```

---

# Types of Namespace

## Built-in Namespace

```python
print
len
max
```

---

## Global Namespace

```python
x = 100
```

---

## Local Namespace

```python
def show():
    a = 10
```

---

# Namespace vs Scope

| Namespace       | Scope                  |
| --------------- | ---------------------- |
| Stores names    | Controls access        |
| Dictionary-like | Visibility rules       |
| Example: x=10   | Example: Local, Global |

---

# Most Important Interview Questions

### Q1. What is Lambda?

A small anonymous one-line function.

### Q2. Why use x[1]?

To access the second value of a tuple.

### Q3. Why KeyError in Dictionary?

Because dictionaries use keys, not indexes.

### Q4. What is **init**?

A constructor automatically called when an object is created.

### Q5. What is Polymorphism?

One name, many forms.

### Q6. What is Method Overriding?

Child class replaces parent method.

### Q7. Does Python support Overloading?

No. Use default arguments or `*args`.

### Q8. What is Scope?

Region where a variable is accessible.

### Q9. What is Namespace?

Storage that maps names to objects.

### Q10. What is LEGB?

```text
Local → Enclosing → Global → Built-in
```

This is the complete revision of all major concepts we discussed today: Lambda Functions, Indexing, Dictionaries, `startswith()`, Constructors (`__init__`), Polymorphism, Method Overriding, Overloading, `*args`, Scope, Namespace, and the LEGB rule.

# Abstraction in Python

## What is Abstraction?

**Abstraction** means:

> **Hiding implementation details and showing only the essential features to the user.**

In simple words:

* User knows **what to do**
* User doesn't need to know **how it works internally**

---

# Real-Life Example

### ATM Machine

When you withdraw money:

1. Insert card
2. Enter PIN
3. Get cash

You don't know:

* How the bank server works
* How the balance is checked
* How transactions are processed

Those details are hidden.

This is **Abstraction**.

---

# Another Example

### Car

You know:

```text
Start Car
Accelerate
Brake
```

You don't know:

```text
Fuel Injection
Engine Timing
Piston Movement
```

Hidden details = Abstraction.

---

# Why Do We Use Abstraction?

### 1. Hide Complexity

Users see only necessary information.

### 2. Increase Security

Internal implementation remains hidden.

### 3. Easy Maintenance

Internal code can change without affecting users.

### 4. Better Design

Programs become cleaner and easier to use.

---

# Abstraction in Python

Python provides abstraction using the:

```python id="txmsna"
ABC
@abstractmethod
```

from the `abc` module.

---

# Abstract Class

An abstract class is a class that contains one or more abstract methods.

### Example

```python id="2x3u80"
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

Here:

* `Animal` is an abstract class.
* `sound()` is an abstract method.

---

# Why Can't We Create an Object?

```python id="m0s5b8"
a = Animal()
```

Error:

```text id="g3mj2z"
TypeError:
Can't instantiate abstract class
```

Because abstract classes are incomplete.

---

# Child Class Must Implement Abstract Method

```python id="ebpkfd"
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog Barks")
```

Create object:

```python id="md6l3z"
d = Dog()
d.sound()
```

Output:

```text id="x77skv"
Dog Barks
```

---

# What is an Abstract Method?

A method declared but not implemented.

```python id="tvp5wi"
@abstractmethod
def sound(self):
    pass
```

The child class must provide the implementation.

---

# Example: Shape

```python id="qk7lh7"
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

Child class:

```python id="s6n7lf"
class Circle(Shape):

    def area(self):
        print("Area of Circle")
```

```python id="6jlwmj"
c = Circle()

c.area()
```

Output:

```text id="a9h3xq"
Area of Circle
```

---

# Without Abstraction

```python id="a7vzpc"
class Animal:

    def sound(self):
        pass
```

A programmer may forget to implement `sound()`.

With abstraction:

```python id="4n1zjp"
@abstractmethod
def sound(self):
    pass
```

Python forces the child class to implement it.

---

# Abstraction vs Encapsulation

| Abstraction                       | Encapsulation                    |
| --------------------------------- | -------------------------------- |
| Hides implementation              | Hides data                       |
| Focuses on what                   | Focuses on how                   |
| Achieved using abstract classes   | Achieved using private variables |
| User sees only necessary features | Protects data                    |

---

## Example

### Abstraction

```text
ATM Machine
```

User sees:

```text
Withdraw
Deposit
Check Balance
```

Internal working is hidden.

---

### Encapsulation

```python id="1qnzkt"
class Bank:

    def __init__(self):
        self.__balance = 1000
```

Balance is protected from direct access.

---

# OOP Pillars

There are four main OOP concepts:

1. **Encapsulation**
2. **Abstraction**
3. **Inheritance**
4. **Polymorphism**

---

# Interview Definition

> Abstraction is an OOP concept that hides implementation details and exposes only essential functionality to the user. In Python, abstraction is achieved using abstract classes and abstract methods provided by the `abc` module.

---

# Quick Revision

### Abstract Class

```python id="tqg6v7"
class Animal(ABC):
```

Cannot create object directly.

---

### Abstract Method

```python id="ujjlwm"
@abstractmethod
def sound(self):
    pass
```

Must be implemented by child class.

---

### Complete Example

```python id="3bz2vq"
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog Barks")

d = Dog()
d.sound()
```

Output:

```text id="g7qu8v"
Dog Barks
```

### Memory Trick

```text
Abstraction = Hide Implementation
Encapsulation = Hide Data
Inheritance = Acquire Properties
Polymorphism = One Name, Many Forms
```

These four concepts are the foundation of Object-Oriented Programming (OOP).

Hiding the user data 

# def abc(a,b):
#     pass
# def abc(a, b,c):  #  function over riding  
#     pass
# abc(2,3)
# abc(2,3,4)

## `__add__()` in Python

`__add__()` is a **magic method** (also called a **dunder method**, because it has double underscores).

It defines what should happen when the **`+` operator** is used with objects.

### Syntax

```python
def __add__(self, other):
    pass
```

* `self` → current object
* `other` → object being added

---

## Why do we use `__add__()`?

Normally, `+` works with built-in types:

```python
print(5 + 3)          # 8
print("Hi" + " All")  # Hi All
```

But for our own classes, Python doesn't know how to add objects.

Example:

```python
class Student:
    pass

s1 = Student()
s2 = Student()

print(s1 + s2)
```

Output:

```text
TypeError: unsupported operand type(s) for +
```

To tell Python how to add two objects, we define `__add__()`.

---

## Example 1: Adding Two Numbers in Objects

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)
```

Output:

```text
30
```

### What happens internally?

```python
n1 + n2
```

Python converts this to:

```python
n1.__add__(n2)
```

---

## Example 2: Student Marks

```python
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks


s1 = Student(80)
s2 = Student(90)

print(s1 + s2)
```

Output:

```text
170
```

---

## Where is `__add__()` used?

### 1. Operator Overloading

Making operators work with custom objects.

```python
obj1 + obj2
```

### 2. Banking Systems

```python
account1 + account2
```

Combine balances.

### 3. Shopping Cart

```python
cart1 + cart2
```

Combine items.

### 4. Vector Mathematics

```python
v1 + v2
```

Add vectors.

### 5. Student Records

```python
s1 + s2
```

Add marks or scores.

---

## Real Example: Vector Addition

```python
class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Vector(self.x + other.x)

    def __str__(self):
        return str(self.x)


v1 = Vector(5)
v2 = Vector(10)

print(v1 + v2)
```

Output:

```text
15
```

---

## Common Magic Methods

| Method          | Operator | Example  |
| --------------- | -------- | -------- |
| `__add__()`     | `+`      | `a + b`  |
| `__sub__()`     | `-`      | `a - b`  |
| `__mul__()`     | `*`      | `a * b`  |
| `__truediv__()` | `/`      | `a / b`  |
| `__lt__()`      | `<`      | `a < b`  |
| `__gt__()`      | `>`      | `a > b`  |
| `__eq__()`      | `==`     | `a == b` |

---

## Interview Answer

**What is `__add__()`?**

`__add__()` is a special (magic) method used to overload the `+` operator for user-defined classes. When we write `obj1 + obj2`, Python internally calls `obj1.__add__(obj2)`. It allows us to define how two objects should be added together.


-------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Enviroument where our program excuted 


I think you're asking:

> **"Where does our program go at compile time and runtime?"**

### Program Execution Flow

```text
Source Code (.py)
       |
       v
   Compiler
       |
       v
 Byte Code (.pyc)
       |
       v
 Python Virtual Machine (PVM)
       |
       v
     Output
```

---

## Compile Time

**Compile Time** is when the source code is checked and converted into another form before execution.

In Python:

```python
a = 10
b = 20
print(a + b)
```

Python first converts it into **Bytecode**.

```text
Source Code
     ↓
Compiler
     ↓
Bytecode (.pyc)
```

### What happens at Compile Time?

* Syntax checking
* Code translation to bytecode

Example:

```python
print("Hello"
```

Output:

```text
SyntaxError: '(' was never closed
```

This error is found during compilation.

---

## Runtime

**Runtime** is when the program is actually executing.

```text
Bytecode
    ↓
PVM (Python Virtual Machine)
    ↓
Execution
```

Example:

```python
a = 10
b = 0
print(a / b)
```

Output:

```text
ZeroDivisionError
```

The syntax is correct, so compilation succeeds.
The error occurs while the program is running → Runtime Error.

---

## Memory Representation

```text
           RAM (Memory)
      -------------------
      | Code Segment    |
      -------------------
      | Stack Memory    |
      -------------------
      | Heap Memory     |
      -------------------
```

### Stack Memory

Stores:

* Function calls
* Local variables

Example:

```python
x = 10
```

### Heap Memory

Stores:

* Objects
* Lists
* Dictionaries
* Class objects

Example:

```python
lst = [1, 2, 3]
```

The list object is stored in Heap Memory.

---

## Compile Time vs Runtime

| Compile Time     | Runtime                         |
| ---------------- | ------------------------------- |
| Before execution | During execution                |
| Syntax checking  | Actual execution                |
| Creates bytecode | Runs bytecode                   |
| SyntaxError      | RuntimeError, ZeroDivisionError |

---

### Interview Answer

**Compile Time** is the phase where Python converts source code into bytecode and checks for syntax errors. **Runtime** is the phase where the Python Virtual Machine (PVM) executes the bytecode. Syntax errors occur at compile time, while errors like division by zero occur at runtime.

runtime where our whole progam run or excute



