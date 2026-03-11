# Design a circular queue with enQueue, deQueue, Front, Rear, isEmpty, isFull operations.

# Author: Kaustav Ghosh

class MyCircularQueue(object):
    def __init__(self, k):
        self.q = [0] * k
        self.head = 0
        self.tail = 0
        self.size = 0
        self.cap = k

    def enQueue(self, value):
        if self.isFull(): return False
        self.q[self.tail] = value
        self.tail = (self.tail + 1) % self.cap
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty(): return False
        self.head = (self.head + 1) % self.cap
        self.size -= 1
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.q[self.head]

    def Rear(self):
        return -1 if self.isEmpty() else self.q[(self.tail - 1) % self.cap]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.cap
