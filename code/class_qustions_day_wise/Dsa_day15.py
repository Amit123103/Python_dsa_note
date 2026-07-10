'''
A social meadia platform stores friendships between users.

requirements:
    create a graph where each user is connected to their friends.
    Display all users and their friends in a formated way.
    Store all user names in a list.
    Sort the user names using Insertion sort.
    Ask the user to search for a user using Binary Search.
    If found, display the user's friends.
    Otherwise, display "User not found."
'''

# class Class:
#     def __init__(self):
#         self.graph = {}
#         self.users = []
#     def add_user(self, user):
#         if user not in self.graph:
#             self.graph[user] = []
#             self.users.append(user)
#     def add_friend(self, user, friend):
#         if user in self.graph and friend in self.graph:
#             self.graph[user].append(friend)
#     def display_users(self):
#         for user in self.graph:
#             print(f"{user}: {', '.join(self.graph[user])}")
#     def insertion_sort(self):
#         for i in range(1, len(self.users)):
#             key = self.users[i]
#             j = i - 1
#             while j >=0 and key < self.users[j]:
#                 self.users[j + 1] = self.users[j]
#                 j -= 1
#                 self.users[j + 1] = key
#     def binary_search(self, user):
#         low = 0
#         high = len(self.users) - 1
#         while low <= high:
#             mid_value = (low + high) // 2
#             if self.users[mid_value] == user:
#                 return mid_value
#             elif self.users[mid_value] < user:
#                 low = mid_value + 1
#             else:
#                 high = mid_value - 1
#         return -1
#     def search_user(self, user):
#         index = self.binary_search(user)
#         if index != -1:
#             print(f"{user}'s friends: {', '.join(self.graph[user])}")
#         else:
#             print("User not found.")

# class_instance = Class()
# class_instance.add_user("Alice")
# class_instance.add_user("Bob")
# class_instance.add_user("Charlie")
# class_instance.add_friend("Alice", "Bob")
# class_instance.add_friend("Alice", "Charlie")
# class_instance.display_users()  


'''
1. Merge Sort
2. Heap Sort
'''

# merge sort using to sort this list using recursion
'''
Split:
[5,2,3,8,2,3]

↓

[5,2,3]    [8,2,3]

↓

[5] [2,3] [8] [2,3]

↓

[5] [2] [3] [8] [2] [3]

Merge:

[2,3]
[2,5]
[2,3,5]

[2,3]
[2,3,8]

Final Merge:

[2,2,3,3,5,8]
'''

# var = [5, 2, 3, 8, 2, 3]

# def merge_sort(var):
#     if len(var) > 1:

#         # Find the middle index
#         mid_value = len(var) // 2

#         # Divide into left and right halves
#         left_half = var[:mid_value]
#         right_half = var[mid_value:]

#         # Recursively sort both halves
#         merge_sort(left_half)
#         merge_sort(right_half)

#         # Merge the sorted halves
#         i = 0  # Index for left_half
#         j = 0  # Index for right_half
#         k = 0  # Index for var

#         # Compare elements from both halves
#         while i < len(left_half) and j < len(right_half):

#             if left_half[i] <= right_half[j]:
#                 var[k] = left_half[i]
#                 i += 1
#             else:
#                 var[k] = right_half[j]
#                 j += 1

#             k += 1

#         # Copy remaining elements from left_half
#         while i < len(left_half):
#             var[k] = left_half[i]
#             i += 1
#             k += 1

#         # Copy remaining elements from right_half
#         while j < len(right_half):
#             var[k] = right_half[j]
#             j += 1
#             k += 1


# merge_sort(var)

# print(var)
        
# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# def merge_sort_iterative(arr):
#     width = 1
#     n = len(arr)

#     while width < n:
#         for i in range(0, n, 2 * width):
#             left = arr[i:i + width]
#             right = arr[i + width:i + 2 * width]

#             merged = merge(left, right)
#             arr[i:i + len(merged)] = merged

#         width *= 2

#     return arr


# var = [5, 2, 3, 8, 2, 3]
# print(merge_sort_iterative(var))

'''Heap Sort 
we can compress it unballanced tree 
'''


arr = [5, 7, 2, 4, 8]

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left
    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right
    # If largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the affected subtree
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)
    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify reduced heap
        heapify(arr, i, 0)


arr = [5, 7, 2, 4, 8]
heap_sort(arr)
print(arr)