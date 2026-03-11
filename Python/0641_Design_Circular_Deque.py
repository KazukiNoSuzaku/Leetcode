# Design a circular double-ended queue supporting insertFront, insertLast, deleteFront, deleteLast.

# Author: Kaustav Ghosh

class MyCircularDeque(object):
    def __init__(self, k):
        self.q = [0] * k
        self.front = 0
        self.rear = 0
        self.size = 0
        self.cap = k

    def insertFront(self, value):
        if self.isFull(): return False
        self.front = (self.front - 1) % self.cap
        self.q[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull(): return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.cap
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty(): return False
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty(): return False
        self.rear = (self.rear - 1) % self.cap
        self.size -= 1
        return True

    def getFront(self):
        return -1 if self.isEmpty() else self.q[self.front]

    def getRear(self):
        return -1 if self.isEmpty() else self.q[(self.rear - 1) % self.cap]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.cap
