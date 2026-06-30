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