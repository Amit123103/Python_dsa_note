'''In a **linked list**, you generally **swap the nodes (by changing pointers/references)** rather than swapping the data inside the nodes.

Bubble sorting 

* Bubble Sort compares **adjacent elements**.
* It swaps them if they are in the wrong order.
* After each pass, the **largest element moves to the end**.
* It is **stable** because equal elements keep their relative order.
* It is **in-place** because it uses constant extra memory.

1. start from left
2. moving larger element to right

'''

# [10, 9, 100, 20, 5] bubble sorting 

    
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         node1 = Node(data)
#         if self.head is None:
#             self.head = node1
#             return

#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = node1

#     def bubble_sort(self):
#         if self.head is None:
#             return

#         swapped = True
#         while swapped:
#             swapped = False
#             current = self.head

#             while current.next:
#                 if current.data > current.next.data:
#                     current.data, current.next.data = current.next.data, current.data
#                     swapped = True
#                 current = current.next

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

# list = LinkedList()

# for i in [10, 9, 100, 20, 5]:
#     list.append(i)

# print("Before Sorting:")
# list.display()

# list.bubble_sort()

# print("After Sorting:")
# list.display()



# list = [10, 9, 100, 20, 5]
# a = len(list)

# for i in range(a):
#     for j in range(a - i - 1):
#         print(list[i], list[j])
#         if list[j] > list[j + 1]:
#             list[j], list[j + 1] = list[j + 1], list[j]

# print(list)



# def bubble_sort(list):
#     n = len(list)

#     for i in range(n):
#         swapped = False
#         for j in range(n - i - 1):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#                 swapped = True
#         if not swapped:
#             break

#     return list


# var = [10, 9, 100, 20, 5]
# print(bubble_sort(var))


# def bubble_sort(var):
#     n = len(var)

#     for i in range(n):
#         for j in range(n - i - 1):   # Left to Right
#             print("Compare:", var[j], "and", var[j + 1])
#             if var[j] > var[j + 1]:
#                 # Value Swapping
#                 var[j], var[j + 1] = var[j + 1], var[j]
#                 print("Swap   :", var)

#     return var
# var = [10, 9, 100, 20, 5]
# print("Before:", var)
# bubble_sort(var)
# print("After :", var)



'''Selection sorting also know as unstable algorithm'''


# def selection_sort(var):
#     temp = len(var)
#     for i in range(temp):
#         min_index = i
#         for j in range(i + 1, temp):
#             if var[j] < var[min_index]:
#                 min_index = j
#         var[i], var[min_index] = var[min_index], var[i]
#     return var


# var = [10, 9, 100, 20, 5]

# print("Before_slection:", var)
# print("After_slection :", selection_sort(var))


# we have disconariy and we need to sort the dictonary according to key disct_var= {1:'value',
#                                                                                   5 : 'value',
#                                                                                   10: 'value'
#                                                                                    8: 'value'}

# dict_var = {
#     1: 'value',
#     5: 'value',
#     10: 'value',
#     8: 'value'
# }

# sorted_dict = dict(sorted(dict_var.items()))

# print(sorted_dict)

# def sort_dict(dict_var):
#     sorted_dict = dict(sorted(dict_var.items()))
#     return sorted_dict


# dict_var = {
#     1: 'value1',
#     5: 'value2',
#     10: 'value3',
#     8: 'value4'
# }

# result = sort_dict(dict_var)
# print(result)





# var = {10: 'asdf',
#        2: 'asdf',
#        5: 'asay',
#        8: 'asdf'}
# var = {'A' : 1,
#        'B' : 4,
#        'C' : 3,
#        'D': 2}
# sorted_var = dict(sorted(var.items()))
# print(sorted_var)
# lambda funtion using to solve it

# var = {
#     'A': 1,
#     'B': 4,
#     'C': 3,
#     'D': 2
# }

# sorted_var = dict(sorted(var.items(), key=lambda item: item[1]))
# print(sorted_var)


'''A circket coach has the scores of 15 players.
Requirements
Accepts scores of all players.
Display the original list.
sort the scores using Bubble sort.
Display the sorted scores.
Ask the coach to enter a player's score.
Search for the score using Binary Search.
Display the player's rank based on the sorted list. 
Also Display:
Highest score 
Lowest score 
total number of players'''



# Bubble Sort
# def bubble_sort(scores):
#     n = len(scores)

#     for i in range(n):
#         for j in range(n - i - 1):
#             if scores[j] > scores[j + 1]:
#                 scores[j], scores[j + 1] = scores[j + 1], scores[j]

#     return scores


# # Binary Search
# def binary_search(scores, target):
#     low = 0
#     high = len(scores) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if scores[mid] == target:
#             return mid
#         elif scores[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1


# # Main Program
# scores = []

# print("Enter scores of 15 players:")

# for i in range(15):
#     score = int(input(f"Player {i + 1}: "))
#     scores.append(score)

# # Original List
# print("\nOriginal Scores:")
# print(scores)

# # Bubble Sort
# sorted_scores = bubble_sort(scores.copy())

# print("\nSorted Scores (Ascending):")
# print(sorted_scores)

# # Binary Search
# target = int(input("\nEnter player's score to search: "))

# index = binary_search(sorted_scores, target)

# if index != -1:
#     # Rank in descending order
#     rank = len(sorted_scores) - index
#     print(f"Score found at position {index + 1} in ascending order.")
#     print(f"Player Rank: {rank}")
# else:
#     print("Score not found.")

# # Highest Score
# print("\nHighest Score:", sorted_scores[-1])

# # Lowest Score
# print("Lowest Score:", sorted_scores[0])

# # Total Players
# print("Total Number of Players:", len(sorted_scores))







'''A circket coach has the scores of 15 players.
Requirements
Accepts scores of all players.
Display the original list.
sort the scores using Bubble sort.
Display the sorted scores.
Ask the coach to enter a player's score.
Search for the score using Binary Search.
Display the player's rank based on the sorted list. 
Also Display:
Highest score 
Lowest score 
total number of players'''


'''

## Plan (Line by Line)

### Step 1

Create a function `bubble_sort(scores)` to sort the player scores.

### Step 2

Find the total number of scores using:

```python
n = len(scores)
```

### Step 3

Start the outer loop to perform Bubble Sort passes.

```python
for i in range(n):
```

### Step 4

Start the inner loop to compare adjacent elements.

```python
for j in range(n - i - 1):
```

### Step 5

Compare the current score with the next score.

```python
if scores[j] > scores[j + 1]:
```

### Step 6

Swap the scores if they are in the wrong order.

```python
scores[j], scores[j + 1] = scores[j + 1], scores[j]
```

### Step 7

Return the sorted list.

```python
return scores
```

---

## Binary Search

### Step 8

Create a function `binary_search(scores, target)`.

### Step 9

Initialize the first index.

```python
low = 0
```

### Step 10

Initialize the last index.

```python
high = len(scores) - 1
```

### Step 11

Continue searching while the search range exists.

```python
while low <= high:
```

### Step 12

Find the middle index.

```python
mid = (low + high) // 2
```

### Step 13

Check whether the middle score is the target.

```python
if scores[mid] == target:
```

### Step 14

Return the index if the score is found.

```python
return mid
```

### Step 15

If the target is greater than the middle score, search the right half.

```python
low = mid + 1
```

### Step 16

Otherwise, search the left half.

```python
high = mid - 1
```

### Step 17

If the score is not found, return `-1`.

```python
return -1
```

---

## Main Program

### Step 18

Create an empty list to store player scores.

```python
scores = []
```

### Step 19

Display a message asking the coach to enter the scores.

### Step 20

Use a loop to accept the scores of 15 players.

```python
for i in range(15):
```

### Step 21

Read each score from the user.

```python
score = int(input())
```

### Step 22

Store the score in the list.

```python
scores.append(score)
```

### Step 23

Display the original list of scores.

```python
print(scores)
```

### Step 24

Sort the scores using Bubble Sort.

```python
sorted_scores = bubble_sort(scores.copy())
```

### Step 25

Display the sorted scores.

```python
print(sorted_scores)
```

### Step 26

Ask the coach to enter a score to search.

```python
target = int(input())
```

### Step 27

Search for the score using Binary Search.

```python
index = binary_search(sorted_scores, target)
```

### Step 28

Check whether the score exists.

```python
if index != -1:
```

### Step 29

Calculate the player's rank.

```python
rank = len(sorted_scores) - index
```

### Step 30

Display the player's position and rank.

### Step 31

If the score is not found, display a suitable message.

```python
print("Score not found.")
```

### Step 32

Display the highest score.

```python
print(sorted_scores[-1])
```

### Step 33

Display the lowest score.

```python
print(sorted_scores[0])
```

### Step 34

Display the total number of players.

```python
print(len(sorted_scores))
```

---

## Flow of the Program

```text
Start
   │
   ▼
Accept 15 Player Scores
   │
   ▼
Display Original Scores
   │
   ▼
Sort Scores using Bubble Sort
   │
   ▼
Display Sorted Scores
   │
   ▼
Enter Score to Search
   │
   ▼
Binary Search
   │
   ├── Score Found ─► Display Position & Rank
   │
   └── Score Not Found
   │
   ▼
Display Highest Score
   │
   ▼
Display Lowest Score
   │
   ▼
Display Total Players
   │
   ▼
End
```

This step-by-step plan matches the structure of your code and is suitable for explaining it in an exam or viva.

'''
'''
# question

A circket coach has the scores of 15 players.
Requirements
Accepts scores of all players.
Display the original list.
sort the scores using Bubble sort.
Display the sorted scores.
Ask the coach to enter a player's score.
Search for the score using Binary Search.
Display the player's rank based on the sorted list. 
Also Display:
Highest score 
Lowest score 
total number of players
 

plan to excute the program

1. Create a Bubble Sort function to sort the player scores
2. Find the total number of scores using `len()`
3. Use the outer loop to perform Bubble Sort passes
4. Use the inner loop to compare adjacent scores
5. Compare the current score with the next score
6. Swap the scores if they are in the wrong order
7. Return the sorted list
8. Create a Binary Search function to search for a score
9. Initialize the first index (low)
10. Initialize the last index (high)
11. Find the middle index (mid)
12. Compare the middle score with the target score
13. Search the right half if the target is larger
14. Search the left half if the target is smaller
15. Return the index if the score is found; otherwise, return -1
16. Create an empty list to store player scores
17. Accept the scores of 15 players from the coach
18. Display the original list of scores
19. Sort the scores using Bubble Sort
20. Display the sorted scores
21. Accept the score to search
22. Search the score using Binary Search
23. Display the player's position and rank if found
24. Display "Score not found" if the score does not exist
25. Display the highest score
26. Display the lowest score
27. Display the total number of players
28. End

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head:
            self.head = new_node
            return
        score = self.head
        while score.next:
            score = score.next
        score.next = new_node
    def display(self):
        score = self.head
        while score:
            print(score.data, end=" ")
            temp = score.next
        print()

    # Bubble Sort
    def bubble_sort(self):
        if self.head:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True

                current = current.next

    # Binary Search (Convert Linked List to List)
    def binary_search(self, score):
        var = []
        list = self.head
        while list:
            var.append(list.data)
            list = list.next
        low = 0
        high = len(var) - 1
        while low <= high:
            mid_value = (low + high) // 2
            if var[mid_value] == score:
                return mid_value
            elif var[mid_value] < score:
                low = mid_value + 1
            else:
                high = mid_value - 1

        return -1

    def highest(self):
        score = self.head
        while score.next:
            score = score.next
        return score.data
    def lowest(self):
        return self.head.data
    def count(self):
        count = 0
        score = self.head
        while score:
            count += 1
            score = score.next

        return count

players = LinkedList()
print("Enter scores of 15 players:")
for i in range(15):
    score = int(input(f"Player {i+1}: "))
    players.append(score)
print("\nOriginal Scores:")
players.display()
players.bubble_sort()
print("\nSorted Scores:")
players.display()

score = int(input("\nEnter score to search: "))
index = players.binary_search(score)
if index != -1:
    rank = players.count() - index
    print("Score Found!")
    print("Rank:", rank)
else:
    print("Score Not Found!")

print("\nHighest Score:", players.highest())
print("Lowest Score :", players.lowest())
print("Total Players:", players.count())
            