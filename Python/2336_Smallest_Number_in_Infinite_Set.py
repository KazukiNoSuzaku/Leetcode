# Author: Kaustav Ghosh
# Problem: Smallest Number in Infinite Set
# Approach: Keep a pointer nxt such that every number >= nxt is still in the set, plus a min-heap (with a companion set for membership) of numbers below nxt that were added back. popSmallest takes from the heap when it is non-empty, since those are all below nxt, otherwise returns nxt and advances it; addBack only records a number below nxt that is not already in the heap

import heapq


class SmallestInfiniteSet(object):

    def __init__(self):
        self.nxt = 1
        self.heap = []
        self.added = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.heap:
            num = heapq.heappop(self.heap)
            self.added.remove(num)
            return num
        self.nxt += 1
        return self.nxt - 1

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.nxt and num not in self.added:
            self.added.add(num)
            heapq.heappush(self.heap, num)
