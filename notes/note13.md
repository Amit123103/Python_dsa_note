'''in linkedlist we  have to chnage not value swap we need to sawap memory addres or node swaping '''

Yes, that's correct. This is an important interview concept.

In a **linked list**, you generally **swap the nodes (by changing pointers/references)** rather than swapping the data inside the nodes.

### Why?

A linked list is made up of nodes:

```text
[10 | • ] → [20 | • ] → [30 | • ] → NULL
```

Each node contains:

* **Data (value)**
* **Next pointer (memory address of the next node)**

When swapping nodes, you change the **next pointers**, not the values.

### Example

Original list:

```text
10 → 20 → 30 → 40
```

Suppose you want to swap nodes containing **20** and **40**.

❌ **Value Swapping**

```text
10 → 40 → 30 → 20
```

Here, only the data values changed.

✅ **Node Swapping (Pointer Swapping)**

```text
Before:
10 → Node(20) → 30 → Node(40)

After:
10 → Node(40) → 30 → Node(20)
```

The actual nodes move by updating their `next` pointers. Their data remains unchanged.

### Why do interviewers prefer node swapping?

* It tests your understanding of **pointer manipulation**.
* Some node data may be large objects, so swapping data is inefficient.
* In many interview problems, the question explicitly says **"swap nodes without swapping data."**

### Interview Answer

> In a linked list, we usually swap **nodes by changing their pointers (memory references)** instead of swapping the values stored in the nodes. This preserves the node data and demonstrates correct pointer manipulation.

### Example of pointer changes

Suppose:

```text
prev1 → A → next1
prev2 → B → next2
```

To swap **A** and **B**, you update the links:

```text
prev1.next = B
prev2.next = A

temp = A.next
A.next = B.next
B.next = temp
```

No data values are exchanged—only the links between nodes are updated.

**Tip for interviews:** If a problem says **"swap nodes without swapping data"**, your solution should modify the `next` pointers, not the `data` fields.


## Bubble Sort

**Bubble Sort** is a simple sorting algorithm that repeatedly compares **adjacent elements** and swaps them if they are in the wrong order. After each pass, the largest unsorted element "bubbles" to the end of the array.

### Example

Unsorted array:

```text
[5, 3, 8, 4, 2]
```

### Pass 1

```text
5 3 8 4 2

5 > 3 → Swap
3 5 8 4 2

5 < 8 → No Swap
3 5 8 4 2

8 > 4 → Swap
3 5 4 8 2

8 > 2 → Swap
3 5 4 2 8
```

Largest element (**8**) is now in its correct position.

### Pass 2

```text
3 5 4 2 8

3 < 5 → No Swap
3 5 4 2 8

5 > 4 → Swap
3 4 5 2 8

5 > 2 → Swap
3 4 2 5 8
```

Continue until the array becomes:

```text
[2, 3, 4, 5, 8]
```

---

## Python Code

```python
arr = [5, 3, 8, 4, 2]
n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
```

**Output:**

```text
[2, 3, 4, 5, 8]
```

---

## Optimized Bubble Sort

If the array is already sorted, we can stop early.

```python
arr = [5, 3, 8, 4, 2]
n = len(arr)

for i in range(n):
    swapped = False

    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    if not swapped:
        break

print(arr)
```

---

## Time Complexity

| Case                  | Complexity |
| --------------------- | ---------- |
| Best (already sorted) | **O(n)**   |
| Average               | **O(n²)**  |
| Worst                 | **O(n²)**  |

**Space Complexity:** **O(1)** (in-place)

---

## Interview Points

* Bubble Sort compares **adjacent elements**.
* It swaps them if they are in the wrong order.
* After each pass, the **largest element moves to the end**.
* It is **stable** because equal elements keep their relative order.
* It is **in-place** because it uses constant extra memory.

### Easy Way to Remember

Think of air bubbles rising in water:

```text
5 3 8 4 2
      ↑
The largest element "bubbles" to the end after each pass.
```

This is why the algorithm is called **Bubble Sort**.

procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        swapped := false
        for i := 1 to n - 1 inclusive do
            if A[i - 1] > A[i] then
                swap(A[i - 1], A[i])
                swapped := true
            end if
        end for
        n := n - 1 
    until not swapped
end procedure

## Selection Sort

**Selection Sort** finds the **smallest element** from the unsorted part of the array and places it at the correct position.

### Example

Array:

```text
[10, 9, 100, 20, 5]
```

### Pass 1

Find the smallest element:

```text
10  9  100  20  5
                ↑ Smallest = 5
```

Swap **10** and **5**

```text
[5, 9, 100, 20, 10]
```

---

### Pass 2

Find the smallest element from:

```text
9  100  20  10
```

Smallest = **9**

No swap needed.

```text
[5, 9, 100, 20, 10]
```

---

### Pass 3

Find the smallest element from:

```text
100  20  10
```

Smallest = **10**

Swap **100** and **10**

```text
[5, 9, 10, 20, 100]
```

---

### Pass 4

Find the smallest element from:

```text
20 100
```

Smallest = **20**

No swap.

```text
[5, 9, 10, 20, 100]
```

✅ **Sorted Array**

```text
[5, 9, 10, 20, 100]
```

---

# Python Code

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [10, 9, 100, 20, 5]

print("Before:", arr)
print("After :", selection_sort(arr))
```

### Output

```text
Before: [10, 9, 100, 20, 5]
After : [5, 9, 10, 20, 100]
```

---

## How it Works

```text
Pass 1 → Find smallest → Put it at index 0

Pass 2 → Find smallest → Put it at index 1

Pass 3 → Find smallest → Put it at index 2

Pass 4 → Find smallest → Put it at index 3
```

---

## Bubble Sort vs Selection Sort

| Bubble Sort                      | Selection Sort                          |
| -------------------------------- | --------------------------------------- |
| Compares adjacent elements       | Finds the smallest element              |
| Many swaps                       | At most one swap per pass               |
| Largest element moves to the end | Smallest element moves to the beginning |
| Time Complexity: **O(n²)**       | Time Complexity: **O(n²)**              |

### Easy Trick to Remember

* **Bubble Sort** → **Swap again and again** with adjacent elements.
* **Selection Sort** → **Select the smallest element** and place it in the correct position.

This is the easiest way to remember the difference in interviews.


deep copy and shello copy
