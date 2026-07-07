'''2.Insert a new node containing 25 after the node containing 20.'''


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
    def insert_after(self, Contain, data):
        valu1 = self.head
        while valu1:
            if valu1.data == Contain:
                node1 = Node(data)
                node1.next = valu1.next
                valu1.next = node1
                return
            valu1 = valu1.next
        print("Nothing")
        
    def display(self):
        valu1 = self.head
        while valu1:
            print(valu1.data, end=" ")
            valu1 = valu1.next
        print("None")


list = LinkedList()
list.insert(10)
list.insert(20)
list.insert(30)
print("Before Insertion:")
list.display()
list.insert_after(20, 25)
print("After Insertion:")
list.display()