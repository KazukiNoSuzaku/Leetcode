# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Maintain sorted set of non-full stack indices with heap

import heapq

class DinnerPlates(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.stacks = []
        self.available = []  # min-heap of indices with space

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        while self.available and self.available[0] < len(self.stacks) and len(self.stacks[self.available[0]]) == self.cap:
            heapq.heappop(self.available)
        if not self.available or self.available[0] >= len(self.stacks):
            self.stacks.append([])
            heapq.heappush(self.available, len(self.stacks) - 1)
        idx = self.available[0]
        self.stacks[idx].append(val)
        if len(self.stacks[idx]) == self.cap:
            heapq.heappop(self.available)

    def pop(self):
        """
        :rtype: int
        """
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return -1
        val = self.stacks[-1].pop()
        heapq.heappush(self.available, len(self.stacks) - 1)
        return val

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        heapq.heappush(self.available, index)
        return self.stacks[index].pop()
