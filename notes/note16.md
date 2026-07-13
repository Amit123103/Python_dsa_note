Yes, your understanding is almost correct. Here's a clearer version with proper comments:

```python
# 1. Normal Arguments
def adf(arg1, arg2):
    # Must pass exactly 2 positional arguments
    pass


# 2. *args
def adf(*args):
    # Can pass any number of positional arguments
    # Stored as a tuple
    pass


# 3. **kwargs
def adf(**kwargs):
    # Can pass any number of keyword arguments
    # Stored as a dictionary
    pass
```

### Examples

#### 1. Normal Arguments

```python
def adf(a, b):
    print(a, b)

adf(10, 20)      # ✅
# adf(10)        # ❌ Error
# adf(10,20,30)  # ❌ Error
```

---

#### 2. `*args`

```python
def adf(*args):
    print(args)

adf(10)
adf(10, 20)
adf(10, 20, 30, 40)
```

Output:

```python
(10,)
(10, 20)
(10, 20, 30, 40)
```

---

#### 3. `**kwargs`

```python
def adf(**kwargs):
    print(kwargs)

adf(name="Amit", age=22, city="Delhi")
```

Output:

```python
{'name': 'Amit', 'age': 22, 'city': 'Delhi'}
```

---

### Quick Revision

| Syntax              | Accepts                            | Stores As  | Example                    |
| ------------------- | ---------------------------------- | ---------- | -------------------------- |
| `def fun(a, b)`     | Exactly 2 arguments                | Variables  | `fun(10, 20)`              |
| `def fun(*args)`    | Any number of positional arguments | Tuple      | `fun(10, 20, 30)`          |
| `def fun(**kwargs)` | Any number of keyword arguments    | Dictionary | `fun(name="Amit", age=22)` |

### Memory Trick

* **Normal arguments** → Fixed number of values.
* **`*args`** → `*` = many **positional** arguments → **Tuple**.
* **`**kwargs`** → `**` = many **keyword** (`key=value`) arguments → **Dictionary**.
Besides `**kwargs`, Python also has several other kinds of function arguments.

## 1. Positional Arguments

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

---

## 2. Keyword Arguments

You pass arguments using the parameter names.

```python
def student(name, age):
    print(name, age)

student(name="Amit", age=22)
student(age=22, name="Amit")   # Order doesn't matter
```

---

## 3. Default Arguments

A parameter has a default value.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Amit")
```

Output:

```
Hello Guest
Hello Amit
```

---

## 4. Variable Positional Arguments (`*args`)

Accepts any number of positional arguments.

```python
def add(*numbers):
    print(numbers)

add(10, 20, 30)
```

Output:

```
(10, 20, 30)
```

---

## 5. Variable Keyword Arguments (`**kwargs`)

Accepts any number of keyword arguments.

```python
def student(**details):
    print(details)

student(name="Amit", age=22, city="Delhi")
```

Output:

```
{'name': 'Amit', 'age': 22, 'city': 'Delhi'}
```

---

## 6. Keyword-Only Arguments

Using `*` forces the following parameters to be passed by keyword.

```python
def student(name, *, age):
    print(name, age)

student("Amit", age=22)   # ✅
# student("Amit", 22)     # ❌ Error
```

---

## 7. Positional-Only Arguments (Python 3.8+)

Using `/` forces the preceding parameters to be positional.

```python
def divide(a, b, /):
    print(a / b)

divide(10, 2)      # ✅
# divide(a=10, b=2) # ❌ Error
```

---

## Summary

| Argument Type       | Syntax              | Example            |
| ------------------- | ------------------- | ------------------ |
| Positional          | `def fun(a, b)`     | `fun(10, 20)`      |
| Keyword             | `def fun(a, b)`     | `fun(a=10, b=20)`  |
| Default             | `def fun(a=10)`     | `fun()`            |
| Variable Positional | `def fun(*args)`    | `fun(1, 2, 3)`     |
| Variable Keyword    | `def fun(**kwargs)` | `fun(name="Amit")` |
| Keyword-Only        | `def fun(*, a)`     | `fun(a=10)`        |
| Positional-Only     | `def fun(a, /)`     | `fun(10)`          |

These are the main types of arguments you will encounter in Python.



| Call                     | Type                | How Python Matches                             |
| ------------------------ | ------------------- | ---------------------------------------------- |
| `asdf(8, 9)`             | Positional argument | By **position** (1st → `args1`, 2nd → `args2`) |
| `asdf(args1=8, args2=9)` | Keyword argument    | By **parameter name**                          |
| `asdf(args2=9, args1=8)` | Keyword argument    | By **parameter name**, so order doesn't matter |


If you mean **file handling access modes** (not access modifiers), these are the modes used with `open()`.

## File Handling Access Modes

### Syntax

```python
file = open("filename.txt", "mode")
```

---

## 1. `r` – Read Mode

* Opens an existing file for reading.
* Error if the file does not exist.
* File pointer starts at the beginning.

```python
file = open("data.txt", "r")
print(file.read())
file.close()
```

---

## 2. `w` – Write Mode

* Opens a file for writing.
* Creates the file if it doesn't exist.
* Overwrites all existing content.

```python
file = open("data.txt", "w")
file.write("Hello")
file.close()
```

---

## 3. `a` – Append Mode

* Opens a file for appending.
* Creates the file if it doesn't exist.
* Adds data to the end of the file.

```python
file = open("data.txt", "a")
file.write("\nWelcome")
file.close()
```

---

## 4. `x` – Create Mode

* Creates a new file.
* Raises an error if the file already exists.

```python
file = open("new.txt", "x")
file.close()
```

---

## 5. `r+` – Read and Write

* Opens an existing file.
* Allows both reading and writing.
* Does **not** create a new file.

```python
file = open("data.txt", "r+")
print(file.read())
file.write(" Python")
file.close()
```

---

## 6. `w+` – Write and Read

* Allows both writing and reading.
* Creates the file if it doesn't exist.
* Overwrites existing content.

```python
file = open("data.txt", "w+")
file.write("Hello")
file.seek(0)
print(file.read())
file.close()
```

---

## 7. `a+` – Append and Read

* Allows reading and appending.
* Creates the file if it doesn't exist.
* New data is added to the end.

```python
file = open("data.txt", "a+")
file.write("\nPython")
file.seek(0)
print(file.read())
file.close()
```

---

## 8. `rb` – Read Binary

Used for binary files such as images, videos, or PDFs.

```python
file = open("image.jpg", "rb")
data = file.read()
file.close()
```

---

## 9. `wb` – Write Binary

Writes binary data to a file.

```python
file = open("image_copy.jpg", "wb")
# file.write(binary_data)
file.close()
```

---

## Summary Table

| Mode | Read | Write |   Create File   | Overwrite | Append |
| ---- | :--: | :---: | :-------------: | :-------: | :----: |
| `r`  |   ✅  |   ❌   |        ❌        |     ❌     |    ❌   |
| `w`  |   ❌  |   ✅   |        ✅        |     ✅     |    ❌   |
| `a`  |   ❌  |   ✅   |        ✅        |     ❌     |    ✅   |
| `x`  |   ❌  |   ✅   | ✅ (only if new) |     ❌     |    ❌   |
| `r+` |   ✅  |   ✅   |        ❌        |     ❌     |    ❌   |
| `w+` |   ✅  |   ✅   |        ✅        |     ✅     |    ❌   |
| `a+` |   ✅  |   ✅   |        ✅        |     ❌     |    ✅   |
| `rb` |   ✅  |   ❌   |        ❌        |     ❌     |    ❌   |
| `wb` |   ❌  |   ✅   |        ✅        |     ✅     |    ❌   |

### Interview Definition

> **File access modes are the different modes used with the `open()` function to specify how a file should be accessed, such as reading (`r`), writing (`w`), appending (`a`), or creating (`x`).**


You can specify a file or folder by its **path**. A path tells Python where the file or folder is located.

---

# 1. File in the Same Folder

If your Python file and the text file are in the same folder:

```
Project/
│── main.py
│── data.txt
```

```python
import os

os.remove("data.txt")
```

---

# 2. File Inside a Folder

Suppose your project looks like this:

```
Project/
│── main.py
│
└── Files/
    │── data.txt
```

Delete the file:

```python
import os

os.remove("Files/data.txt")
```

or on Windows:

```python
import os

os.remove("Files\\data.txt")
```

---

# 3. File with Full Path

```python
import os

os.remove(r"C:\Users\Amit\Desktop\data.txt")
```

The `r` before the string means **raw string**, so you don't need to escape the backslashes.

Without `r`, you would write:

```python
os.remove("C:\\Users\\Amit\\Desktop\\data.txt")
```

---

# 4. Delete an Empty Folder

```
Project/
│── main.py
│
└── MyFolder/
```

```python
import os

os.rmdir("MyFolder")
```

---

# 5. Delete a Folder with Files

```
Project/
│── main.py
│
└── MyFolder/
    │── data.txt
    │── image.jpg
```

```python
import shutil

shutil.rmtree("MyFolder")
```

---

# 6. Check Before Deleting

```python
import os

path = "Files/data.txt"

if os.path.exists(path):
    os.remove(path)
    print("File Deleted")
else:
    print("File Not Found")
```

---

# 7. Current Working Directory

To see where Python is looking for files:

```python
import os

print(os.getcwd())
```

Example output:

```
C:\Users\Amit\Desktop\Python
```

If `data.txt` is in this folder:

```python
os.remove("data.txt")
```

works correctly.

---

# Summary

| Task                     | Code                                           |
| ------------------------ | ---------------------------------------------- |
| Delete file              | `os.remove("data.txt")`                        |
| Delete file in folder    | `os.remove("Files/data.txt")`                  |
| Delete using full path   | `os.remove(r"C:\Users\Amit\Desktop\data.txt")` |
| Delete empty folder      | `os.rmdir("MyFolder")`                         |
| Delete folder with files | `shutil.rmtree("MyFolder")`                    |
| Check if file exists     | `os.path.exists(path)`                         |
| Get current folder       | `os.getcwd()`                                  |

## Example Folder Structure

```
Python/
│── main.py
│
├── Notes/
│   ├── file1.txt
│   └── file2.txt
│
└── Images/
    └── photo.jpg
```

Delete `file1.txt`:

```python
import os

os.remove("Notes/file1.txt")
```

Delete the `Images` folder (if it's empty):

```python
import os

os.rmdir("Images")
```

Delete the `Notes` folder and everything inside it:

```python
import shutil

shutil.rmtree("Notes")
```

The important idea is that you pass the **path** to the file or folder you want to delete. Python uses that path to locate the item on your computer.


import os

path = "Files/data.txt"

if os.path.exists(path):
    os.remove(path)
    print("File Deleted")
else:
    print("File Not Found")

raise: for our Own exception '


Assert: terminate the excution of block


Yes. Here is a simple explanation:

## `raise`

`raise` is used to **create our own exception manually**.

### Syntax:

```python
raise Exception("Error Message")
```

### Example:

```python
age = 15

if age < 18:
    raise Exception("Age must be 18 or above")
```

**Output:**

```text
Exception: Age must be 18 or above
```

You can also create your own exception class:

```python
class InvalidAge(Exception):
    pass

age = 15

if age < 18:
    raise InvalidAge("Invalid Age")
```

---

## `assert`

`assert` is used for **debugging and checking conditions**.

If the condition is `False`, it raises an `AssertionError` and **terminates the execution**.

### Syntax:

```python
assert condition, "message"
```

### Example:

```python
x = -5

assert x > 0, "Number must be positive"
```

**Output:**

```text
AssertionError: Number must be positive
```

---

# `try`, `except`, `finally`

### `try`

Contains the code that may produce an error.

### `except`

Handles the error if it occurs.

### `finally`

Always executes, whether an exception occurs or not.

### Example:

```python
try:
    a = 10
    b = 0
    print(a/b)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program Ended")
```

**Output:**

```text
Cannot divide by zero
Program Ended
```

---

# Difference Table

| Keyword   | Purpose                                                         |
| --------- | --------------------------------------------------------------- |
| `raise`   | Manually generate our own exception                             |
| `assert`  | Check condition for debugging; raises `AssertionError` if false |
| `try`     | Write risky code                                                |
| `except`  | Handle exceptions                                               |
| `finally` | Executes always                                                 |

---

### Short Exam Definition

* **Raise:** Used to explicitly throw our own exception.
* **Assert:** Used to test conditions during debugging; if the condition is false, execution stops with `AssertionError`.
* **Try-Except-Finally:** Mechanism to handle runtime errors and ensure cleanup code always executes.

Q: Why do we use finally?

Answer:
The finally block is used to execute important cleanup code such as closing files, database connections, or releasing resources. It runs regardless of whether an exception occurs.

Short Definition for Exam

finally is used to execute a block of code that must run under all circumstances, whether an exception occurs or not.


