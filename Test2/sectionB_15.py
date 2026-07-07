'''15.Count the total number of nodes present in a binary tree.'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def create_elemts(self):
        self.root = Node(50)
        self.root.left = Node(30)
        self.root.right = Node(70)

    def count(self, node):
        if node == None:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)

tree1 = BinaryTree()
tree1.create_elemts()
print("Total Nodes:", tree1.count(tree1.root))