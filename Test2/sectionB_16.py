'''16.Find and display all the leaf nodes of a binary tree.'''

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

    def leafNodes(self, node):
        if node == None:
            return

        if node.left == None and node.right == None:
            print(node.data, end=" ")

        self.leafNodes(node.left)
        self.leafNodes(node.right)

tree1 = BinaryTree()

tree1.create_elemts()

print("Leaf Nodes:")
tree1.leafNodes(tree1.root)