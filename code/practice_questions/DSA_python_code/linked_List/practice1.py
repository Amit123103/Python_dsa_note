'''1. Create a linked list with the values **10, 20, 30, 40, 50**. Display all the elements from the beginning to the end.
'''
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class linkedList:
#     def __init__(self):
#         self.head = None
#     def insert_end(self, data):
#         new_node = Node(data)
#         if self.head:
#             current_value = self.head
#             while current-value.ref:
#                 current_value = current_value.ref
#             current_value.ref = new_node
#         else:
#             self.head = new_node
            
#     def display(self):
#         if self.head:
#             current_value = self.head
#             while current_value:
#                 print(current_value.data, end=":")
#                 current_value = current_value.ref
    

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def display(self):
        if self.head is None:
            print("Linked List blank")
            return
        temp = self.head
        while temp:
            print(temp.data, end=", ")
            temp = temp.next
        print("None")
value = LinkedList()
value.insert(10)
value.insert(20)
value.insert(30)
value.insert(40)
value.insert(50)
# Display elements
print("Linked List:")
value.display()