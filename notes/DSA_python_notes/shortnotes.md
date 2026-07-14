# PY, PyENV, and How `print("Hello World")` Works

## 1. What is `.py`?

A **`.py`** file is a Python source code file.

Example:

```python
# hello.py
print("Hello World")
```

* `.py` = Python file extension
* Contains Python code written by the programmer

---

## 2. What is PyENV?

**PyENV** is a tool used to manage multiple Python versions on the same computer.

### Why use PyENV?

Suppose:

```text
Project A needs Python 3.10
Project B needs Python 3.12
```

Normally, only one Python version may be active.

PyENV lets you switch between versions easily.

Example:

```bash
pyenv install 3.10.5
pyenv install 3.12.0

pyenv global 3.12.0
```

### Where is it used?

* Software development
* Data science projects
* Different projects requiring different Python versions

---

# How `print("Hello World")` Works

When you run:

```python
print("Hello World")
```

A lot happens behind the scenes.

---

## Step 1: Write Source Code

```python
print("Hello World")
```

Saved in:

```text
hello.py
```

---

## Step 2: Python Interpreter Starts

When you run:

```bash
python hello.py
```

Python reads the file.

```text
hello.py
    ↓
Python Interpreter
```

---

## Step 3: Compilation

Python compiles the code into **bytecode**.

```text
Source Code
     ↓
 Compiler
     ↓
 Bytecode
```

Conceptually:

```text
print("Hello World")
     ↓
Bytecode Instructions
```

---

## Step 4: PVM Executes Bytecode

**PVM (Python Virtual Machine)** executes the bytecode.

```text
Bytecode
    ↓
PVM
    ↓
Execution
```

---

## Step 5: `print()` Function Runs

Python finds the built-in function:

```python
print()
```

It sends the text to the screen.

```text
Output Device (Console)
```

---

## Final Output

```text
Hello World
```

---

# Complete Flow Diagram

```text
hello.py
   |
   v
+----------------+
| Source Code    |
| print("Hello") |
+----------------+
        |
        v
+----------------+
| Python Compiler|
+----------------+
        |
        v
+----------------+
| Bytecode       |
+----------------+
        |
        v
+----------------+
| PVM            |
| (Interpreter)  |
+----------------+
        |
        v
+----------------+
| Console Output |
+----------------+
        |
        v
   Hello World
```

---

# Memory Representation

When:

```python
print("Hello World")
```

Python creates a string object:

```text
Heap Memory
----------------
"Hello World"
----------------
```

The `print()` function reads that string and displays it on the console.

---

## Interview Answer

### What is `.py`?

A `.py` file is a Python source code file containing Python instructions.

### What is PyENV?

PyENV is a Python version management tool that allows multiple Python versions to be installed and switched between easily.

### How does `print("Hello World")` work?

1. The code is written in a `.py` file.
2. Python compiles it into bytecode.
3. The PVM (Python Virtual Machine) executes the bytecode.
4. The built-in `print()` function sends the string to the console.
5. The output `Hello World` appears on the screen.




Yes, this is the correct flow of a Python program.

### Example

```python
print("Hello World")
```

### Execution Flow

```text
1. Source Code (.py file)
        |
        v
2. Python Interpreter
        |
        v
3. Compile Time
   - Checks Syntax
   - Converts to Bytecode
        |
        v
4. Runtime (PVM)
   - Executes Bytecode
        |
        v
5. Output
   - Hello World
```

### Detailed Flow

```text
hello.py
   |
   v
+------------------+
| Python           |
| Interpreter      |
+------------------+
   |
   v
+------------------+
| Compile Time     |
| Syntax Checking  |
| Bytecode Create  |
+------------------+
   |
   v
+------------------+
| Runtime          |
| PVM Executes     |
| Bytecode         |
+------------------+
   |
   v
+------------------+
| Output Screen    |
+------------------+
   |
   v
Hello World
```

### What Happens at Each Step?

#### 1. Python Interpreter

Reads the `.py` file.

```python
print("Hello World")
```

#### 2. Compile Time

Python checks:

```python
print("Hello World")
```

for syntax errors.

Example:

```python
print("Hello World"
```

Gives:

```text
SyntaxError
```

Then Python converts code into **Bytecode**.

#### 3. Runtime (PVM)

PVM = Python Virtual Machine

It executes the bytecode instruction by instruction.

#### 4. Output

```text
Hello World
```

appears on the console.

---

### Interview Answer

**Python Program Execution Flow:**

```text
Source Code (.py)
      ↓
Python Interpreter
      ↓
Compile Time
(Syntax Check + Bytecode Generation)
      ↓
Runtime (PVM Execution)
      ↓
Output
```

* **Compile Time** → Syntax checking and bytecode generation.
* **Runtime** → PVM executes the bytecode.
* **Output** → Result displayed on the screen.


# Difference Between List and Tuple in Python

| Feature      | List              | Tuple              |
| ------------ | ----------------- | ------------------ |
| Syntax       | `[]`              | `()`               |
| Mutable      | Yes (can change)  | No (cannot change) |
| Performance  | Slower            | Faster             |
| Memory Usage | More memory       | Less memory        |
| Methods      | Many methods      | Few methods        |
| Use Case     | Data that changes | Fixed data         |

---

## 1. Syntax

### List

```python
my_list = [1, 2, 3]
```

### Tuple

```python
my_tuple = (1, 2, 3)
```

---

## 2. Mutability

### List (Mutable)

You can add, remove, or modify elements.

```python
numbers = [1, 2, 3]

numbers[0] = 10

print(numbers)
```

Output:

```text
[10, 2, 3]
```

### Tuple (Immutable)

You cannot modify elements.

```python
numbers = (1, 2, 3)

numbers[0] = 10
```

Output:

```text
TypeError: 'tuple' object does not support item assignment
```

---

## 3. Methods

### List Methods

```python
lst = [1, 2, 3]

lst.append(4)
lst.remove(2)
lst.insert(1, 100)
```

### Tuple Methods

Only a few methods:

```python
t = (1, 2, 3, 1)

print(t.count(1))
print(t.index(2))
```

---

## 4. Memory

Tuple uses less memory because it cannot be changed.

```python
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
```

Tuple is more memory-efficient.

---

## 5. Speed

Tuple is faster than List because it is immutable.

---

## Example

### List

```python
students = ["Amit", "Rahul", "Riya"]

students.append("Priya")

print(students)
```

Output:

```text
['Amit', 'Rahul', 'Riya', 'Priya']
```

### Tuple

```python
students = ("Amit", "Rahul", "Riya")

print(students)
```

Output:

```text
('Amit', 'Rahul', 'Riya')
```

---

## When to Use List?

Use a **List** when data can change.

Examples:

* Student records
* Shopping cart
* To-do list

```python
cart = ["Laptop", "Mouse"]
```

---

## When to Use Tuple?

Use a **Tuple** when data should remain fixed.

Examples:

* Days of the week
* Months of the year
* Coordinates

```python
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
```

---

## Easy Memory Trick

```text
List  = Can Change
Tuple = Cannot Change
```

```text
[]  → List
()  → Tuple
```

## Interview Answer

**List** is a mutable collection that allows adding, removing, and modifying elements. It is created using square brackets `[]`.

**Tuple** is an immutable collection that cannot be modified after creation. It is created using parentheses `()`.

Lists are used when data changes frequently, while tuples are used for fixed data.


What is range() in Python?

range() is a built-in Python function used to generate a sequence of numbers.

It is commonly used with loops.

Syntax
range(start, stop, step)

evrey sequencail deta type work sequence
Indexing ----------------------------------------------------

Index is the position of an element in a sequence. Python uses zero-based indexing, meaning the first element has index 0, the second has index 1, and so on. Negative indexing starts from the end, where -1 refers to the last element.

set - unorder data in sequence

# Set Theory (Short Notes)

A **Set** is a collection of **unique elements**.

Example:

```python
A = {1, 2, 3, 4}
```

---

## Types of Sets

### 1. Empty Set

No elements.

```python
A = set()
```

---

### 2. Finite Set

Limited number of elements.

```python
A = {1, 2, 3}
```

---

### 3. Infinite Set

Unlimited elements.

```text
N = {1, 2, 3, 4, ...}
```

---

## Set Operations

### Union ( ∪ )

Combines all elements.

```text
A = {1,2,3}
B = {3,4,5}

A ∪ B = {1,2,3,4,5}
```

### Intersection ( ∩ )

Common elements.

```text
A ∩ B = {3}
```

### Difference ( - )

Elements in A but not in B.

```text
A - B = {1,2}
```

### Symmetric Difference

Elements in either set but not both.

```text
A △ B = {1,2,4,5}
```

---

## Python Example

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)   # Union
print(A & B)   # Intersection
print(A - B)   # Difference
```

---

## Interview Answer

**Set Theory** is a branch of mathematics that deals with collections of unique elements called sets. Common operations are **Union, Intersection, Difference, and Symmetric Difference**. In Python, sets are represented using `{}` and do not allow duplicate values.


# Nested Dictionary in Python

A **Nested Dictionary** is a dictionary inside another dictionary.

### Syntax

```python
student = {
    "name": "Amit",
    "marks": {
        "Math": 90,
        "Science": 85
    }
}
```

Here, `"marks"` is a dictionary inside the main dictionary.

---

## Example

```python
students = {
    "s1": {
        "name": "Amit",
        "age": 21
    },
    "s2": {
        "name": "Rahul",
        "age": 22
    }
}

print(students)
```

Output:

```text
{
 's1': {'name': 'Amit', 'age': 21},
 's2': {'name': 'Rahul', 'age': 22}
}
```

---

## Accessing Values

```python
print(students["s1"]["name"])
```

Output:

```text
Amit
```

Explanation:

```text
students["s1"]        -> {'name':'Amit','age':21}
students["s1"]["name"] -> Amit
```

---

## Updating a Value

```python
students["s1"]["age"] = 25
print(students)
```

---

## Looping Through Nested Dictionary

```python
for key, value in students.items():
    print(key, value)
```

Output:

```text
s1 {'name': 'Amit', 'age': 21}
s2 {'name': 'Rahul', 'age': 22}
```

---

## Real-Life Example

```python
employees = {
    101: {"name": "Alice", "salary": 50000},
    102: {"name": "Bob", "salary": 60000}
}

print(employees[101]["salary"])
```

Output:

```text
50000
```

---

## Interview Answer

A **Nested Dictionary** is a dictionary that contains one or more dictionaries as values. It is used to store structured and hierarchical data, such as student records, employee information, or product details.



---------------------------  boolean -----------------------
# Boolean (`bool`) in Python

A **Boolean** is a data type that has only **two values**:

```text
True
False
```

---

## Creating Boolean Values

```python
a = True
b = False

print(a)
print(b)
```

Output:

```text
True
False
```

---

## Type of Boolean

```python
a = True
print(type(a))
```

Output:

```text
<class 'bool'>
```

---

## Boolean in Comparisons

Python returns `True` or `False` when comparing values.

```python
print(10 > 5)
print(10 < 5)
print(10 == 10)
```

Output:

```text
True
False
True
```

---

## Boolean with `if`

```python
age = 18

if age >= 18:
    print("Eligible to Vote")
```

Output:

```text
Eligible to Vote
```

Condition evaluates to `True`.

---

## Boolean Conversion

```python
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Hello"))
```

Output:

```text
True
False
False
True
```

### Rules

```text
0      → False
None   → False
""     → False
[]     → False
{}     → False

Any non-zero number or non-empty value → True
```

---

## Real-Life Example

```python
is_logged_in = True

if is_logged_in:
    print("Welcome User")
```

Output:

```text
Welcome User
```

---

## Interview Answer

**Boolean (`bool`) is a Python data type that represents logical values. It has only two possible values: `True` and `False`. Boolean values are commonly used in comparisons, conditions, and decision-making statements such as `if`, `while`, and logical operations.**

####  control flow
# Control Flow in Python

**Control Flow** determines the order in which statements are executed in a program.

It controls the flow of execution based on conditions and loops.

---

## Types of Control Flow

### 1. Conditional Statements

Used to make decisions.

### `if`

```python
age = 18

if age >= 18:
    print("Eligible")
```

Output:

```text
Eligible
```

---

### `if-else`

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

Output:

```text
Not Eligible
```

---

### `if-elif-else`

```python
marks = 75

if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("C")
```

Output:

```text
B
```

---

## 2. Loops

Used to repeat code.

### `for` Loop

```python
for i in range(3):
    print(i)
```

Output:

```text
0
1
2
```

---

### `while` Loop

```python
i = 1

while i <= 3:
    print(i)
    i += 1
```

Output:

```text
1
2
3
```

---

## 3. Loop Control Statements

### `break`

Stops the loop.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

Output:

```text
0
1
2
```

---

### `continue`

Skips the current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:

```text
0
1
3
4
```

---

### `pass`

Placeholder; does nothing.

```python
for i in range(3):
    pass
```

---

## Flow Diagram

```text
Start
  |
  v
Condition?
  |
True ------> Execute Block
  |
False
  |
 End
```

---

## Interview Answer

**Control Flow** is the order in which a program's statements are executed. In Python, control flow is managed using **conditional statements (`if`, `elif`, `else`)**, **loops (`for`, `while`)**, and **control statements (`break`, `continue`, `pass`)**. These help the program make decisions and repeat tasks.
