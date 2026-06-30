# Explanation of Your Code (Line by Line)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
```

## What is a Node?

A **Node** is a single element of a linked list.

Imagine a train.

```
[10] ---> [20] ---> [30] ---> None
```

Each box is called a **Node**.

Every node has **two parts**:

```
+--------------------+
| data | reference   |
+--------------------+
```

Example:

```
+-------------+
| 10 | ------ |---->
+-------------+
```

* `data` stores the value.
* `ref` stores the address of the next node.

---

## Constructor

```python
def __init__(self, data):
```

The constructor runs automatically whenever we create a node.

Example

```python
n1 = Node(10)
```

Now Python executes

```python
self.data = 10
self.ref = None
```

Memory looks like

```
n1

+----------------+
| data = 10      |
| ref = None     |
+----------------+
```

---

## Why

```python
self.data = data
```

Stores the actual value.

If we don't write this,

```
Node(10)
```

will not remember 10.

---

## Why

```python
self.ref = None
```

Initially the node doesn't know which node comes next.

So we set

```
ref = None
```

which means

```
No next node
```

---

# Linked List Class

```python
class LinkedList:
```

This class manages all nodes.

Think of it as the controller.

---

## Constructor

```python
def __init__(self):
    self.head = None
```

Initially the list is empty.

```
Head

None
```

---

## Why do we need `head`?

The **head** stores the address of the first node.

Example

```
Head

 |
 V

+----+----+
|10  | *------> None
+----+----+
```

Without the head, we cannot access the linked list.

---

# Insert at Beginning

```python
def insert_start(self, data):
```

This function inserts a node at the beginning.

---

## Step 1

```python
new_node = Node(data)
```

Create a new node.

Suppose

```python
insert_start(30)
```

Memory

```
new_node

+-----------+
|30 | None  |
+-----------+
```

---

## Step 2

```python
new_node.ref = self.head
```

Make the new node point to the old first node.

Suppose list already contains

```
Head

 |
 V

10 -->20-->None
```

After

```python
new_node.ref = self.head
```

```
30 ---->
         10 --->20
```

---

## Step 3

```python
self.head = new_node
```

Now move the head to the new node.

```
Head

 |
 V

30 -->10-->20-->None
```

---

# Insert Between

```python
def insert_betw(self, data, prev):
```

Here

```
prev
```

means

**Insert after this node.**

Suppose

```
10 --->20 --->30
```

We want

```
10 --->15 --->20 --->30
```

Here

```
prev = node having 10
```

---

## Step 1

```python
new_node = Node(data)
```

Creates

```
15
```

```
15 ---> None
```

---

## Step 2

```python
new_node.ref = prev.ref
```

Currently

```
10 --->20
```

`prev.ref`

points to

```
20
```

Now

```
15 --->20
```

Memory

```
10 --->20

15 --->20
```

---

## Step 3

```python
prev.ref = new_node
```

Now

```
10 --->15 --->20
```

Done.

---

# Complete Diagram

Before

```
Head

 |
 V

10 -------->20-------->30-------->None
```

After

```python
insert_betw(15,node10)
```

```
Head

 |
 V

10 ------->15-------->20-------->30-------->None
```

---

# Why Do We Write These Statements?

| Code                       | Why?                                         |
| -------------------------- | -------------------------------------------- |
| `class Node`               | Creates a blueprint for each node.           |
| `self.data`                | Stores the value in the node.                |
| `self.ref`                 | Stores the address of the next node.         |
| `head`                     | Keeps track of the first node in the list.   |
| `new_node = Node(data)`    | Creates a new node object.                   |
| `new_node.ref = self.head` | Connects the new node to the old first node. |
| `self.head = new_node`     | Makes the new node the first node.           |
| `new_node.ref = prev.ref`  | Links the new node to the node after `prev`. |
| `prev.ref = new_node`      | Links `prev` to the newly inserted node.     |

---

# Same Code with Detailed Comments

```python
# Node class represents one element of the linked list
class Node:

    # Constructor
    def __init__(self, data):

        # Store the value in the node
        self.data = data

        # Store the address of the next node
        # Initially there is no next node
        self.ref = None


# Linked List class
class LinkedList:

    # Constructor
    def __init__(self):

        # Initially the list is empty
        # Head points to the first node
        self.head = None

    # Insert a node at the beginning
    def insert_start(self, data):

        # Create a new node
        new_node = Node(data)

        # New node points to the current first node
        new_node.ref = self.head

        # Move the head to the new node
        self.head = new_node

    # Insert a node after a given previous node
    def insert_betw(self, data, prev):

        # Create a new node
        new_node = Node(data)

        # New node points to the next node of prev
        new_node.ref = prev.ref

        # Previous node now points to the new node
        prev.ref = new_node
```

This is the standard implementation of inserting at the beginning and inserting after a given node in a **singly linked list**





To **delete the last node** in a singly linked list, there are **three cases**:

1. The list is empty.
2. The list has only one node.
3. The list has more than one node.

## Code

```python
def delete_last(self):

    # Case 1: Linked list is empty
    if self.head is None:
        print("Linked List is Empty")
        return

    # Case 2: Only one node
    if self.head.ref is None:
        self.head = None
        return

    # Case 3: More than one node
    current = self.head

    # Move to the second last node
    while current.ref.ref is not None:
        current = current.ref

    # Delete the last node
    current.ref = None
```

---

## Example

Before:

```text
Head
 |
 V
10 → 20 → 30 → 40 → None
```

### Step 1

`current` starts at `10`.

### Step 2

The loop:

```python
while current.ref.ref is not None:
    current = current.ref
```

moves `current` until it reaches the **second last node** (`30`).

Now:

```text
Head
 |
 V
10 → 20 → 30 → 40 → None
           ^
        current
```

### Step 3

```python
current.ref = None
```

Now the list becomes:

```text
Head
 |
 V
10 → 20 → 30 → None
```

The node containing `40` is no longer connected to the list, so it is effectively deleted.

---

### Why do we use `current.ref.ref`?

We want to stop at the **second last node**, not the last one.

Suppose:

```text
10 → 20 → 30 → 40 → None
```

When `current` is `30`:

* `current.ref` is `40`
* `current.ref.ref` is `None`

So the loop stops, and we can simply do:

```python
current.ref = None
```

which removes the last node.




Below is a **complete Singly Linked List program** that includes the most common operations asked in **CSE205/Data Structures**.

```python
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# Linked List Class
class Linkedlist:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_new(self, data):
        node = Node(data)
        node.ref = self.head
        self.head = node

    # Insert at End
    def insert_end(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        current = self.head

        while current.ref is not None:
            current = current.ref

        current.ref = node

    # Find Node using Value
    def find_node(self, value):

        current = self.head

        while current is not None:

            if current.data == value:
                return current

            current = current.ref

        return None

    # Insert After a Given Value
    def insert_btw(self, data, value):

        prev = self.find_node(value)

        if prev is None:
            print("Value Not Found")
            return

        node = Node(data)
        node.ref = prev.ref
        prev.ref = node

    # Search Value
    def search(self, value):

        current = self.head

        while current is not None:

            if current.data == value:
                print("Value Found")
                return

            current = current.ref

        print("Value Not Found")

    # Delete First Node
    def delete_first(self):

        if self.head is None:
            print("Linked List is Empty")
            return

        self.head = self.head.ref

    # Delete Last Node
    def delete_last(self):

        if self.head is None:
            print("Linked List is Empty")
            return

        if self.head.ref is None:
            self.head = None
            return

        current = self.head

        while current.ref.ref is not None:
            current = current.ref

        current.ref = None

    # Delete by Value
    def delete_node(self, value):

        if self.head is None:
            print("Linked List is Empty")
            return

        if self.head.data == value:
            self.head = self.head.ref
            return

        current = self.head

        while current.ref is not None:

            if current.ref.data == value:
                current.ref = current.ref.ref
                return

            current = current.ref

        print("Value Not Found")

    # Display Linked List
    def display(self):

        if self.head is None:
            print("Linked List is Empty")
            return

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.ref

        print("None")
```

---

## Example

```python
ll = Linkedlist()

ll.insert_new(20)
ll.insert_new(10)
ll.insert_end(30)
ll.insert_end(40)

ll.display()
```

Output:

```
10 -> 20 -> 30 -> 40 -> None
```

---

### Search

```python
ll.search(30)
```

Output:

```
Value Found
```

---

### Insert After Value

```python
ll.insert_btw(25, 20)
```

Output:

```
10 -> 20 -> 25 -> 30 -> 40 -> None
```

---

### Delete First

```python
ll.delete_first()
```

Output:

```
20 -> 25 -> 30 -> 40 -> None
```

---

### Delete Last

```python
ll.delete_last()
```

Output:

```
20 -> 25 -> 30 -> None
```

---

### Delete by Value

```python
ll.delete_node(25)
```

Output:

```
20 -> 30 -> None
```

---

## These are the main linked list operations commonly asked in CSE205:

1. ✅ Create Node
2. ✅ Create Linked List
3. ✅ Insert at Beginning
4. ✅ Insert at End
5. ✅ Insert After a Value (Between)
6. ✅ Search a Value
7. ✅ Find a Node
8. ✅ Delete First Node
9. ✅ Delete Last Node
10. ✅ Delete a Node by Value
11. ✅ Display the Linked List

Mastering these operations will prepare you for most singly linked list questions in exams.
