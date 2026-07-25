# Author: Kaustav Ghosh
# Problem: Finding MK Average
# Approach: Keep the last m values in a queue and partition them across three SortedLists (smallest k, middle, largest k) with a running middle sum; each add/erase then rebalances by shifting at most a couple of boundary elements

from collections import deque
from sortedcontainers import SortedList

class MKAverage(object):
    def __init__(self, m, k):
        """
        :type m: int
        :type k: int
        """
        self.m = m
        self.k = k
        self.queue = deque()
        self.low = SortedList()   # k smallest
        self.mid = SortedList()   # middle m - 2k
        self.high = SortedList()  # k largest
        self.mid_sum = 0

    def addElement(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.queue.append(num)
        self._insert(num)
        if len(self.queue) > self.m:
            self._erase(self.queue.popleft())

    def _insert(self, num):
        if self.low and num < self.low[-1]:
            self.low.add(num)
        elif self.high and num > self.high[0]:
            self.high.add(num)
        else:
            self.mid.add(num)
            self.mid_sum += num
        self._rebalance()

    def _erase(self, num):
        if self.low and num <= self.low[-1]:
            self.low.remove(num)
        elif self.high and num >= self.high[0]:
            self.high.remove(num)
        else:
            self.mid.remove(num)
            self.mid_sum -= num
        self._rebalance()

    def _rebalance(self):
        if len(self.low) + len(self.mid) + len(self.high) < self.m:
            return
        # low must hold exactly k smallest
        while len(self.low) < self.k:
            x = self.mid.pop(0)
            self.mid_sum -= x
            self.low.add(x)
        while len(self.low) > self.k:
            x = self.low.pop()
            self.mid.add(x)
            self.mid_sum += x
        # high must hold exactly k largest
        while len(self.high) < self.k:
            x = self.mid.pop()
            self.mid_sum -= x
            self.high.add(x)
        while len(self.high) > self.k:
            x = self.high.pop(0)
            self.mid.add(x)
            self.mid_sum += x

    def calculateMKAverage(self):
        """
        :rtype: int
        """
        if len(self.queue) < self.m:
            return -1
        return self.mid_sum // len(self.mid)
