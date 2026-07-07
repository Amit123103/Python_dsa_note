'''4.Count and display the total number of nodes in the linked list.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node1 = Node(data)
        if self.head is None:
            self.head = node1
            return
        valu1 = self.head
        while valu1.next:
            valu1 = valu1.next
        valu1.next = node1
    def count(self):
        valu1 = self.head
        total = 0
        while valu1:
            total = total + 1
            valu1 = valu1.next
        print("Total Nodes:", total)
    def display(self):
        valu1 = self.head
        while valu1:
            print(valu1.data, end=" ")
            valu1 = valu1.next
        print(" ")


list = LinkedList()
list.insert(10)
list.insert(20)
list.insert(30)
list.insert(40)
print("Linked List:")
list.display()
list.count()