# Author: Kaustav Ghosh
# 2336. Smallest Number in Infinite Set
# https://leetcode.com/problems/smallest-number-in-infinite-set/
# Min-heap + set tracking added-back numbers below current pointer

import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.current = 1          # smallest number not yet popped from the infinite set
        self.added_back = []      # min-heap of numbers added back
        self.added_back_set = set()  # for O(1) membership check

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.added_back and self.added_back[0] < self.current:
            val = heapq.heappop(self.added_back)
            self.added_back_set.remove(val)
            return val
        val = self.current
        self.current += 1
        return val

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.current and num not in self.added_back_set:
            heapq.heappush(self.added_back, num)
            self.added_back_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
