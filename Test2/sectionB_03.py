'''3.Delete the node containing 30 from the linked list and display the updated
list.'''

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
    def delete(self, Contain):
        valu1 = self.head
        if valu1 and valu1.data == Contain:
            self.head = valu1.next
            return
        prev = None
        while valu1 and valu1.data != Contain:
            prev = valu1
            valu1 = valu1.next
        if valu1 is None:
            print("Nothing")
            return
        prev.next = valu1.next

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
list.insert(40)

print("Before Deletion:")
list.display()
list.delete(30)
print("After Deletion:")
list.display()