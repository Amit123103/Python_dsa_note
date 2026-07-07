'''10.Remove one element from the front of the queue and display the updated
queue.'''

class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)
    def delete(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Removed Element:", self.queue.pop(0))
    def display(self):
        print("Queue:")
        for i in self.queue:
            print(i, end=" ")
        print()

queue1 = Queue()

queue1.insert(10)
queue1.insert(20)
queue1.insert(30)
queue1.insert(40)

print("Before Deletion:")
queue1.display()
queue1.delete()
print("After Deletion:")
queue1.display()