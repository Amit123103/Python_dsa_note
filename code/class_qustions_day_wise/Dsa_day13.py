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

var = {
    'A': 1,
    'B': 4,
    'C': 3,
    'D': 2
}

sorted_var = dict(sorted(var.items(), key=lambda item: item[1]))
print(sorted_var)