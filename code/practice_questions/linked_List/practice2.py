'''2. Given a linked list containing **5 → 10 → 15 → 20**, insert the value **12** after **10** and 
display the updated linked list.
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
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node1
        else:
            self.head = node1
    def insert_after(self, data, after):
        node1 = Node(data)
        temp = self.head
        while temp:
            if temp.data == after:
                node1.next = temp.next
                temp.next = node1
                return
            temp = temp.next
    def display(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.data, end=" - ")
                temp = temp.next
            print("None")
        else:
            print("Linked List have nothing")

value = LinkedList()
value.insert(5)
value.insert(10)
value.insert(15)
value.insert(20)
# inserting after 10
value.insert_after(12, 10)
value.display()

    