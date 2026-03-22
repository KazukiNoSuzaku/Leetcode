# Author: Kaustav Ghosh

from sortedcontainers import SortedList

class MKAverage(object):
    def __init__(self, m, k):
        """
        :type m: int
        :type k: int
        """
        self.m = m
        self.k = k
        self.queue = []
        self.sorted_list = SortedList()
        self.total = 0

    def addElement(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.queue.append(num)
        self.sorted_list.add(num)
        self.total += num
        if len(self.queue) > self.m:
            old = self.queue[-self.m - 1]
            self.sorted_list.remove(old)
            self.total -= old

    def calculateMKAverage(self):
        """
        :rtype: int
        """
        if len(self.queue) < self.m:
            return -1
        # Remove smallest k and largest k
        bottom_sum = sum(self.sorted_list[i] for i in range(self.k))
        top_sum = sum(self.sorted_list[self.m - self.k + i] for i in range(self.k))
        return (self.total - bottom_sum - top_sum) // (self.m - 2 * self.k)
