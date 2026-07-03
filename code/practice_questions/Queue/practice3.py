'''3. Given a queue of integers, display all the elements in the order they will be removed from the queue.'''

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    def front(self):
        if self.is_empty():
            return None
        return self.items[0]
    def is_empty(self):
        return len(self.items) ==0
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements in order of removal: ", self.items)
            
queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)
removed = queue.dequeue()
queue.display()
print("removed element: ", removed)