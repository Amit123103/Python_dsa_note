
# first creating first node first node  
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None  # reference value None 
# # this my second where i have to add my new node created
# class Linkedlist:
#     def __init__(self):
#         self.head = None
        
#     def insert_new(self, data ):
#         node1 = Node(data)
#         node1.ref = self.head
#         self.head = node1
        
#     # here i am inserting new node and between two nodes 
#     def insert_btw(self, data, prev):
#         node1 = Node(data)
#         node1.ref = prev.ref
#         prev.ref = node1
#     def insert_end(self, data):
#         node1 = Node(data)
#         node1.ref = None
        # node1.head = None(data)
        

#devlop a code find node using the data
# finding nodes 
# def find_node(self, data):
#     current = self.head
#     while current:  # while loop using 
#         if current.data == data:
#             print("value found")
#             return current   # here found data then going to while loop 
#         current = current.ref
#         print("value Not")
#     # Data not found
#     return None



# first creating first node
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None   # reference is None initially


# # this is my Linked List class
# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     # Insert new node at the beginning
#     def insert_new(self, data):
#         node1 = Node(data)
#         node1.ref = self.head
#         self.head = node1

#     # Insert a new node between two nodes
#     def insert_btw(self, data, prev):
#         node1 = Node(data)
#         node1.ref = prev.ref
#         prev.ref = node1

#     # Insert a new node at the end
#     def insert_end(self, data):

#         # Create a new node
#         node1 = Node(data)

#         # If the linked list is empty
#         if self.head is None:
#             self.head = node1
#             return

#         # Start from the first node
#         n = self.head

#         # Move to the last node
#         while n.ref is not None:
#             n = n.ref

#         # Connect the last node to the new node
#         n.ref = node1
        
        
        
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#     def insert_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         current = self.head
#         while current.ref is not None:
#             current = current.ref
#         current.ref = new_node
#     def search(self, key):
#         current = self.head
#         while current is not None:
#             if current.data == key:
#                 print("Value Found")
#                 return
#             current = current.ref
#         print("Value Not Found")
# # Create linked list
# ll = Linkedlist()
# ll.insert_end(10)
# ll.insert_end(20)
# ll.insert_end(30)
# ll.insert_end(40)
# ll.search(30)
# ll.search(100)


# ------------------- delteing node ---------------

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
class Linkedlist:
    def __init__(self):
        self.head = None
    # Insert at beginning
    def insert_new(self, data):
        node1 = Node(data)
        node1.ref = self.head
        self.head = node1
    # Insert after a given node
    def insert_btw(self, data, prev):
        node1 = Node(data)
        node1.ref = prev.ref
        prev.ref = node1
    # Insert at end
    def insert_end(self, data):
        node1 = Node(data)
        if self.head is None:
            self.head = node1
            return
        n = self.head
        while n.ref is not None:
            n = n.ref
        n.ref = node1
    # Delete a node by value
def delete_node(self, value):
    # Check if the linked list is empty
    if self.head is None:
        print("Linked List is Empty")
        return
    # If the value is in the first node
    if self.head.data == value:
        self.head = self.head.ref
        print("Node Deleted")
        return
    # Traverse the linked list
    current = self.head
    while current.ref is not None:
    # Check if the next node contains the value
        if current.ref.data == value:
            # Remove the node
            current.ref = current.ref.ref
            print("Node Deleted")
            return
        current = current.ref
    # Value not found
    print("Value Not Found")
    
    
    
   # delting last node 
def delete_last(self):
    # Linked list is empty
    if self.head:
        print("empty")
        return
    #  Only one node
    if self.head.ref:
        self.head = None
        return
    #  More than one node
    current = self.head
    # Move to the second last node
    while current.ref.ref:
        current = current.ref
    # Delete the last node
    current.ref = None