'''5.Create an empty stack and push the values 5, 10, 15, 20 into it. Display
the stack.'''

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
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