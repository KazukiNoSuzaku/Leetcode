# Design a data structure to store the strings' count with the ability to return the strings
# with minimum and maximum counts. All operations inc, dec, getMaxKey, getMinKey should be O(1).

# Author: Kaustav Ghosh

class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = self.next = None

class AllOne(object):
    def __init__(self):
        self.head = Node(0)     # min sentinel
        self.tail = Node(float('inf'))  # max sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_node = {}

    def _insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        if key not in self.key_node:
            node = self.head
        else:
            node = self.key_node[key]
        count = node.count + 1
        if node.next.count != count:
            new_node = Node(count)
            self._insert_after(node, new_node)
        else:
            new_node = node.next
        new_node.keys.add(key)
        self.key_node[key] = new_node
        if key in node.keys:
            node.keys.discard(key)
            if not node.keys and node != self.head:
                self._remove(node)

    def dec(self, key):
        node = self.key_node[key]
        count = node.count - 1
        node.keys.discard(key)
        if count == 0:
            del self.key_node[key]
        else:
            if node.prev.count != count:
                new_node = Node(count)
                self._insert_after(node.prev, new_node)
            else:
                new_node = node.prev
            new_node.keys.add(key)
            self.key_node[key] = new_node
        if not node.keys:
            self._remove(node)

    def getMaxKey(self):
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ''

    def getMinKey(self):
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ''
