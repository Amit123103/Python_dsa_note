'''Algorithm'''

'''Easy Formula to Remember
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
Moves the larger element toward the end.'''

# list = [2, 100, 9, 105, 10, 20, 15, 36, 55, 42]
# bubble = len(list)
# for i in range(bubble - 1):
#     for j in range(bubble - 1 - i):
#         if list[j] > list[j + 1]:
#             list[j], list[j + 1] = list[j + 1], list[j]

# print("Sorted List:", list)


# list = [2, 100, 9, 105, 10, 20, 15, 36, 55, 42]

# print(list.index(20))
# print(20 in list)

# list1 = 20

# for i in range(len(list)):
#     if list[i] == list1:
#         print("Found at index:", i)
#         break
    
# list1 = 20
# i = 0
# while i < len(list):
#     if list[i] == list1:
#         print("Found:", i)
#         break
#     i += 1

# class Search:
#     def search(self, list1, list2):
#         i = 0
#         while i < len(list1):
#             if list1[i] == list2:
#                 print("Found:", i)
#                 return
#             i += 1
#         print("Not Found")
# var = Search()

# list = [2, 100, 9, 105, 10, 20, 15, 36, 55, 42]

# var.search(list, 20)


# binary search tree 


# sort = [2, 9, 10, 15, 20, 36, 42, 55, 100, 105]

# # mid element

# element = 20

# low = 0
# high = len(sort) - 1

# while low <= high:

#     mid = (low + high) // 2

#     if sort[mid] == element:
#         print("Found at index:", mid)
#         break

#     elif sort[mid] < element:
#         low = mid + 1

#     else:
#         high = mid - 1
        
        
        
# def binary_search(var, element):

#     low = 0
#     high = len(var) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if var[mid] == element:
#             print("Found at index:", mid)
#             return
#         elif var[mid] < element:
#             low = mid + 1
#         else:
#             high = mid - 1
#     print("Not Found")


# var = [2, 9, 10, 15, 20, 36, 42, 55, 100, 105]

# binary_search(var, 20)


# def search(var, element):
#     sorted_var= var.sort()
#     mid_index = len(sorted_var)//2
#     if sorted_var[mid_index] <element:
#         search(sorted_var[mid_index: ],element )
#     elif sorted_var[mid_index] > element:
#         search(sorted_var[: mid_index+1], element)
        
#     else:
#         print(f'{element} found on the index{var.mid.index}')
        
        
# var = [2, 100, 9, 105, 10, 20, 15, 36, 55, 42]

# print(search(var, 20))


# def search(var, element):

#     sorted_var = sorted(var)      # var.sort() returns None

#     mid_index = len(sorted_var) // 2

#     if sorted_var[mid_index] == element:
#         print(f"{element} found at index {mid_index}")
#         return
#     elif sorted_var[mid_index] < element:
#         return search(sorted_var[mid_index + 1:], element)
#     else:
#         return search(sorted_var[:mid_index], element)


# var = [2, 100, 9, 105, 10, 20, 15, 36, 55, 42]

# search(var,15)



# def search(var, element):
#     var.sort()
#     low = 0
#     high = len(var) - 1
#     for i in range(len(var)):
#         mid_index = (low + high) // 2
#         if var[mid_index] == element:
#             print(f"{element} found at index {mid_index}")
#             return
#         elif var[mid_index] < element:
#             low = mid_index + 1
#         else:
#             high = mid_index - 1

#     print("Element not found")


# var = [2, 100, 9, 105, 10, 20, 15, 36, 55, 42]

# search(var, 20)




# def search(var, element):
#     var.sort()
#     low = 0
#     high = len(var) - 1

#     while low <= high:
#         mid_index = (low + high) // 2
#         if var[mid_index] == element:
#             print(f"{element} found at index {mid_index}")
#             return
#         elif var[mid_index] < element:
#             low = mid_index + 1
#         else:
#             high = mid_index - 1
#     print("Element not found")


# var = [2, 100, 9, 105, 10, 20, 15, 36, 55, 42]
# search(var, 20)
     
     
# def search(var, target):

#     var.sort()

#     low = 0
#     high = len(var) - 1

#     while low <= high:

#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid

#         if arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1


# sort = [2, 100, 9, 105, 10, 20, 15, 36, 55, 42]

# print(search(sort, 20))

 # in this question where in list number add digits like 1+1+1 = 3 like this all list number we need 
 # in single digit number we need to print like where we adding 899 = 8+9+9 = 26the agai need to add 2+6= 8 when
 # where i can get single number of out of list number different different we need signle number output value
#var = [111, 501, 100, 515, 424, 899, 991, 605, 103, 1104]

# var = [111, 501, 100, 515, 424, 899, 991, 605, 103, 1104]

# list = []
# for num in var:
#     while num > 9:
#         total = 0
#         for digit in str(num):
#             total += int(digit)
#         num = total
#     list.append(num)
# print(list)


# using linkedlist to solve this problem

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def insert(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new_node
#     def digital_sum(self):
#         temp = self.head
#         while temp:
#             num = temp.data
#             while num > 9:
#                 total = 0
#                 for digit in str(num):
#                     total += int(digit)
#                 num = total
#             print(num)
#             temp = temp.next


# list = LinkedList()

# var = [111, 501, 100, 515, 424, 899, 991, 605, 103, 1104]
# for i in var:
#     list.insert(i)
# list.digital_sum()


 # i need t take a input of list pattern of input 1,2,3,4,5 and output i want [1,2,3,4,5]
 
 
 # Take input like: 1,2,3,4,5

# num = input("Enter numbers: ")
# num = list(map(int, num.split(",")))
# print(num)


# def Input():
#     num = input("Enter numbers: ")
#     num = list(map(int, num.split(",")))
#     return num

# output = list()
# print(output)
'''
*       *
* *   * *
    *
* *   * *
*       *

'''

# star = [
#     "*       *",
#     "* *   * *",
#     "    *",
#     "* *   * *",
#     "*       *"
# ]

# for line in star:
#     print(line)



# for i in range(5):
#     if i == 0 or i == 4:
#         print("*", end="")
#         for j in range(7):
#             print(" ", end="")
#         print("*")

#     elif i == 1 or i == 3:
#         print("*", end="")
#         print(" ", end="")
#         print("*", end="")
#         for j in range(3):
#             print(" ", end="")
#         print("*", end="")
#         print(" ", end="")
#         print("*")

#     else:
#         for j in range(4):
#             print(" ", end="")
      #   print("*")
      
'''
*       *
* *   * *
    *
* *   * *
*       *

'''
      

for i in range(5):
    for j in range(9):
        if i == 0 or i == 4:
            if j == 0 or j == 8:
                print("*", end="")
            else:
                print(" ", end="")
        elif i == 1 or i == 3:
            if j == 0 or j == 2 or j == 6 or j == 8:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            if j == 4:
                print("*", end="")
            else:
                print(" ", end="")
    print()
    
    




