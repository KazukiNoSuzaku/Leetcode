# Design a map with insert and sum operations where sum returns total for all keys with given prefix.

# Author: Kaustav Ghosh

class MapSum(object):
    def __init__(self):
        self.data = {}

    def insert(self, key, val):
        self.data[key] = val

    def sum(self, prefix):
        return sum(v for k, v in self.data.items() if k.startswith(prefix))
