'''9.Create a queue and insert the values 10, 20, 30, 40.'''

class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)
    def display(self):
        print("Queue:")
        for i in self.queue:
            print(i, end=" ")
        print()

queue = Queue()
queue.insert(10)
queue.insert(20)
queue.insert(30)
queue.insert(40)
queue.display()