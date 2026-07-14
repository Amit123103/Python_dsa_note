'''1. Create an empty queue and perform the following operations:

   * Enqueue 10
   * Enqueue 20
   * Enqueue 30
   * Display the front element.
'''

class Queue:
    def __init__(self):
        self.items =[]
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
        return len(self.items)==0
# create a queue
queue = Queue()
# Enqueue elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front element: ", queue.front())