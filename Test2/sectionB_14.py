'''14.Perform an Inorder Traversal on a binary tree.'''
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

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

tree = BinaryTree()
tree.create_tree()
print("Inorder Traversal:")
tree.inorder(tree.root)