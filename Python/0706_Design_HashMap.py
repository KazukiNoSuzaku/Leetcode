# Design a HashMap with put, get, and remove operations.

# Author: Kaustav Ghosh

class MyHashMap(object):
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[h]):
            if k == key:
                self.buckets[h][i] = (key, value)
                return
        self.buckets[h].append((key, value))

    def get(self, key):
        for k, v in self.buckets[self._hash(key)]:
            if k == key: return v
        return -1

    def remove(self, key):
        h = self._hash(key)
        self.buckets[h] = [(k, v) for k, v in self.buckets[h] if k != key]
