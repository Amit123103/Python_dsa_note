'''3. Given a stack of integers, display all the elements from top to bottom without changing the order of the stack.
'''

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def is_empty(self):
        return len(self.items)==0
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements from top to bottom: ", self.items[:: -1])

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.display()
