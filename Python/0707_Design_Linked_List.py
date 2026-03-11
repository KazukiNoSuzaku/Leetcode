# Design a singly linked list with get, addAtHead, addAtTail, addAtIndex, deleteAtIndex.

# Author: Kaustav Ghosh

class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index >= self.size: return -1
        cur = self.head
        for _ in range(index): cur = cur[1]
        return cur[0]

    def addAtHead(self, val):
        self.head = [val, self.head]
        self.size += 1

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index > self.size: return
        dummy = [0, self.head]
        cur = dummy
        for _ in range(index): cur = cur[1]
        cur[1] = [val, cur[1]]
        self.head = dummy[1]
        self.size += 1

    def deleteAtIndex(self, index):
        if index >= self.size: return
        dummy = [0, self.head]
        cur = dummy
        for _ in range(index): cur = cur[1]
        cur[1] = cur[1][1]
        self.head = dummy[1]
        self.size -= 1
