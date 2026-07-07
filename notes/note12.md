###  Algorithm

1. step-by-step
2. optimize
2(a). Time complexity(time)
2(b). space complexity(space-RAM)


When solving any algorithm problem, you should follow this standard format:

### 1. Algorithm (Step-by-Step)

Write the logic of the solution in simple steps.

**Example: Find the largest element in an array**

1. Start.
2. Read the array.
3. Assume the first element is the largest.
4. Traverse the remaining elements.
5. If the current element is greater than the largest, update the largest.
6. Repeat until the end of the array.
7. Print the largest element.
8. End.

---

### 2. Optimization

After writing the basic algorithm, think about improving it.

* Can the number of loops be reduced?
* Can extra memory be avoided?
* Can a better data structure be used?
* Can a better algorithm reduce the running time?

---

### 2(a). Time Complexity (Time)

Time complexity tells how the running time grows as the input size (**n**) increases.

| Complexity     | Name         | Example                     |
| -------------- | ------------ | --------------------------- |
| **O(1)**       | Constant     | Access an array element     |
| **O(log n)**   | Logarithmic  | Binary Search               |
| **O(n)**       | Linear       | Single loop                 |
| **O(n log n)** | Linearithmic | Merge Sort, Heap Sort       |
| **O(n²)**      | Quadratic    | Two nested loops            |
| **O(2ⁿ)**      | Exponential  | Recursive subset generation |
| **O(n!)**      | Factorial    | Generating all permutations |

---

### 2(b). Space Complexity (Space/RAM)

Space complexity tells how much extra memory the algorithm uses.

| Complexity   | Meaning                                    |
| ------------ | ------------------------------------------ |
| **O(1)**     | No extra memory (constant space)           |
| **O(n)**     | Extra array/list of size **n**             |
| **O(n²)**    | Extra 2D matrix                            |
| **O(log n)** | Recursive call stack (e.g., Binary Search) |

---

## Example

**Problem:** Find the sum of all elements in an array.

**Algorithm**

1. Initialize `sum = 0`.
2. Traverse the array.
3. Add each element to `sum`.
4. Print `sum`.

**Optimization**

* Only one traversal is required.
* No extra data structure is needed.

**Time Complexity**

* **O(n)** (each element is visited once)

**Space Complexity**

* **O(1)** (only one variable `sum` is used)

---

### Standard Template for Any Coding Question

```text
1. Algorithm
   - Step 1
   - Step 2
   - Step 3
   - ...

2. Optimization
   - Can it be improved?
   - Best possible approach

3. Time Complexity
   - O(...)

4. Space Complexity
   - O(...)
```

This is the standard format commonly expected in coding interviews, DSA assignments, and technical exams.


For for loops, the time complexity depends on how many times the loop runs.

General Rule:

Time Complexity = Number of Iterations

### 1. Single for loop

Time Complexity: O(n)

Loop runs n times.

### 2. Nested for loops

Time Complexity: O(n²)

Outer loop = n, Inner loop = n → Total = n × n.

### 3. Loop with increment by 2

Time Complexity: O(n)

Runs about n/2 times, but constants are ignored.

### 4. Loop doubling each time

Time Complexity: O(log n)

Values: 1, 2, 4, 8, 16...

### 5. Two independent loops

Time Complexity: O(n)

Because n + n = 2n → O(n).

### Quick Summary Table

for(i=0; i<n; i++)

Complexity

O(n)

Nested n × n loops

Complexity

O(n²)

i += 2

Complexity

O(n)

i *= 2

Complexity

O(log n)

Two separate n loops

Complexity

O(n)

Interview Trick

Count how many times the loop executes. That gives the time complexity.

Space Complexity for most simple loops is O(1) because only loop variables are used.

### Example asked in exams

Total operations = 1 + 2 + 3 + ... + n

Using the formula n(n+1)/2, the complexity is:

Time Complexity

O(n²)



for(1) input --->>> 10 ~ f(n) -->> represent in growth graph

If a **for loop runs from 1 to n**, then:

```cpp
for (int i = 1; i <= n; i++)
{
    // Constant work
}
```

* **Input (n):** 10
* **Number of iterations:** 10
* **Function:** (f(n)=n)
* **Time Complexity:** **O(n)**

The growth is **linear**, meaning if the input doubles, the work also doubles.

### Table

| Input (n) | f(n) = Operations |
| --------- | ----------------: |
| 1         |                 1 |
| 2         |                 2 |
| 4         |                 4 |
| 6         |                 6 |
| 8         |                 8 |
| 10        |                10 |

### Conclusion

* **Algorithm:** Traverse from `1` to `n`.
* **Function:** (f(n)=n)
* **Time Complexity:** **O(n)** (Linear)
* **Space Complexity:** **O(1)** (Constant)

**Rule to remember:**

* `for(i=1; i<=n; i++)` → **O(n)**
* `for(i=1; i<=n; i+=2)` → **O(n)**
* `for(i=1; i<=n; i*=2)` → **O(log n)**
* Two nested `for` loops (`n × n`) → **O(n²)**


Linear Growth of a For Loop

A for loop that executes from 1 to n grows linearly with the input size.

input	operations
1	1
2	2
4	4
6	6
8	8
10	10


time +O , theta, Omega

time and exeation




In algorithm analysis, there are **three types of time complexity notations**:

| Notation    | Name      | Meaning             |
| ----------- | --------- | ------------------- |
| **O(f(n))** | **Big O** | Worst Case          |
| **Θ(f(n))** | **Theta** | Average/Tight Bound |
| **Ω(f(n))** | **Omega** | Best Case           |

---

## 1. Big O (O) – Worst Case

* Maximum time an algorithm can take.
* Used most often in interviews.

**Example: Linear Search**

```cpp
for(int i=0; i<n; i++)
{
    if(arr[i] == key)
        return i;
}
```

If the element is at the **last position** or not present:

* Comparisons = **n**
* **Time Complexity = O(n)**

---

## 2. Theta (Θ) – Average (Tight Bound)

* Represents the **expected** running time.
* Gives both upper and lower bounds together.

**Example**

Linear Search

* Sometimes found early.
* Sometimes found late.

Average comparisons:

[
\frac{n+1}{2}
]

Ignoring constants:

* **Θ(n)**

---

## 3. Omega (Ω) – Best Case

* Minimum time required.
* Fastest possible execution.

**Example**

```cpp
arr = [10,20,30,40]
key = 10
```

The element is found immediately.

Comparisons = **1**

* **Ω(1)**

---

# Execution Time vs Time Complexity

| Execution Time                                  | Time Complexity                          |
| ----------------------------------------------- | ---------------------------------------- |
| Measured in seconds, milliseconds, microseconds | Measured using Big O, Θ, Ω               |
| Depends on CPU, RAM, compiler, operating system | Independent of hardware                  |
| Changes from computer to computer               | Always remains the same for an algorithm |

### Example

```cpp
for(int i=0; i<n; i++)
{
    cout << i;
}
```

* On Computer A: **0.02 seconds**
* On Computer B: **0.05 seconds**

Execution times are different.

But the **time complexity is still**:

* **O(n)**
* **Θ(n)**
* **Ω(n)**

---

## Linear Search Example

| Case         | Complexity | Reason                                          |
| ------------ | ---------- | ----------------------------------------------- |
| Best Case    | **Ω(1)**   | Element found at the first position             |
| Average Case | **Θ(n)**   | Element found around the middle                 |
| Worst Case   | **O(n)**   | Element found at the last position or not found |

---

## Binary Search Example

| Case         | Complexity   |
| ------------ | ------------ |
| Best Case    | **Ω(1)**     |
| Average Case | **Θ(log n)** |
| Worst Case   | **O(log n)** |

---

## Easy Trick to Remember

* **O (Big O)** → **Upper Bound (Worst Case)**
* **Θ (Theta)** → **Exact/Tight Bound (Average Case)**
* **Ω (Omega)** → **Lower Bound (Best Case)**

### Memory Shortcut

```text
Ω (Omega)  → Best Case    → Minimum Time
Θ (Theta)  → Average Case → Expected Time
O (Big O)  → Worst Case   → Maximum Time
```

This is the standard way time complexity is explained in DSA courses, coding interviews, and university exams.


### A machine have 64 bit processing ,8gb ram and 2 core and B machine 32 bit , 64 GB and 8 core  and we give 128bit string passing which one is best 

If you are processing a **128-bit string**, the best machine depends on what "processing" means. Let's compare the two machines.

| Feature   | Machine A  | Machine B  |
| --------- | ---------- | ---------- |
| Processor | **64-bit** | **32-bit** |
| RAM       | **8 GB**   | **64 GB**  |
| CPU Cores | **2**      | **8**      |

### Can they process a 128-bit string?

Yes. A **128-bit string** is only **16 bytes**, which is tiny. Both machines can store and process it.

### Which machine is better?

* **For handling a single 128-bit string or general modern software:** **Machine A** is better because it has a **64-bit processor**. A 64-bit CPU is designed to efficiently handle larger data sizes and modern operating systems and applications.
* **Machine B** has much more RAM (64 GB) and more CPU cores (8), which is excellent for multitasking or running many tasks in parallel. However, its **32-bit processor is a major limitation**. A 32-bit architecture cannot take full advantage of 64 GB of RAM in a typical configuration and is generally less capable for modern workloads.

### Conclusion

For processing a **128-bit string**, **Machine A** is the better choice because of its **64-bit architecture**.

If you were comparing the machines for **running many parallel tasks** or **large-scale workloads**, the answer would depend on whether Machine B is actually using a 32-bit operating system and how its memory is configured. In real-world systems, a 32-bit CPU with 64 GB RAM is an unusual and impractical combination because a standard 32-bit processor cannot fully address all 64 GB of memory.



### machine A will be faster than machine B because machine is a  have 2 for complexity to process and second machine have 4 for loop both can solve but machine a faster than second one



### Searching data
1. sorted data
2. unsorted data

### Sorted Data vs Unsorted Data

The answer depends on the operation you want to perform.

| Operation            | Sorted Data                    | Unsorted Data                         | Faster       |
| -------------------- | ------------------------------ | ------------------------------------- | ------------ |
| Search               | ✅ Binary Search (**O(log n)**) | Linear Search (**O(n)**)              | **Sorted**   |
| Insert               | **O(n)**                       | **O(1)** (at end)                     | **Unsorted** |
| Delete               | **O(n)**                       | **O(n)** (or **O(1)** if index known) | Depends      |
| Find Minimum/Maximum | **O(1)** (first/last element)  | **O(n)**                              | **Sorted**   |

---

## 1. Why is Sorted Data Faster for Searching?

### Unsorted Data

Example:

```text
20  5  18  9  30  2  15
```

To find **30**, you may have to check every element.

```text
20 ❌
5  ❌
18 ❌
9  ❌
30 ✅
```

Worst-case comparisons = **n**

**Time Complexity = O(n)**

---

### Sorted Data

```text
2  5  9  15  18  20  30
```

Use **Binary Search**:

1. Check the middle element.
2. If the target is larger, search the right half.
3. If smaller, search the left half.
4. Repeat.

Only **log₂(n)** comparisons are needed.

**Time Complexity = O(log n)**

---

## 2. Why is Unsorted Data Faster for Insertion?

### Unsorted

```text
5  10  20
```

Insert **15**:

```text
5  10  20  15
```

Just append it.

**Time Complexity = O(1)**

---

### Sorted

```text
5  10  20
```

Insert **15**:

```text
5  10  15  20
```

You must:

1. Find the correct position.
2. Shift elements.

**Time Complexity = O(n)**

---

## 3. Why is Sorted Data Better?

### Example: Search for 70

**Unsorted**

```text
40 10 70 30 20
```

May need to check every element.

---

**Sorted**

```text
10 20 30 40 70
```

Binary Search:

```text
10 20 30 40 70
      ↑
Middle = 30

70 > 30
Search right half

40 70
 ↑
Middle = 40

70 > 40

70 ✅
```

Very few comparisons.

---

## Time Complexity Comparison

| Operation | Sorted       | Unsorted          |
| --------- | ------------ | ----------------- |
| Search    | **O(log n)** | **O(n)**          |
| Insert    | **O(n)**     | **O(1)** (append) |
| Delete    | **O(n)**     | **O(n)**          |
| Find Min  | **O(1)**     | **O(n)**          |
| Find Max  | **O(1)**     | **O(n)**          |

---

## Which One is Faster?

* **Searching:** ✅ **Sorted data** is faster because it supports **Binary Search (O(log n))**.
* **Inserting:** ✅ **Unsorted data** is faster because you can add an element directly without maintaining order.
* **Finding minimum/maximum:** ✅ **Sorted data** is faster because the smallest and largest values are already at the ends.

### Easy Trick to Remember

* **Sorted Data → Fast Search**
* **Unsorted Data → Fast Insert**

**Rule:** If your application performs many searches, keep the data **sorted**. If it performs frequent insertions and order doesn't matter, **unsorted** data is usually more efficient.

Here are the **most common sorting algorithms** used in DSA:

| Sorting Algorithm  | Best Case      | Average Case   | Worst Case     | Space    | Stable  |
| ------------------ | -------------- | -------------- | -------------- | -------- | ------- |
| **Bubble Sort**    | O(n)           | O(n²)          | O(n²)          | O(1)     | ✅ Yes   |
| **Selection Sort** | O(n²)          | O(n²)          | O(n²)          | O(1)     | ❌ No    |
| **Insertion Sort** | O(n)           | O(n²)          | O(n²)          | O(1)     | ✅ Yes   |
| **Merge Sort**     | O(n log n)     | O(n log n)     | O(n log n)     | O(n)     | ✅ Yes   |
| **Quick Sort**     | O(n log n)     | O(n log n)     | O(n²)          | O(log n) | ❌ No    |
| **Heap Sort**      | O(n log n)     | O(n log n)     | O(n log n)     | O(1)     | ❌ No    |
| **Counting Sort**  | O(n + k)       | O(n + k)       | O(n + k)       | O(k)     | ✅ Yes   |
| **Radix Sort**     | O(d × (n + k)) | O(d × (n + k)) | O(d × (n + k)) | O(n + k) | ✅ Yes   |
| **Bucket Sort**    | O(n + k)       | O(n + k)       | O(n²)          | O(n)     | Depends |
| **Shell Sort**     | O(n log n)     | ~O(n^1.5)      | O(n²)          | O(1)     | ❌ No    |

### Comparison-Based Sorting Algorithms

These compare elements to determine order:

1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
6. Heap Sort
7. Shell Sort

### Non-Comparison Sorting Algorithms

These sort without directly comparing elements:

1. Counting Sort
2. Radix Sort
3. Bucket Sort

### Easy Way to Remember

**Basic Sorting (Beginner):**

* Bubble Sort
* Selection Sort
* Insertion Sort

**Efficient Sorting (Most Used):**

* Merge Sort
* Quick Sort
* Heap Sort

**Special Sorting (Integer/Range-Based):**

* Counting Sort
* Radix Sort
* Bucket Sort

### Frequently Asked in Interviews

* ✅ Bubble Sort
* ✅ Selection Sort
* ✅ Insertion Sort
* ✅ Merge Sort
* ✅ Quick Sort
* ✅ Heap Sort

These six algorithms are the most important for DSA exams, coding interviews, and competitive programming.

### speacial sorting buket sort and redix and counting sort

## Brute Force Algorithm

A **Brute Force Algorithm** is the simplest approach to solve a problem. It **tries every possible solution** until it finds the correct one.

### Definition

> A brute force algorithm checks all possible cases without using any optimization.

---

## How It Works

1. Generate all possible solutions.
2. Check each solution.
3. If the solution is correct, return it.
4. Otherwise, continue checking.

---

## Example 1: Linear Search (Brute Force)

Find `20` in the array:

```text
Array = [5, 10, 15, 20, 25]
```

Algorithm:

1. Compare 20 with 5 ❌
2. Compare 20 with 10 ❌
3. Compare 20 with 15 ❌
4. Compare 20 with 20 ✅
5. Stop.

**Time Complexity:**

* Best Case: **Ω(1)**
* Average Case: **Θ(n)**
* Worst Case: **O(n)**

---

## Example 2: Two Sum

```text
Array = [2, 7, 11, 15]
Target = 9
```

Brute Force:

* Check (2,7) ✅
* Check (2,11)
* Check (2,15)
* Check (7,11)
* ...

Two nested loops.

**Time Complexity:** **O(n²)**

---

## Example 3: Password Guessing

Password = `"1234"`

A brute force attack tries:

```text
0000
0001
0002
...
1234 ✅
```

It checks every possible password until the correct one is found.

---

## Advantages

* ✔ Very simple to understand.
* ✔ Easy to implement.
* ✔ Always finds the correct solution (if one exists).

---

## Disadvantages

* ✖ Slow for large inputs.
* ✖ Performs unnecessary computations.
* ✖ Usually not suitable for large datasets.

---

## Brute Force vs Optimized Algorithm

| Feature         | Brute Force                | Optimized                        |
| --------------- | -------------------------- | -------------------------------- |
| Approach        | Try every possibility      | Use efficient techniques         |
| Speed           | Slower                     | Faster                           |
| Time Complexity | Usually O(n²), O(2ⁿ), etc. | Often O(n), O(log n), O(n log n) |
| Implementation  | Easy                       | More complex                     |

---

## Real-Life Example

Imagine you forgot the PIN of your phone.

* **Brute Force:** Try every PIN one by one until it unlocks.
* **Optimized:** Remember a hint or use another method to reduce the number of attempts.

---

## Easy Definition for Exams

> **Brute Force Algorithm:** A straightforward algorithmic technique that solves a problem by checking all possible solutions until the correct one is found. It is simple to implement but usually inefficient for large inputs.

### Key Points to Remember

* **Checks every possibility**
* **No optimization**
* **Easy to implement**
* **Usually slower**
* **Guarantees the correct answer if one exists**






Easy Formula to Remember
Outer Loop (i)
      ↓
Controls the number of passes.

Inner Loop (j)
      ↓
Compares adjacent elements.

if
      ↓
Checks if a swap is needed.

Swap
      ↓
Moves the larger element toward the end.



`sort()` and `sorted()` are both used to sort data in Python, but they work differently.

| Feature                | `sort()`             | `sorted()`                                    |
| ---------------------- | -------------------- | --------------------------------------------- |
| Works on               | Lists only           | Any iterable (list, tuple, string, set, etc.) |
| Changes original data? | ✅ Yes                | ❌ No                                          |
| Returns                | `None`               | A new sorted list                             |
| Memory                 | Uses less (in-place) | Uses more (creates a new list)                |

---

## 1. `sort()` Function

* Sorts the **original list**.
* Does **not** create a new list.
* Returns `None`.

### Syntax

```python
list.sort(reverse=False, key=None)
```

### Example

```python
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)
```

### Output

```text
[1, 2, 5, 8]
```

The original list has changed.

---

### Return Value

```python
numbers = [5, 2, 8]

result = numbers.sort()

print(result)
```

### Output

```text
None
```

Because `sort()` modifies the list directly.

---

## 2. `sorted()` Function

* Does **not** modify the original data.
* Returns a **new sorted list**.

### Syntax

```python
sorted(iterable, reverse=False, key=None)
```

### Example

```python
numbers = [5, 2, 8, 1]

new_list = sorted(numbers)

print(new_list)
print(numbers)
```

### Output

```text
[1, 2, 5, 8]
[5, 2, 8, 1]
```

The original list remains unchanged.

---

## Example with a Tuple

`sort()` does not work on tuples.

```python
t = (5, 2, 8, 1)

print(sorted(t))
```

### Output

```text
[1, 2, 5, 8]
```

---

## Example with a String

```python
text = "python"

print(sorted(text))
```

### Output

```text
['h', 'n', 'o', 'p', 't', 'y']
```

---

## Descending Order

### `sort()`

```python
numbers = [5, 2, 8, 1]
numbers.sort(reverse=True)

print(numbers)
```

### Output

```text
[8, 5, 2, 1]
```

---

### `sorted()`

```python
numbers = [5, 2, 8, 1]

print(sorted(numbers, reverse=True))
```

### Output

```text
[8, 5, 2, 1]
```

---

## Using `key`

Sort strings by their length.

```python
words = ["apple", "kiwi", "banana", "fig"]

print(sorted(words, key=len))
```

### Output

```text
['fig', 'kiwi', 'apple', 'banana']
```

---

## Memory Comparison

```python
numbers = [4, 3, 2, 1]

numbers.sort()        # Same list is sorted
```

Memory:

```text
Old List
   ↓
Sorted List
```

---

```python
numbers = [4, 3, 2, 1]

new_numbers = sorted(numbers)
```

Memory:

```text
Old List  --------> [4,3,2,1]

New List  --------> [1,2,3,4]
```

---

## When to Use Which?

* Use **`sort()`** when:

  * You have a **list**.
  * You want to modify the original list.
  * You want to save memory.

* Use **`sorted()`** when:

  * You want to keep the original data unchanged.
  * You are sorting a **tuple, string, set, or other iterable**.
  * You need a new sorted list.

---

## Interview Summary

| `sort()`                    | `sorted()`                |
| --------------------------- | ------------------------- |
| In-place sorting            | Returns a new sorted list |
| Only for lists              | Works with all iterables  |
| Returns `None`              | Returns the sorted list   |
| Faster and uses less memory | Uses extra memory         |

### Easy Trick to Remember

* **`sort()` → "Same list"** (changes the original list)
* **`sorted()` → "Separate list"** (creates a new sorted list)





# 📘 DSA & Python Quick Notes (Revision)

---

# 1. Algorithm

An **algorithm** is a step-by-step procedure to solve a problem.

### Format

1. Algorithm (Steps)
2. Optimization
3. Time Complexity
4. Space Complexity

Example

```text
Input
↓
Algorithm
↓
Output
```

---

# 2. Time Complexity

Measures **how execution time grows** as input size (`n`) increases.

## Big O Notation

| Notation | Meaning               |
| -------- | --------------------- |
| **O()**  | Worst Case            |
| **Θ()**  | Average (Tight Bound) |
| **Ω()**  | Best Case             |

### Example

Linear Search

* Best = Ω(1)
* Average = Θ(n)
* Worst = O(n)

---

# 3. Space Complexity

Measures **extra RAM** used by an algorithm.

Examples

```text
O(1)  Constant
O(n)  Linear
O(n²) Matrix
```

---

# 4. Common Complexities

| Complexity | Name         |
| ---------- | ------------ |
| O(1)       | Constant     |
| O(log n)   | Logarithmic  |
| O(n)       | Linear       |
| O(n log n) | Linearithmic |
| O(n²)      | Quadratic    |
| O(2ⁿ)      | Exponential  |
| O(n!)      | Factorial    |

---

# 5. For Loop Complexity

### Single Loop

```python
for i in range(n):
```

Time → **O(n)**

Space → **O(1)**

---

### Nested Loop

```python
for i in range(n):
    for j in range(n):
```

Time → **O(n²)**

---

### Increment by 2

```python
for i in range(0,n,2):
```

Time → **O(n)**

---

### Double Every Time

```python
i = 1
while i < n:
    i *= 2
```

Time → **O(log n)**

---

# 6. Growth Graph

```
Operations
 ^
 |            *
 |          *
 |        *
 |      *
 |    *
 |  *
 +--------------------> n

Linear Growth
f(n)=n
```

---

# 7. Execution Time vs Time Complexity

| Execution Time              | Time Complexity                  |
| --------------------------- | -------------------------------- |
| Seconds                     | Mathematical                     |
| Depends on CPU              | Independent of CPU               |
| Different on every computer | Same algorithm ⇒ Same complexity |

---

# 8. Machine Comparison

Machine A

* 64-bit Processor
* 8 GB RAM
* 2 Core

Machine B

* 32-bit Processor
* 64 GB RAM
* 8 Core

For processing a **128-bit string**, **Machine A** is generally the better choice because of its **64-bit architecture**. A 32-bit processor cannot efficiently use very large memory and is limited for modern workloads.

---

# 9. Data Manipulation

Basic Operations

* Insert
* Delete
* Update
* Select
* Search
* Filter
* Sort
* Merge
* Split
* Clean
* Aggregate
* Transform

---

# 10. Sorted vs Unsorted Data

| Operation | Sorted   | Unsorted |
| --------- | -------- | -------- |
| Search    | O(log n) | O(n)     |
| Insert    | O(n)     | O(1)     |
| Delete    | O(n)     | O(n)     |
| Min/Max   | O(1)     | O(n)     |

### Rule

* Searching → Sorted
* Insertion → Unsorted

---

# 11. Sorting Algorithms

Basic

* Bubble Sort
* Selection Sort
* Insertion Sort

Efficient

* Merge Sort
* Quick Sort
* Heap Sort

Non-Comparison

* Counting Sort
* Radix Sort
* Bucket Sort

---

# 12. Bubble Sort

Logic

```
Compare
↓
Swap
↓
Largest moves to end
↓
Repeat
```

Example

```python
arr = [2,100,9,105,10]
```

After sorting

```python
[2,9,10,100,105]
```

Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n)       |
| Average | O(n²)      |
| Worst   | O(n²)      |
| Space   | O(1)       |

---

# 13. Bubble Sort Functions

```python
n = len(arr)
```

Counts elements.

---

```python
for i in range(n-1):
```

Controls **passes**.

---

```python
for j in range(n-1-i):
```

Compares adjacent elements.

---

```python
if arr[j] > arr[j+1]:
```

Checks order.

---

```python
arr[j], arr[j+1] = arr[j+1], arr[j]
```

Swaps elements.

---

# 14. Python `sort()` vs `sorted()`

| sort()                | sorted()            |
| --------------------- | ------------------- |
| Changes original list | Returns new list    |
| Only list             | Any iterable        |
| Returns None          | Returns sorted list |

---

### Example

```python
arr.sort()
```

Original list changes.

---

```python
new = sorted(arr)
```

Original list stays unchanged.

---

# 15. Which Algorithm Does Python Use?

Both

```python
sort()
```

and

```python
sorted()
```

use **Timsort**.

Timsort =

* Merge Sort
* Insertion Sort

Complexity

Best → O(n)

Average → O(n log n)

Worst → O(n log n)

---

# 16. Search in Python List

### Check Exists

```python
20 in arr
```

---

### Get Index

```python
arr.index(20)
```

---

### Safe Search

```python
if 20 in arr:
    print(arr.index(20))
```

---

### Using Loop

```python
for i,x in enumerate(arr):
    if x == target:
        print(i)
```

---

# 17. Brute Force Algorithm

Definition

Checks **every possible solution** until the correct one is found.

Examples

* Linear Search
* Bubble Sort
* Two Sum (nested loops)
* Password guessing

Advantages

* Easy
* Simple
* Correct

Disadvantages

* Slow
* Not optimized

---

# 18. Python Developer Tips

### Check value

```python
20 in arr
```

---

### Get index

```python
arr.index(20)
```

---

### Find all indexes

```python
[i for i,x in enumerate(arr) if x==20]
```

---

### First index

```python
next((i for i,x in enumerate(arr) if x==20),-1)
```

---

# 19. Interview Cheat Sheet

### Search

* Linear Search → O(n)
* Binary Search → O(log n)

### Sorting

* Bubble → O(n²)
* Selection → O(n²)
* Insertion → O(n²)
* Merge → O(n log n)
* Quick → O(n log n) average, O(n²) worst
* Heap → O(n log n)
* Timsort → O(n log n)

### Loop Complexities

```python
for i in range(n)
```

→ O(n)

```python
for i in range(n):
    for j in range(n)
```

→ O(n²)

```python
i *= 2
```

→ O(log n)

---

# 🎯 Final Memory Tricks

* **Algorithm** = Steps to solve a problem.
* **Big O** = Worst Case.
* **Theta (Θ)** = Average/Tight Bound.
* **Omega (Ω)** = Best Case.
* **Time Complexity** = Speed growth.
* **Space Complexity** = Extra memory used.
* **Sorted Data** → Faster searching.
* **Unsorted Data** → Faster insertion.
* **Bubble Sort** → Compare adjacent elements and swap.
* **Python `sort()` & `sorted()`** → Use **Timsort**.
* **`sort()`** modifies the original list.
* **`sorted()`** returns a new sorted list.
* **`in`** checks if an element exists.
* **`index()`** returns the element's position.
* **Brute Force** = Try every possibility until the correct answer is found.

These notes cover the core concepts you discussed and provide a concise revision guide for DSA, Python, interviews, and exams.

# 📘 Searching in DSA (Quick Notes)

## What is Searching?

**Searching** is the process of finding a specific element in a collection of data (array, list, etc.).

**Example**

```text
Array = [2, 100, 9, 105, 10, 20]

Find = 20
```

Output:

```text
Found at index 5
```

---

# Types of Searching

## 1. Linear Search (Sequential Search)

* Checks each element one by one.
* Works on **sorted and unsorted** data.

### Algorithm

1. Start from the first element.
2. Compare it with the target.
3. If it matches, return the index.
4. Otherwise, move to the next element.
5. Repeat until the end.

### Python Code

```python
arr = [2, 100, 9, 105, 10, 20]

target = 20

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)
        break
```

### Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | Ω(1)       |
| Average | Θ(n)       |
| Worst   | O(n)       |
| Space   | O(1)       |

---

## 2. Binary Search

* Works **only on sorted data**.
* Divides the search space into two halves.

### Algorithm

1. Find the middle element.
2. If the middle is the target → Found.
3. If the target is smaller → Search the left half.
4. If the target is larger → Search the right half.
5. Repeat until found or the search space is empty.

### Python Code

```python
arr = [2, 9, 10, 15, 20, 36, 42, 55, 100, 105]

target = 20

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Found at index", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
```

### Complexity

| Case    | Complexity       |
| ------- | ---------------- |
| Best    | Ω(1)             |
| Average | Θ(log n)         |
| Worst   | O(log n)         |
| Space   | O(1) (iterative) |

---

# Linear Search vs Binary Search

| Feature      | Linear Search       | Binary Search      |
| ------------ | ------------------- | ------------------ |
| Data         | Sorted or Unsorted  | **Sorted only**    |
| Method       | Check every element | Divide and conquer |
| Best Case    | O(1)                | O(1)               |
| Average Case | O(n)                | O(log n)           |
| Worst Case   | O(n)                | O(log n)           |

---

# Python Search Methods

### Check if an element exists

```python
arr = [2, 100, 9, 105, 10, 20]

print(20 in arr)
```

Output

```text
True
```

---

### Get the index

```python
arr = [2, 100, 9, 105, 10, 20]

print(arr.index(20))
```

Output

```text
5
```

---

### Safe Search

```python
arr = [2, 100, 9, 105, 10, 20]

target = 20

if target in arr:
    print(arr.index(target))
else:
    print("Not Found")
```

---

### Find All Occurrences

```python
arr = [20, 5, 20, 10, 20]

target = 20

indexes = [i for i, x in enumerate(arr) if x == target]

print(indexes)
```

Output

```text
[0, 2, 4]
```

---

# Real-Life Examples

* 📖 Find a word in a dictionary → **Binary Search**
* 📞 Find a contact in an unsorted phone list → **Linear Search**
* 🛒 Search a product by ID in a sorted database → **Binary Search**

---

# Interview Questions

### Which search is faster?

✅ **Binary Search** because its time complexity is **O(log n)**.

### When can Binary Search be used?

✅ Only when the data is **sorted**.

### Can Binary Search work on an unsorted array?

❌ No.

### Which search works on any array?

✅ **Linear Search**.

---

# Memory Trick

```text
Searching
│
├── Linear Search
│   ├── Sorted / Unsorted
│   ├── O(n)
│   └── Check one by one
│
└── Binary Search
    ├── Sorted only
    ├── O(log n)
    └── Divide into halves
```

## Quick Revision

* **Linear Search** → Checks each element → **O(n)**.
* **Binary Search** → Searches by halving the range → **O(log n)**.
* **Binary Search requires sorted data**.
* **Python shortcuts:**

  * `x in arr` → Check existence.
  * `arr.index(x)` → Get index (raises an error if not found).
  * `enumerate()` → Find all matching indices.

Your code has several mistakes:

### Mistakes

1. `i` is never initialized.
2. `list[i]` should be `list1[i]`.
3. `if list[i] == list1` compares an element with the entire list.
4. `i` is never incremented (`i += 1`).
5. `list1.list = [...]` is not the correct way to call a method.
6. You need to pass the **target value** (e.g., `20`) to search for.

---

## Correct Code Using a Class

```python
class Search:
    def search(self, list1, target):
        i = 0

        while i < len(list1):
            if list1[i] == target:
                print("Found at index:", i)
                return
            i += 1

        print("Not Found")


obj = Search()

numbers = [2, 100, 9, 105, 10, 20, 15, 36, 55, 42]

obj.search(numbers, 20)
```

### Output

```text
Found at index: 5
```

---

## Without a Class (Simpler)

```python
numbers = [2, 100, 9, 105, 10, 20, 15, 36, 55, 42]

target = 20

i = 0

while i < len(numbers):
    if numbers[i] == target:
        print("Found at index:", i)
        break
    i += 1
```

---

### Interview Tip

For DSA interviews, they usually expect you to write the **second version** (without a class), because it demonstrates the **Linear Search algorithm** clearly. The class version is useful when you're organizing code in larger Python projects.



# Binary Search

**Binary Search** is a searching algorithm that works **only on sorted data**. It repeatedly divides the search space into two halves.

---

## Algorithm

1. Sort the array (if it is not already sorted).
2. Set:

   * `low = 0`
   * `high = len(arr) - 1`
3. Find the middle index:

   ```python
   mid = (low + high) // 2
   ```
4. If `arr[mid] == target`, return the index.
5. If `target > arr[mid]`, search the right half:

   ```python
   low = mid + 1
   ```
6. Otherwise, search the left half:

   ```python
   high = mid - 1
   ```
7. Repeat until `low > high`.

---

## Step 1: Sort the List

Original list:

```python
[2, 100, 9, 105, 10, 20, 15, 36, 55, 42]
```

Sorted list:

```python
[2, 9, 10, 15, 20, 36, 42, 55, 100, 105]
```

---

## Python Code (Iterative)

```python
arr = [2, 9, 10, 15, 20, 36, 42, 55, 100, 105]

target = 20

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Found at index:", mid)
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1
```

### Output

```text
Found at index: 4
```

---

# Dry Run

Search for **20**

```text
Index : 0  1  2  3  4  5  6  7   8    9
Value : 2  9 10 15 20 36 42 55 100 105
```

### Iteration 1

```text
low = 0
high = 9

mid = (0 + 9) // 2 = 4

arr[4] = 20
```

Target found immediately.

---

## Example: Search for 42

### Iteration 1

```text
low = 0
high = 9

mid = 4

arr[4] = 20

42 > 20
```

Search the right half.

```text
low = 5
high = 9
```

---

### Iteration 2

```text
mid = (5 + 9) // 2 = 7

arr[7] = 55

42 < 55
```

Search the left half.

```text
low = 5
high = 6
```

---

### Iteration 3

```text
mid = (5 + 6) // 2 = 5

arr[5] = 36

42 > 36
```

```text
low = 6
high = 6
```

---

### Iteration 4

```text
mid = (6 + 6) // 2 = 6

arr[6] = 42
```

Found.

---

## Recursive Binary Search

```python
def binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)

    else:
        return binary_search(arr, low, mid - 1, target)


arr = [2, 9, 10, 15, 20, 36, 42, 55, 100, 105]

print(binary_search(arr, 0, len(arr) - 1, 20))
```

**Output**

```text
4
```

---

## Complexity

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | **Ω(1)**        |
| Average Case | **Θ(log n)**    |
| Worst Case   | **O(log n)**    |

**Space Complexity**

* Iterative: **O(1)**
* Recursive: **O(log n)** (due to the recursion stack)

---

## Difference: Linear Search vs Binary Search

| Feature           | Linear Search     | Binary Search                   |
| ----------------- | ----------------- | ------------------------------- |
| Works on          | Sorted & Unsorted | **Sorted only**                 |
| Method            | Check one by one  | Divide the search space in half |
| Worst Time        | **O(n)**          | **O(log n)**                    |
| Space (Iterative) | **O(1)**          | **O(1)**                        |

### Memory Trick

```text
Linear Search
↓
Check every element
O(n)

Binary Search
↓
Find middle
↓
Left or Right?
↓
Repeat
O(log n)
```

**Important:** If the input array is **not sorted**, you must sort it first before applying Binary Search.
# Binary Search Tree (BST)

A **Binary Search Tree (BST)** is a binary tree where every node follows a specific rule:

* **Left child** contains values **smaller** than the parent.
* **Right child** contains values **greater** than the parent.

This property makes searching, insertion, and deletion efficient.

---

# BST Rule

```text
Left  <  Root  <  Right
```

Example:

```text
        20
       /  \
     10    30
    / \    / \
   5  15 25  40
```

* Left of 20 → 10, 5, 15 (all smaller than 20)
* Right of 20 → 30, 25, 40 (all greater than 20)

---

# How a BST is Created

Insert the numbers:

```text
20, 10, 30, 5, 15, 25, 40
```

### Step 1

Insert **20**

```text
20
```

---

### Step 2

Insert **10**

10 < 20

Go left.

```text
   20
  /
10
```

---

### Step 3

Insert **30**

30 > 20

Go right.

```text
   20
  /  \
10   30
```

---

### Step 4

Insert **5**

5 < 20 → Left

5 < 10 → Left

```text
     20
    /  \
  10   30
 /
5
```

---

### Step 5

Insert **15**

15 < 20 → Left

15 > 10 → Right

```text
      20
     /  \
   10   30
  / \
 5  15
```

---

### Step 6

Insert **25**

25 > 20 → Right

25 < 30 → Left

```text
      20
     /  \
   10   30
  / \   /
 5 15 25
```

---

### Step 7

Insert **40**

40 > 20

40 > 30

```text
        20
       /  \
     10    30
    / \   / \
   5 15 25 40
```

---

# Searching in BST

Search for **25**

```text
        20
       /  \
     10    30
    / \   / \
   5 15 25 40
```

### Step 1

25 > 20

Go right.

---

### Step 2

25 < 30

Go left.

---

### Step 3

25 == 25

Found ✅

Only **3 comparisons** are needed.

---

# Searching for 15

```text
20
↓
15 < 20
↓
Go Left

10
↓

15 > 10
↓

Go Right

15

Found
```

---

# Insertion Algorithm

Suppose we insert **35**.

```text
        20
       /  \
     10    30
          /  \
        25   40
```

35 > 20

↓

Go Right

↓

35 > 30

↓

Go Right

↓

35 < 40

↓

Go Left

Final Tree

```text
        20
       /  \
     10    30
          /  \
        25   40
             /
            35
```

---

# Deletion

There are **3 cases**:

### Case 1: Leaf Node

Delete **15**

```text
Before

10
 \
15

After

10
```

---

### Case 2: One Child

```text
20
 \
30
 \
40
```

Delete 30

```text
20
 \
40
```

---

### Case 3: Two Children

Delete **20**

Replace it with either:

* the **inorder successor** (smallest node in the right subtree), or
* the **inorder predecessor** (largest node in the left subtree),

then delete that replacement node from its original position.

---

# Complexity

| Operation | Average      | Worst    |
| --------- | ------------ | -------- |
| Search    | **O(log n)** | **O(n)** |
| Insert    | **O(log n)** | **O(n)** |
| Delete    | **O(log n)** | **O(n)** |

The worst case happens when the tree becomes skewed (like a linked list).

---

# BST vs Binary Tree

| Binary Tree          | Binary Search Tree            |
| -------------------- | ----------------------------- |
| No ordering rule     | Left < Root < Right           |
| Search may take O(n) | Search is O(log n) on average |
| Any arrangement      | Values are ordered            |

---

# Real-Life Examples

* Contact search
* Dictionary lookup
* Database indexing
* File system organization
* Leaderboards and ranking systems

---

# Memory Trick

```text
          Root
         /    \
 Smaller      Larger
```

Always remember:

* **Left subtree → Smaller values**
* **Right subtree → Larger values**

---

# Quick Revision

* A BST is a **binary tree with an ordering rule**.
* **Left < Root < Right**.
* Searching follows the order instead of checking every node.
* Average search, insertion, and deletion take **O(log n)**.
* If the tree becomes unbalanced (skewed), operations can degrade to **O(n)**.

A **Binary Search Tree (BST) is not sorted by rearranging the tree**. Instead, it **stores data in an ordered way**. To get the elements in sorted order, you perform an **Inorder Traversal**.

---

# Step 1: Insert Elements

Suppose you have:

```text
20, 10, 30, 5, 15, 25, 40
```

Insert them one by one.

```
Insert 20

20
```

```
Insert 10

   20
  /
10
```

```
Insert 30

   20
  /  \
10   30
```

```
Insert 5

     20
    /  \
  10   30
 /
5
```

```
Insert 15

      20
     /  \
   10   30
  / \
 5  15
```

```
Insert 25

      20
     /  \
   10   30
  / \   /
 5 15 25
```

```
Insert 40

        20
       /  \
     10    30
    / \   / \
   5 15 25 40
```

---

# Step 2: Inorder Traversal

The rule is:

```
Left
↓
Root
↓
Right
```

For the tree above:

```
        20
       /  \
     10    30
    / \   / \
   5 15 25 40
```

Visit:

```
5
↓

10
↓

15
↓

20
↓

25
↓

30
↓

40
```

**Output (Sorted):**

```text
5 10 15 20 25 30 40
```

---

# Python Code

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
```

Calling:

```python
inorder(root)
```

prints:

```
5 10 15 20 25 30 40
```

---

# Why Does Inorder Traversal Sort a BST?

A BST always satisfies:

```
Left < Root < Right
```

So when you visit:

```
Left → Root → Right
```

you naturally visit values from **smallest to largest**.

---

# Example

Unsorted input:

```
40 20 10 30 60 50 70
```

BST:

```
         40
       /    \
     20      60
    /  \    /  \
  10   30 50   70
```

Inorder Traversal:

```
10
20
30
40
50
60
70
```

Sorted output:

```text
10 20 30 40 50 60 70
```

---

# Complexity

### Building the BST

* Average: **O(n log n)**
* Worst (skewed tree): **O(n²)**

### Inorder Traversal

* Visits each node exactly once.
* **Time Complexity:** **O(n)**
* **Space Complexity:** **O(h)**, where `h` is the height of the tree (due to the recursion stack).

---

# Interview Tip

**Question:** How do you sort elements using a Binary Search Tree?

**Answer:**

1. Insert all elements into the BST.
2. Perform an **Inorder Traversal (Left → Root → Right)**.
3. The traversal outputs the elements in **ascending sorted order**.

### Memory Trick

```text
BST Rule:
Left < Root < Right

Traversal:
Left → Root → Right

Result:
Sorted Order (Ascending)
```

This is why **inorder traversal of a Binary Search Tree always produces a sorted sequence**.
If you want a **function that inserts elements into a Binary Search Tree (BST) and then prints them in sorted order**, here is the standard implementation.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.data:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


# Driver Code
arr = [2, 100, 9, 105, 10, 20, 15, 36, 55, 42]

tree = BST()
root = None

for value in arr:
    root = tree.insert(root, value)

print("Sorted Order:")
tree.inorder(root)
```

### Output

```text
Sorted Order:
2 9 10 15 20 36 42 55 100 105
```

---

## How it Works

### Step 1: Insert Elements

Input:

```text
2, 100, 9, 105, 10, 20, 15, 36, 55, 42
```

BST becomes:

```text
        2
         \
         100
        /
       9
        \
        10
          \
          20
         /  \
       15    36
                \
                55
               /
              42
                 \
                 105
```

(Exact shape depends on insertion order.)

### Step 2: Inorder Traversal

The traversal always follows:

```text
Left
↓
Root
↓
Right
```

This prints:

```text
2 9 10 15 20 36 42 55 100 105
```

which is the **sorted order**.

---

## Complexity

| Operation         | Complexity     |
| ----------------- | -------------- |
| Insert (Average)  | **O(log n)**   |
| Insert (Worst)    | **O(n)**       |
| Inorder Traversal | **O(n)**       |
| Total Average     | **O(n log n)** |

This is the standard BST-based sorting approach (often called **Tree Sort**).
