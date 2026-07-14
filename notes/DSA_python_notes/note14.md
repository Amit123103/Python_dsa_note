## Insertion Sort (Python)

Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position.

### Code

```python
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Example
arr = [10, 5, 8, 3, 2]
print("Original Array:", arr)

insertion_sort(arr)

print("Sorted Array:", arr)
```

### Output

```text
Original Array: [10, 5, 8, 3, 2]
Sorted Array: [2, 3, 5, 8, 10]
```

### How it Works

For the array:

```text
[10, 5, 8, 3, 2]
```

* Pass 1: Insert `5`

  ```
  [5, 10, 8, 3, 2]
  ```
* Pass 2: Insert `8`

  ```
  [5, 8, 10, 3, 2]
  ```
* Pass 3: Insert `3`

  ```
  [3, 5, 8, 10, 2]
  ```
* Pass 4: Insert `2`

  ```
  [2, 3, 5, 8, 10]
  ```

### Time Complexity

| Case                        | Time Complexity |
| --------------------------- | --------------- |
| Best Case (Already Sorted)  | O(n)            |
| Average Case                | O(n²)           |
| Worst Case (Reverse Sorted) | O(n²)           |

### Space Complexity

* **Space:** O(1) (In-place sorting)
* **Stable:** ✅ Yes

### Dry Run

For `arr = [4, 3, 2, 1]`

| Pass | Key | Array After Insertion |
| ---- | --- | --------------------- |
| 1    | 3   | `[3, 4, 2, 1]`        |
| 2    | 2   | `[2, 3, 4, 1]`        |
| 3    | 1   | `[1, 2, 3, 4]`        |

Insertion Sort is efficient for **small datasets** or **nearly sorted arrays**, but for large datasets, algorithms like Merge Sort or Quick Sort are generally faster.



There are **two main types of parsing** in compiler design:

### 1. Top-Down Parsing

* Starts parsing from the **start symbol** of the grammar.
* Tries to derive the input string from the start symbol.
* Builds the parse tree from **root to leaves**.

**Examples:**

* Recursive Descent Parser
* Predictive Parser (LL(1))

**Advantages:**

* Easy to implement.
* Simple to understand.

**Disadvantages:**

* Cannot handle left-recursive grammars.
* May require grammar modification (left factoring).

---

### 2. Bottom-Up Parsing

* Starts parsing from the **input string**.
* Reduces the input to the start symbol.
* Builds the parse tree from **leaves to root**.

**Examples:**

* Shift-Reduce Parser
* LR Parser
* SLR Parser
* LALR Parser
* CLR (Canonical LR) Parser

**Advantages:**

* Handles a larger class of grammars.
* Can parse left-recursive grammars.

**Disadvantages:**

* More complex to implement.
* Parser construction is more difficult.

---

### Comparison

| Feature        | Top-Down Parsing         | Bottom-Up Parsing                |
| -------------- | ------------------------ | -------------------------------- |
| Starts From    | Start symbol             | Input string                     |
| Parse Tree     | Root → Leaves            | Leaves → Root                    |
| Derivation     | Leftmost derivation      | Rightmost derivation in reverse  |
| Complexity     | Simpler                  | More complex                     |
| Left Recursion | Not supported            | Supported                        |
| Examples       | Recursive Descent, LL(1) | Shift-Reduce, LR, SLR, LALR, CLR |

**Memory Tip:**

* **Top-Down** = **Start → Input** (Root to Leaves)
* **Bottom-Up** = **Input → Start** (Leaves to Root)
The **names of parsing techniques** are:

1. **Top-Down Parsing**

   * Recursive Descent Parser
   * Predictive Parser (LL(1))

2. **Bottom-Up Parsing**

   * Shift-Reduce Parser
   * LR Parser
   * SLR (Simple LR) Parser
   * CLR (Canonical LR) Parser
   * LALR (Look-Ahead LR) Parser

### Main Types

* **Top-Down Parsing**
* **Bottom-Up Parsing**

These are the two major categories of parsing used in compiler design.


# Quick Sort (Easy Notes)

## What is Quick Sort?

**Quick Sort** is a **Divide and Conquer** sorting algorithm.

It works by:

1. Choosing a **Pivot** element.
2. Placing the pivot in its correct sorted position.
3. Moving all smaller elements to the left of the pivot.
4. Moving all larger elements to the right of the pivot.
5. Repeating the same process for the left and right parts.

---

## Steps of Quick Sort

1. Select a **pivot** (first, last, middle, or random element).
2. Partition the array around the pivot.
3. Recursively sort the left subarray.
4. Recursively sort the right subarray.

---

## Example

### Array

```text
[8, 3, 1, 7, 0, 10, 2]
```

### Step 1: Choose Pivot = 2 (last element)

```text
Before Partition
[8, 3, 1, 7, 0, 10, 2]
```

After placing the pivot in the correct position:

```text
[1, 0, 2, 7, 8, 10, 3]
```

Now,

```text
Left Side  = [1, 0]
Pivot      = 2
Right Side = [7, 8, 10, 3]
```

---

### Step 2: Sort Left Side

```text
[1, 0]
```

Choose Pivot = 0

```text
[0, 1]
```

---

### Step 3: Sort Right Side

```text
[7, 8, 10, 3]
```

Choose Pivot = 3

```text
[3, 8, 10, 7]
```

Now sort

```text
[8, 10, 7]
```

Choose Pivot = 7

```text
[7, 10, 8]
```

Now sort

```text
[10, 8]
```

Choose Pivot = 8

```text
[8, 10]
```

---

### Final Sorted Array

```text
[0, 1, 2, 3, 7, 8, 10]
```

---

# Recursion Tree

```text
                 [8 3 1 7 0 10 2]
                       Pivot=2
                     /          \
                 [1 0]      [7 8 10 3]
                Pivot=0       Pivot=3
               /     \        /      \
             []     [1]     []    [8 10 7]
                                  Pivot=7
                                 /       \
                               []      [10 8]
                                       Pivot=8
                                      /      \
                                    []      [10]
```

---

# Algorithm

```text
QuickSort(arr, low, high)

if low < high
    pivot = Partition(arr, low, high)

    QuickSort(arr, low, pivot-1)
    QuickSort(arr, pivot+1, high)
```

---

# Python Code

```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


arr = [8, 3, 1, 7, 0, 10, 2]

quick_sort(arr, 0, len(arr) - 1)

print(arr)
```

**Output:**

```text
[0, 1, 2, 3, 7, 8, 10]
```

---

# Time Complexity

| Case         | Complexity                                                           |
| ------------ | -------------------------------------------------------------------- |
| Best Case    | **O(n log n)**                                                       |
| Average Case | **O(n log n)**                                                       |
| Worst Case   | **O(n²)** (when the pivot is always the smallest or largest element) |

---

# Space Complexity

* **Space Complexity:** **O(log n)** (due to recursion)
* **Stable:** ❌ No
* **In-place:** ✅ Yes

---

# Quick Revision (Exam Notes)

* Uses **Divide and Conquer**.
* Select a **pivot** element.
* Place the pivot in its correct position.
* Elements **smaller** than the pivot go to the **left**.
* Elements **greater** than the pivot go to the **right**.
* Repeat the same process recursively for both halves.
* **Best/Average:** **O(n log n)**
* **Worst:** **O(n²)**
* **Space:** **O(log n)** (recursive stack)
* **In-place:** Yes
* **Stable:** No

**Memory Trick:** **Pivot → Partition → Recursion → Sorted Array**.

# 📘 Today's Notes (DSA + Python + Libraries)

---

# 1. Insertion Sort

## Definition

Insertion Sort is a simple sorting algorithm that places each element in its correct position in the sorted part of the array.

---

## Algorithm

1. Start from the second element.
2. Compare it with previous elements.
3. Shift larger elements one position to the right.
4. Insert the current element in its correct position.
5. Repeat until the array is sorted.

---

## Python Code

```python
arr = [7, 3, 5, 9, 2]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)
```

Output

```text
[2, 3, 5, 7, 9]
```

---

## Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n)       |
| Average | O(n²)      |
| Worst   | O(n²)      |

---

# 2. Parsing

Parsing is the process of checking whether the input follows the grammar rules of a language.

## Types of Parsing

### Top-Down Parsing

* Starts from the start symbol.
* Builds the parse tree from root to leaves.

Examples

* Recursive Descent Parser
* Predictive Parser (LL(1))

---

### Bottom-Up Parsing

* Starts from the input string.
* Builds the parse tree from leaves to root.

Examples

* Shift Reduce Parser
* LR Parser
* SLR Parser
* CLR Parser
* LALR Parser

---

## Difference

| Top Down      | Bottom Up     |
| ------------- | ------------- |
| Root → Leaves | Leaves → Root |
| Easy          | Complex       |
| LL Parser     | LR Parser     |

---

# 3. Quick Sort

## Definition

Quick Sort is a Divide and Conquer sorting algorithm.

---

## Steps

1. Choose Pivot.
2. Partition the array.
3. Sort left part recursively.
4. Sort right part recursively.

---

## Recursive Code

```python
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = []
    middle = []
    right = []

    for x in arr:

        if x < pivot:
            left.append(x)

        elif x == pivot:
            middle.append(x)

        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)


arr = [7,3,5,9,2,15]

print(quick_sort(arr))
```

Output

```text
[2,3,5,7,9,15]
```

---

## Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n²)      |

---

# 4. Virtual Environment (venv)

## Why do we activate it?

The primary reason is:

> To isolate a project's Python packages and dependencies from other projects.

---

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate (Windows)

PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

CMD

```cmd
.venv\Scripts\activate
```

---

## Install Packages

```bash
pip install matplotlib
```

```bash
pip install networkx
```

```bash
pip install kivy
```

```bash
pip install cherrypy
```

---

## Exit Virtual Environment

```bash
deactivate
```

---

# 5. `.env` File vs `venv`

| `.env`                       | `venv`                      |
| ---------------------------- | --------------------------- |
| Stores environment variables | Stores project packages     |
| API Keys                     | Python Libraries            |
| Configuration                | Isolated Python Environment |

---

# 6. Graph

## Definition

A graph is a collection of nodes connected by edges.

Example

```text
Amit ----- Rahul
  |
 Arya
```

---

## Python Representation

```python
graph = {
    "Amit":["Rahul","Arya"],
    "Rahul":["Amit"]
}
```

---

# 7. Social Media Graph Problem

### Requirements

* Create Graph
* Add Friendships
* Display Friends
* Store Users in List
* Insertion Sort
* Binary Search
* Display Friends
* User Not Found

---

## Flow

```text
Create Graph

↓

Store Users

↓

Insertion Sort

↓

Binary Search

↓

Found?

↓

Display Friends

↓

User Not Found
```

---

# 8. NetworkX

Used for Graph Data Structure.

Import

```python
import networkx as nx
```

Create Graph

```python
graph = nx.Graph()
```

Add Friendship

```python
graph.add_edge("Amit","Rahul")
```

Display Graph

```python
nx.draw(graph, with_labels=True)
```

---

# 9. Matplotlib

Used to display the graph visually.

Import

```python
import matplotlib.pyplot as plt
```

Show Graph

```python
plt.show()
```

---

# 10. Common Errors

### Error

```text
ModuleNotFoundError: No module named 'matplotlib'
```

Solution

```bash
pip install matplotlib
```

---

### Error

```text
AttributeError:
module 'numpy' has no attribute 'Graph'
```

Wrong

```python
import numpy as np

graph = np.Graph()
```

Correct

```python
import networkx as nx

graph = nx.Graph()
```

---

### Error

```text
Port 8080 not free
```

Reason

Another application is already using port **8080**.

Solution

```python
cherrypy.config.update({
    "server.socket_port":8081
})
```

---

# 11. Kivy

Used for Desktop GUI Applications.

Install

```bash
pip install kivy
```

Import

```python
from kivy.app import App
```

Used to create:

* Buttons
* Text Boxes
* Labels
* Desktop Applications

---

# 12. CherryPy

Used to create Web Applications.

Install

```bash
pip install cherrypy
```

Start Server

```python
cherrypy.quickstart(app)
```

Default URL

```text
http://localhost:8080
```

If the port is busy

```text
http://localhost:8081
```

---

# 13. Rich Library

Used for beautiful terminal output.

Install

```bash
pip install rich
```

Features

* Colored Text
* Tables
* Panels
* Trees
* Progress Bars

---

# 14. Libraries Learned Today

| Library    | Purpose                              |
| ---------- | ------------------------------------ |
| NetworkX   | Graph Data Structure                 |
| Matplotlib | Graph Visualization                  |
| Kivy       | Desktop GUI                          |
| CherryPy   | Web Framework                        |
| Rich       | Beautiful Terminal Output            |
| NumPy      | Numerical Computing (Not for Graphs) |

---

# 15. Viva Questions

### What is Graph?

A graph is a collection of nodes connected by edges.

### What is Insertion Sort?

A sorting algorithm that inserts each element into its correct position.

### What is Binary Search?

A searching algorithm that works only on sorted data.

### Why activate a virtual environment?

To isolate project dependencies and avoid conflicts with other projects.

### What is the difference between `.env` and `venv`?

* `.env` stores configuration values and secrets.
* `venv` stores project-specific Python packages.

### Which library is used to draw graphs?

* **NetworkX** (graph structure)
* **Matplotlib** (visualization)

### Which library creates desktop GUIs?

**Kivy**

### Which library creates web applications?

**CherryPy**

### Which library enhances terminal output?

**Rich**

---

# Quick Revision

* **Insertion Sort** → O(n²)
* **Quick Sort** → Divide and Conquer
* **Binary Search** → O(log n), requires sorted data
* **Top-Down Parsing** → Root to Leaves
* **Bottom-Up Parsing** → Leaves to Root
* **Graph** → Nodes + Edges
* **NetworkX** → Graph library
* **Matplotlib** → Visualization
* **Kivy** → Desktop GUI
* **CherryPy** → Web framework
* **Rich** → Beautiful terminal output
* **`venv`** → Isolated Python environment
* **`.env`** → Environment variables and configuration
