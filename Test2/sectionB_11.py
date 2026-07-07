'''11.Display the front element of the queue without removing it.'''

class Queue:
    def __init__(self):
        self.queue = []

    def insert_elemts(self, value):
        self.queue.append(value)
    def front_element(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Front element:", self.queue[0])
    def display(self):
        print("Queue:")
        for i in self.queue:
            print(i, end=" ")
        print()

queue1 = Queue()
queue1.insert_elemts(10)
queue1.insert_elemts(20)
queue1.insert_elemts(30)
queue1.insert_elemts(40)
queue1.display()
queue1.front_element()