# Author: Kaustav Ghosh
# Problem: Design Most Recently Used Queue
# Approach: Removing from the middle of a list and appending is linear per fetch, which the follow-up asks to improve on, so the queue is instead laid out across a wider slot array with room for every append, and a Fenwick tree records which slots are still occupied. Finding the k-th element then becomes descending that tree for the earliest slot whose running occupancy reaches k, which is logarithmic rather than a scan, and the move itself is two updates: clear the old slot and occupy the next free slot past the tail. Nothing is ever shifted, so the order is carried entirely by slot position.

class MRUQueue(object):

    def __init__(self, n):
        """
        :type n: int
        """
        # Room for the initial elements plus one appended slot per fetch.
        self.capacity = n + 2000
        self.tree = [0] * (self.capacity + 1)
        self.values = [0] * (self.capacity + 1)
        for slot in range(1, n + 1):
            self.values[slot] = slot
            self._occupy(slot, 1)
        self.tail = n

    def _occupy(self, slot, delta):
        while slot <= self.capacity:
            self.tree[slot] += delta
            slot += slot & -slot

    def _slot_of(self, k):
        # Earliest slot whose running occupancy reaches k.
        at = 0
        step = 1 << self.capacity.bit_length()
        while step:
            nxt = at + step
            if nxt <= self.capacity and self.tree[nxt] < k:
                at = nxt
                k -= self.tree[nxt]
            step >>= 1
        return at + 1

    def fetch(self, k):
        """
        :type k: int
        :rtype: int
        """
        slot = self._slot_of(k)
        value = self.values[slot]
        self._occupy(slot, -1)
        self.tail += 1
        self.values[self.tail] = value
        self._occupy(self.tail, 1)
        return value


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
