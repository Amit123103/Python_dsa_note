'''6.Pop one element from the stack and display the updated stack.'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is blank")
        else:
            print("Pop Element:", self.stack.pop())
    def display(self):
        print("Stack:")
        for i in range(len(self.stack) - 1, -1, -1):
            print(self.stack[i])

stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
print("Before Pop:")
stack.display()
stack.pop()
print("After Pop:")
stack.display()