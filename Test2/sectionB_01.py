'''Section B – Coding Questions (20 × 2 = 40 Marks)
1.Create a linked list containing the values 10, 20, 30, 40, 50 and display
all the elements.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        node1 = Node(data)
        if not self.head:
            self.head = node1
            return
        valu1 = self.head
        while valu1.next:
            valu1 = valu1.next
        valu1.next = node1

    def display(self):
        valu1 = self.head
        while valu1:
            print(valu1.data, end=" ")
            valu1 = valu1.next
        print() 

list = LinkedList() 
for i in [10, 20, 30, 40, 50]:
    list.append(i)
list.display()
