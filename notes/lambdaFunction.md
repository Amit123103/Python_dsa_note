# Lambda Function in Python

## What is a Lambda Function?

A **Lambda Function** is a small anonymous (nameless) function in Python.

Normally, we create functions using the `def` keyword. But for simple operations that are used only once, Python provides **lambda functions**.

### Syntax

```python
lambda arguments: expression
```

* `lambda` → keyword to create lambda function
* `arguments` → input parameters
* `expression` → single statement whose result is returned automatically

---

## Why Do We Use Lambda Functions?

We use lambda functions when:

1. The function is small and simple.
2. We need a function only once.
3. We want to avoid writing a full `def` function.
4. We need to pass a function as an argument to another function.

---

## Normal Function vs Lambda Function

### Using def

```python
def square(x):
    return x * x

print(square(5))
```

**Output**

```python
25
```

### Using Lambda

```python
square = lambda x: x * x

print(square(5))
```

**Output**

```python
25
```

---

# How Lambda Works

```python
add = lambda a, b: a + b

print(add(10, 20))
```

**Output**

```python
30
```

Equivalent Normal Function:

```python
def add(a, b):
    return a + b
```

---

# Where Do We Use Lambda?

Most commonly with:

1. `map()`
2. `filter()`
3. `reduce()`
4. `sorted()`
5. `max()`
6. `min()`

---

# 1. Lambda with map()

### Purpose

Apply a function to every item in a list.

### Example

```python
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

**Output**

```python
[2, 4, 6, 8, 10]
```

### Explanation

Each element is multiplied by 2.

---

# 2. Lambda with filter()

### Purpose

Select elements based on a condition.

### Example

```python
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)
```

**Output**

```python
[2, 4, 6]
```

### Explanation

Only even numbers are returned.

---

# 3. Lambda with reduce()

### Purpose

Combine all elements into a single value.

```python
from functools import reduce

result = reduce(lambda x, y: x + y, [1, 2, 3, 4])

print(result)
```

**Output**

```python
10
```

### Explanation

```
1+2=3
3+3=6
6+4=10
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

sorted_students = sorted(
    students,
    key=lambda x: x[1]
)

print(sorted_students)
```

**Output**

```python
[
 ('Amit', 80),
 ('Priya', 85),
 ('Rahul', 95)
]
```

### Explanation

Sorting based on marks (`x[1]`).

---

# 5. Lambda with max()

```python
students = [
    ("Amit", 80),
    ("Rahul", 95),
    ("Priya", 85)
]

highest = max(
    students,
    key=lambda x: x[1]
)

print(highest)
```

**Output**

```python
('Rahul', 95)
```

---

# 6. Lambda with min()

```python
students = [
    ("Amit", 80),
    ("Rahul", 95),
    ("Priya", 85)
]

lowest = min(
    students,
    key=lambda x: x[1]
)

print(lowest)
```

**Output**

```python
('Amit', 80)
```

---

# Multiple Arguments in Lambda

```python
multiply = lambda a, b: a * b

print(multiply(5, 4))
```

**Output**

```python
20
```

---

# Lambda with Conditional Expression

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))
```

**Output**

```python
Even
Odd
```

---

# When Should You Use Lambda?

Use Lambda When:

✅ Small one-line functions

✅ Inside `map()`, `filter()`, `sorted()`

✅ Temporary functions

✅ Function passed as argument

Example:

```python
names = ["amit", "rahul", "priya"]

result = sorted(names, key=lambda x: len(x))

print(result)
```

---

# When NOT to Use Lambda?

Avoid Lambda When:

❌ Logic is large

❌ Multiple statements are needed

❌ Complex conditions exist

❌ Function will be reused many times

Bad Example:

```python
lambda x:
    if x > 10:
        return x
```

Lambda cannot contain multiple statements.

Use normal function instead:

```python
def check(x):
    if x > 10:
        return x
```

---

# How to Identify When Lambda is Needed?

Ask yourself:

### Question 1

Is the function very small?

**Yes → Lambda**

```python
lambda x: x * 2
```

### Question 2

Will I use the function only once?

**Yes → Lambda**

### Question 3

Am I passing a function to `map`, `filter`, `sorted`, `max`, or `min`?

**Yes → Lambda**

### Question 4

Does the function contain many lines?

**Yes → Use `def`**

---

# Interview Definition

> A Lambda Function is an anonymous, single-expression function in Python created using the `lambda` keyword. It is mainly used for short, temporary operations and is commonly used with functions such as `map()`, `filter()`, `reduce()`, and `sorted()`.

## Quick Revision

| Feature             | Lambda                    |
| ------------------- | ------------------------- |
| Name Required       | No                        |
| Keyword             | lambda                    |
| Return Statement    | Automatic                 |
| Multiple Statements | No                        |
| Best For            | Small Functions           |
| Common Use          | map(), filter(), sorted() |

### Most Common Real-Life Example

```python
students = [
    ("Amit", 80),
    ("Rahul", 95),
    ("Priya", 85)
]

students.sort(key=lambda x: x[1])

print(students)
```

This is one of the most common uses of lambda functions in Python projects and interviews.
