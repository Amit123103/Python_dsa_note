'''13.Create the following binary tree:
```
50
/ \
30 70
```
Display the root, left child, and right child.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def create_tree(self):
        self.root = Node(50)
        self.root.left = Node(30)
        self.root.right = Node(70)

    def display(self):
        print("Root:", self.root.data)
        print("Left Child:", self.root.left.data)
        print("Right Child:", self.root.right.data)

tree1 = BinaryTree()
tree1.create_tree()
tree1.display()