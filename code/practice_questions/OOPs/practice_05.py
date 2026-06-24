'''5. Binary Search Tree Class

Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
Left Side  < Root
Right Side > Root

Example:

      10
     /  \
    5   20
5 is less than 10 → goes left

'''
class Node:

    def __init__(self, data,left, right):
        self.data = data
        self.left = left
        self.right = right


root = Node(10, Node(5,None, None), Node(20,None, None))  

# root.left = 
# root.right = 

print(root.data)
print(root.left.data)
print(root.right.data)


