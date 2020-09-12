
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.arrow = 0

    def append(self, item):
        self.data[self.arrow] = item
        self.arrow += 1
        if self.arrow == self.capacity:
            self.arrow = 0

    def get(self):
        return [value for value in self.data if value is not None]
