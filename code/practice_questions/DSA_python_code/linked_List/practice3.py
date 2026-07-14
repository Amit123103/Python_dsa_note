'''3. Given a linked list containing **8 → 16 → 24 → 32**, delete 
the node containing **24** and display the remaining elements.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node1 = Node(data)
        if self.head:
            link = self.head
            while link.next:
                link = link.next
            link.next = node1
        else:
            self.head = node1

    def delete(self, data):
        if self.head:
            if self.head.data == data:
                self.head = self.head.next
                return

            link = self.head
            while link.next:
                if link.next.data == data:
                    link.next = link.next.next
                    return
                link = link.next

    def display(self):
        if self.head:
            link = self.head
            while link:
                print(link.data, end=" - ")
                link = link.next
            print("None")
        else:
            print("Linked List is Empty")


value = LinkedList()

value.insert(8)
value.insert(16)
value.insert(24)
value.insert(32)

# Delete 24
value.delete(24)

value.display()