import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def __str__(self):
        return self.storage

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size ==0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        a = self.data

        a.enqueue(item)
        if len(self.data) == self.capacity:
            a.dequeue(item)
            

    def get(self):
        return self.data

c = RingBuffer(5)

c.append(10)
c.append(20)
print(c.get())