# Heap Data Structure

A **Heap** is a **Complete Binary Tree** that satisfies the **Heap Property**.

A heap is mainly used to efficiently get the **minimum** or **maximum** element.

---

## Complete Binary Tree

A Complete Binary Tree means:

* Every level is completely filled except possibly the last.
* The last level is filled from **left to right**.

Example:

```text
        10
       /  \
      20   30
     / \   /
    40 50 60
```

✅ Complete Binary Tree

---

# Types of Heap

There are two types:

## 1. Max Heap

The parent is always **greater than or equal to** its children.

```text
         50
       /    \
     30      40
    /  \    /  \
   10  20 15  25
```

Parent ≥ Children

```
50 > 30,40
30 > 10,20
40 > 15,25
```

The largest element is always at the root.

---

## 2. Min Heap

The parent is always **smaller than or equal to** its children.

```text
         5
       /   \
      8     10
     / \    / \
   15 20 30 25
```

Parent ≤ Children

The smallest element is always at the root.

---

# Array Representation

A heap is usually stored in an array.

Example

```text
        10
      /    \
     20     30
    /  \    /
   40  50 60
```

Array

```python
[10, 20, 30, 40, 50, 60]
```

---

## Index Relationship

Suppose

```python
arr = [10,20,30,40,50,60]
```

If the parent index is **i**

Left Child

```python
2*i + 1
```

Right Child

```python
2*i + 2
```

Parent

```python
(i-1)//2
```

Example

```text
Index : 0 1 2 3 4 5
Value :10 20 30 40 50 60
```

For index = 1

```python
Left = 2(1)+1 = 3
Right = 2(1)+2 = 4
```

Values

```text
Parent = 20

Left = 40

Right = 50
```

---

# Insertion in Heap

Insert

```text
10
20
15
30
40
```

### Step 1

Insert 10

```text
10
```

---

### Step 2

Insert 20

```text
10
/
20
```

20 > 10 (Min Heap)

No swap.

---

### Step 3

Insert 15

```text
   10
  /  \
20   15
```

No swap.

---

### Step 4

Insert 30

```text
      10
     /  \
   20    15
  /
30
```

No swap.

---

### Step 5

Insert 40

```text
      10
     /  \
   20    15
  / \
30 40
```

Finished.

---

# Example with Swapping

Insert

```text
20
15
10
```

Step 1

```text
20
```

---

Insert 15

```text
20
/
15
```

Since

```
15 < 20
```

Swap

```text
15
/
20
```

---

Insert 10

```text
   15
  /  \
20   10
```

Swap

```text
   10
  /  \
20   15
```

This process is called **Heapify Up** (or **Sift Up**).

---

# Deletion from Heap

Delete always removes the **root**.

Example

```text
      10
     /  \
   20    15
  / \
30 40
```

Remove 10

Move the last element (40) to the root.

```text
      40
     /  \
   20    15
  /
30
```

Now fix the heap.

40 > 15

Swap

```text
      15
     /  \
   20    40
  /
30
```

This process is called **Heapify Down** (or **Sift Down**).

---

# Heapify

Heapify rearranges nodes to restore the heap property.

### Heapify Up

```text
Insert
↓

Compare with parent

↓

Swap if needed

↓

Repeat
```

---

### Heapify Down

```text
Delete root

↓

Move last element to root

↓

Compare with children

↓

Swap with smaller (Min Heap) or larger (Max Heap)

↓

Repeat
```

---

# Python (`heapq`)

Python's built-in `heapq` module implements a **Min Heap**.

### Create a Heap

```python
import heapq

heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 2)

print(heap)
```

Output

```python
[2, 5, 20, 10]
```

---

### Remove the Smallest Element

```python
import heapq

heap = [2, 5, 20, 10]

smallest = heapq.heappop(heap)

print(smallest)
print(heap)
```

Output

```python
2
[5, 10, 20]
```

---

### Convert a List into a Heap

```python
import heapq

arr = [9, 5, 1, 8, 3]

heapq.heapify(arr)

print(arr)
```

Output

```python
[1, 3, 9, 8, 5]
```

---

### Max Heap in Python

Python doesn't provide a built-in max heap, but you can simulate one by storing negative values.

```python
import heapq

heap = []

nums = [5, 8, 2, 10]

for num in nums:
    heapq.heappush(heap, -num)

while heap:
    print(-heapq.heappop(heap))
```

Output

```text
10
8
5
2
```

---

# Time Complexity

| Operation            | Time Complexity |
| -------------------- | --------------: |
| Insert               |        O(log n) |
| Delete Root          |        O(log n) |
| Peek (Min/Max)       |            O(1) |
| Heapify (Build Heap) |            O(n) |
| Search               |            O(n) |

---

# Applications of Heap

* Priority Queue
* Heap Sort
* Dijkstra's Shortest Path Algorithm
* Prim's Minimum Spanning Tree Algorithm
* Task Scheduling
* Finding the K Largest or K Smallest Elements
* Median of a Data Stream

### Key Takeaways

* A heap is a **complete binary tree** stored efficiently in an array.
* **Min Heap:** parent ≤ children; smallest element at the root.
* **Max Heap:** parent ≥ children; largest element at the root.
* Insert and delete operations take **O(log n)** due to heapify.
* Python's `heapq` module provides a **Min Heap** implementation.

Here are complete **Merge Sort Notes** with explanation, recursion tree, and a full dry run.

# Merge Sort

## Definition

**Merge Sort** is a **Divide and Conquer** sorting algorithm.

It works in three steps:

1. **Divide** the array into two halves.
2. **Recursively sort** each half.
3. **Merge** the two sorted halves into one sorted array.

Unlike Bubble Sort or Selection Sort, Merge Sort **does not sort by swapping adjacent elements**. Instead, it repeatedly splits the array and merges sorted pieces.

---

# Divide and Conquer

```text
                Problem
                   |
        -----------------------
        |                     |
     Divide               Divide
        |                     |
   Smaller Problem     Smaller Problem
        |                     |
        --------Conquer---------
                 |
              Merge
                 |
          Final Sorted Array
```

---

# Algorithm

```text
Step 1
Split the array into two halves.

↓

Step 2
Repeat until every sub-array contains only one element.

↓

Step 3
Merge two sorted arrays into one sorted array.

↓

Step 4
Continue merging until only one sorted array remains.
```

---

# Example

```python
arr = [5, 2, 3, 8, 2, 3]
```

---

# Step 1 — Divide

Length = 6

```text
mid = 6 // 2 = 3
```

```text
Left  = [5,2,3]
Right = [8,2,3]
```

Tree

```text
               [5,2,3,8,2,3]
                /         \
          [5,2,3]      [8,2,3]
```

---

## Divide Left Again

```text
[5,2,3]

mid = 1
```

```text
Left = [5]

Right = [2,3]
```

Tree

```text
               [5,2,3]
               /     \
            [5]    [2,3]
```

---

## Divide [2,3]

```text
mid = 1
```

```text
Left = [2]

Right = [3]
```

Tree

```text
        [2,3]
        /   \
      [2]   [3]
```

Now every array has one element.

Stop recursion.

---

## Divide Right Side

```text
[8,2,3]

mid = 1
```

```text
Left = [8]

Right = [2,3]
```

Again

```text
        [2,3]
       /    \
     [2]    [3]
```

Stop recursion.

---

# Complete Recursion Tree

```text
                     [5,2,3,8,2,3]
                    /             \
              [5,2,3]          [8,2,3]
              /     \          /      \
           [5]     [2,3]     [8]    [2,3]
                    /  \               /  \
                  [2] [3]           [2]  [3]
```

Notice that the recursion **always goes down** until each array has **one element**.

---

# Why Stop at One Element?

Because a single element is **already sorted**.

Examples

```text
[5] ✓ Sorted

[10] ✓ Sorted

[100] ✓ Sorted
```

No further splitting is needed.

---

# Returning from Recursion (Merge Phase)

Once the recursion reaches the bottom, it starts returning.

Now Merge Sort begins merging.

---

## Merge 1

Merge

```text
[2]

[3]
```

Compare

```text
2 < 3
```

Result

```text
[2,3]
```

---

## Merge 2

Merge

```text
[5]

[2,3]
```

Compare

```text
5 vs 2

Take 2
```

Result

```text
[2]
```

Compare

```text
5 vs 3

Take 3
```

Result

```text
[2,3]
```

No more elements on the right.

Copy remaining

```text
5
```

Result

```text
[2,3,5]
```

---

## Merge 3

Merge

```text
[2]

[3]
```

Result

```text
[2,3]
```

---

## Merge 4

Merge

```text
[8]

[2,3]
```

Compare

```text
8 vs 2

Take 2
```

Compare

```text
8 vs 3

Take 3
```

Copy remaining

```text
8
```

Result

```text
[2,3,8]
```

---

## Final Merge

Merge

```text
Left

[2,3,5]

Right

[2,3,8]
```

Compare each element:

```text
2 vs 2

Take Left 2

Result

[2]
```

```text
3 vs 2

Take Right 2

Result

[2,2]
```

```text
3 vs 3

Take Left 3

Result

[2,2,3]
```

```text
5 vs 3

Take Right 3

Result

[2,2,3,3]
```

```text
5 vs 8

Take 5

Result

[2,2,3,3,5]
```

Right side still has

```text
8
```

Final result

```text
[2,2,3,3,5,8]
```

---

# Full Dry Run

```text
Input

[5,2,3,8,2,3]

↓

Split

[5,2,3]

[8,2,3]

↓

Split

[5]

[2,3]

[8]

[2,3]

↓

Split

[2]

[3]

[2]

[3]

↓

Merge

[2]+[3]

↓

[2,3]

↓

Merge

[5]+[2,3]

↓

[2,3,5]

↓

Merge

[2]+[3]

↓

[2,3]

↓

Merge

[8]+[2,3]

↓

[2,3,8]

↓

Final Merge

[2,3,5]

+

[2,3,8]

↓

[2,2,3,3,5,8]
```

---

# Merge Function Logic

```python
while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        arr[k] = left[i]
        i += 1
    else:
        arr[k] = right[j]
        j += 1
    k += 1
```

**Explanation:**

* `i` points to the current element in the left half.
* `j` points to the current element in the right half.
* `k` points to the position in the original array where the next smallest element should be placed.
* Compare `left[i]` and `right[j]`.
* Copy the smaller element into `arr[k]`.
* Move the corresponding pointer (`i` or `j`) and then increment `k`.
* Continue until one half is exhausted.
* Finally, copy any remaining elements from the non-empty half into `arr`.

---

# Complete Merge Sort Code

```python
def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [5, 2, 3, 8, 2, 3]

merge_sort(arr)

print(arr)
```

**Output**

```python
[2, 2, 3, 3, 5, 8]
```

---

# Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n log n) |

---

# Space Complexity

```text
O(n)
```

Merge Sort creates temporary arrays (`left` and `right`) during merging, so it is **not an in-place sorting algorithm**.

---

# Advantages

* Stable sorting algorithm (preserves the order of equal elements).
* Guaranteed **O(n log n)** performance in all cases.
* Excellent for sorting large datasets.
* Works well with linked lists and external sorting.

---

# Disadvantages

* Requires extra memory (`O(n)`).
* Slower than Quick Sort in many practical in-memory scenarios because of additional copying.
* Recursive implementation adds function call overhead.

---

# Interview Points

* **Algorithm Type:** Divide and Conquer
* **Stable:** ✅ Yes
* **In-place:** ❌ No
* **Recursive:** ✅ Yes
* **Best/Average/Worst Time:** **O(n log n)**
* **Space Complexity:** **O(n)**
* **Stopping Condition (Base Case):** `len(arr) <= 1`

It sounds like you mean **"Shrink Tree"**. In DSA, there isn't a standard data structure or algorithm called a "Shrink Tree." You might be referring to one of these concepts:

## 1. Skew Tree (Most Likely)

A **Skew Tree** is a binary tree where every node has only one child.

### Left Skewed Tree

```text
        10
       /
      20
     /
    30
   /
  40
```

### Right Skewed Tree

```text
10
  \
   20
     \
      30
        \
         40
```

**Properties:**

* Every node has only one child.
* Height = Number of nodes.
* Similar to a linked list.
* Search, insertion, and deletion can become **O(n)** in the worst case.

---

## 2. Strict Binary Tree

Every node has either:

* **0 children**, or
* **2 children**

Example:

```text
        1
      /   \
     2     3
    / \
   4   5
```

✅ Valid Strict Binary Tree

Not valid:

```text
      1
     /
    2
```

because node `1` has only one child.

---

## 3. Complete Binary Tree

Every level is completely filled except possibly the last, and the last level is filled from left to right.

```text
        1
      /   \
     2     3
    / \   /
   4  5  6
```

This is the type of tree used by a **Heap**.

---

## 4. Perfect Binary Tree

All internal nodes have exactly **2 children**, and all leaf nodes are at the **same level**.

```text
          1
       /     \
      2       3
     / \     / \
    4   5   6   7
```

---

## 5. Full Binary Tree

Another name often used for a **Strict Binary Tree**.

---

## 6. Balanced Binary Tree

The height difference between the left and right subtrees of every node is at most **1**.

```text
        1
      /   \
     2     3
    /
   4
```

Balanced trees provide efficient operations, typically **O(log n)**.

---

## Common Types of Trees to Learn

| Tree Type                 | Description                             |
| ------------------------- | --------------------------------------- |
| Binary Tree               | Each node has at most 2 children        |
| Binary Search Tree (BST)  | Left < Root < Right                     |
| Complete Binary Tree      | Used in Heaps                           |
| Full (Strict) Binary Tree | Every node has 0 or 2 children          |
| Perfect Binary Tree       | All levels completely filled            |
| Balanced Binary Tree      | Height difference ≤ 1                   |
| Left Skewed Tree          | Only left children                      |
| Right Skewed Tree         | Only right children                     |
| AVL Tree                  | Self-balancing BST                      |
| Red-Black Tree            | Self-balancing BST                      |
| B-Tree                    | Database and file systems               |
| Trie                      | Stores strings efficiently              |
| Heap                      | Complete Binary Tree with heap property |

If by **"srink tree"** you meant something else (for example, a term from your class notes or a specific interview question), tell me the exact spelling or share a screenshot, and I'll explain that concept.


# Types of Trees in Data Structures (DSA)

Below are the most important tree types you should know for interviews and DSA.

---

# 1. General Tree

A node can have any number of children.

```text
        A
      / | \
     B  C  D
    / \
   E   F
```

---

# 2. Binary Tree

Each node has at most **2 children**.

```text
      1
     / \
    2   3
```

---

# 3. Full Binary Tree (Strict Binary Tree / Proper Binary Tree)

Every node has **0 or 2 children**.

```text
        1
      /   \
     2     3
    / \
   4   5
```

---

# 4. Perfect Binary Tree

* Every internal node has 2 children.
* All leaf nodes are at the same level.

```text
          1
       /     \
      2       3
     / \     / \
    4   5   6   7
```

---

# 5. Complete Binary Tree

* Every level is completely filled except possibly the last.
* Last level fills from left to right.

```text
        1
      /   \
     2     3
    / \   /
   4   5 6
```

**Used in Heap.**

---

# 6. Balanced Binary Tree

Height difference between left and right subtree ≤ 1.

```text
       1
      / \
     2   3
    /
   4
```

---

# 7. Degenerate Tree

Every node has only one child.

```text
1
 \
  2
   \
    3
     \
      4
```

Looks like a linked list.

---

# 8. Left Skewed Tree

Every node has only a left child.

```text
      1
     /
    2
   /
  3
 /
4
```

---

# 9. Right Skewed Tree

Every node has only a right child.

```text
1
 \
  2
   \
    3
     \
      4
```

---

# 10. Binary Search Tree (BST)

Left < Root < Right

```text
        50
      /    \
    30      70
   /  \    /  \
 20  40  60  80
```

---

# 11. AVL Tree

A self-balancing Binary Search Tree.

```text
        30
      /    \
    20      40
   /
 10
```

Automatically rotates to remain balanced.

---

# 12. Red-Black Tree

A self-balancing BST using red and black colors.

```text
      (B)20
      /    \
   (R)10  (R)30
```

Used in:

* Java `TreeMap`
* C++ `map`
* Linux Kernel

---

# 13. Splay Tree

Frequently accessed nodes move to the root.

```text
Search

↓

Rotate

↓

Node becomes Root
```

---

# 14. Treap

Combination of:

* BST
* Heap

Maintains:

* BST property
* Heap priority

---

# 15. Cartesian Tree

Combines:

* Heap property
* Inorder traversal property

---

# 16. Heap

Complete Binary Tree.

Types:

* Min Heap
* Max Heap

```text
        5
      /   \
     8     9
    / \
   15 20
```

---

# 17. B Tree

Used in:

* Databases
* File Systems

Allows many children.

```text
        [20 40]
       /   |   \
    ...   ...  ...
```

---

# 18. B+ Tree

Extension of B Tree.

All records stored in leaf nodes.

Used in:

* MySQL
* Oracle
* PostgreSQL

---

# 19. Trie (Prefix Tree)

Stores strings efficiently.

```text
          Root
         /
        c
       /
      a
     / \
    t   r
```

Words:

* cat
* car

---

# 20. Radix Tree

Compressed Trie.

Used in:

* Routers
* IP Lookup
* Linux Kernel

---

# 21. Segment Tree

Range queries.

Example:

```text
Sum(2,5)

Minimum

Maximum
```

---

# 22. Fenwick Tree (Binary Indexed Tree)

Efficient:

* Prefix Sum
* Updates

Time:

```text
O(log n)
```

---

# 23. Expression Tree

Represents mathematical expressions.

```text
        +
      /   \
     *     5
    / \
   3   4
```

Represents:

```text
(3 × 4) + 5
```

---

# 24. Parse Tree

Used by:

* Compilers
* Interpreters

---

# 25. Syntax Tree (Abstract Syntax Tree - AST)

Simplified Parse Tree.

Used by:

* Python
* Java
* C Compiler

---

# 26. Decision Tree

Used in Machine Learning.

```text
Age > 18?

Yes

No
```

---

# 27. N-ary Tree

Each node can have up to **N** children.

```text
        A
      / | | \
     B  C D  E
```

---

# 28. Tournament Tree

Used in:

* Scheduling
* Finding minimum/maximum efficiently

---

# 29. Huffman Tree

Used in:

* Data Compression
* ZIP
* JPEG
* PNG

---

# 30. Suffix Tree

Stores all suffixes of a string.

Used in:

* Pattern Matching
* DNA Analysis

---

# 31. KD Tree (K-Dimensional Tree)

Stores multi-dimensional data.

Used in:

* AI
* Machine Learning
* Computer Graphics

---

# 32. Quad Tree

Each node has **4 children**.

Used in:

* GIS
* Games
* Image Processing

---

# 33. Octree

Each node has **8 children**.

Used in:

* 3D Graphics
* Game Engines

---

# 34. Interval Tree

Stores intervals.

Example:

```text
[5,10]

[8,15]

[20,30]
```

---

# 35. Rope Tree

Efficient string manipulation.

Used in:

* Text Editors
* IDEs

---

# Complete List

| No. | Tree Name                          |
| --: | ---------------------------------- |
|   1 | General Tree                       |
|   2 | Binary Tree                        |
|   3 | Full (Strict) Binary Tree          |
|   4 | Perfect Binary Tree                |
|   5 | Complete Binary Tree               |
|   6 | Balanced Binary Tree               |
|   7 | Degenerate Tree                    |
|   8 | Left Skewed Tree                   |
|   9 | Right Skewed Tree                  |
|  10 | Binary Search Tree (BST)           |
|  11 | AVL Tree                           |
|  12 | Red-Black Tree                     |
|  13 | Splay Tree                         |
|  14 | Treap                              |
|  15 | Cartesian Tree                     |
|  16 | Heap (Min Heap, Max Heap)          |
|  17 | B-Tree                             |
|  18 | B+ Tree                            |
|  19 | Trie (Prefix Tree)                 |
|  20 | Radix Tree                         |
|  21 | Segment Tree                       |
|  22 | Fenwick Tree (Binary Indexed Tree) |
|  23 | Expression Tree                    |
|  24 | Parse Tree                         |
|  25 | Abstract Syntax Tree (AST)         |
|  26 | Decision Tree                      |
|  27 | N-ary Tree                         |
|  28 | Tournament Tree                    |
|  29 | Huffman Tree                       |
|  30 | Suffix Tree                        |
|  31 | KD Tree                            |
|  32 | Quad Tree                          |
|  33 | Octree                             |
|  34 | Interval Tree                      |
|  35 | Rope Tree                          |

### Most Important for DSA Interviews

Focus on these first:

* Binary Tree
* Binary Search Tree (BST)
* Full Binary Tree
* Perfect Binary Tree
* Complete Binary Tree
* Balanced Binary Tree
* Left & Right Skewed Trees
* AVL Tree
* Red-Black Tree
* Heap (Min & Max)
* Trie
* Segment Tree
* Fenwick Tree (BIT)
* B-Tree and B+ Tree
