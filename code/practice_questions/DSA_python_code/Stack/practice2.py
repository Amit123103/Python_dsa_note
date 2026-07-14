'''2. Given a stack containing **5, 10, 15, 20** (20 is on top), 
remove the top element and display the updated stack.'''

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
    
stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
removed = stack.pop()

print("Removed element:", removed)
print("Updated Stack:", stack.items)
print("Top element:", stack.peek())
