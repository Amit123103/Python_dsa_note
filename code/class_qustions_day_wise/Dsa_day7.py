
# first creating first node first node  
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None  # reference value None 
# this my second where i have to add my new node created
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_new(self, data ):
        node1 = Node(data)
        node1.ref = self.head
        self.head = node1
        
    # here i am inserting new node and between two nodes 
    def insert_btw(self, data, prev):
        node1 = Node(data)
        node1.ref = prev.ref
        prev.ref = node1
    def insert_end(self, data):
        node1 = Node(data)
        node1.ref = None
        # node1.head = None(data)
        