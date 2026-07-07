'''7.Display the top element of the stack without removing it.'''
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def top(self):
        if len(self.stack) == 0:
            print("Stack is blank")
        else:
            print("Top Element:", self.stack[-1])

    def display(self):
        print("Stack:")
        for i in range(len(self.stack) - 1, -1, -1):
            print(self.stack[i])

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
stack.display()
stack.top()