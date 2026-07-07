'''12.Display all the elements of the queue in FIFO order.'''


class Queue:
    def __init__(self):
        self.queue = []

    def insert_element(self, value):
        self.queue.append(value)
    def display(self):
        print("Queue Elements:")
        for i in self.queue:
            print(i, end=" ")
        print()

queue1 = Queue()
queue1.insert_element(10)
queue1.insert_element(20)
queue1.insert_element(30)
queue1.insert_element(40)
queue1.display()