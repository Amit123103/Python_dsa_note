'''8.Check whether a stack is empty and display an appropriate message.'''

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def Empty(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")
            
            
stack = Stack()
stack.Empty()
stack.push(10)
stack.push(20)
stack.Empty()



