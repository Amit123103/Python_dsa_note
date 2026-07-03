'''1. Create an empty stack and perform the following operations:

   * Push 10
   * Push 20
   * Push 30
   * Display the top element.'''
   
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
        return len(self.items) == 0
# Create a stack
stack = Stack()
# Push elements
stack.push(10)
stack.push(20)
stack.push(30)
# Display top element
print("Top element: ",stack.peek())
