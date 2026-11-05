# Author: Kaustav Ghosh
# Problem: Finding MK Average
# Approach: The average is over the middle slice of the last m values once the k smallest and k largest are set aside, so what is needed is the sum of a rank range, not a sorted list. Two Fenwick trees indexed by value hold how many copies of each value are in the window and what they add up to, which makes inserting or evicting a value a logarithmic update and lets the sum of the k smallest be read by descending the count tree to the k-th value and then correcting for the ties that straddle the boundary. The largest k is the mirror image, and a deque tracks which value leaves when the window overflows, so every call is logarithmic in the value range rather than linear in m.

class MKAverage(object):

    LIMIT = 100001

    def __init__(self, m, k):
        """
        :type m: int
        :type k: int
        """
        from collections import deque

        self.m = m
        self.k = k
        self.window = deque()
        self.counts = [0] * (self.LIMIT + 1)
        self.sums = [0] * (self.LIMIT + 1)
        self.total = 0

    def _update(self, value, copies):
        self.total += value * copies
        index = value
        while index <= self.LIMIT:
            self.counts[index] += copies
            self.sums[index] += value * copies
            index += index & -index

    def _prefix(self, value):
        found = filled = 0
        index = value
        while index > 0:
            found += self.counts[index]
            filled += self.sums[index]
            index -= index & -index
        return found, filled

    def _sum_of_smallest(self, wanted):
        # Walk down the tree to the value at rank `wanted`, taking whole
        # buckets while they fit and part of the straddling one.
        node = 0
        taken = gathered = 0
        step = 1 << (self.LIMIT.bit_length() - 1)
        while step:
            nxt = node + step
            if nxt <= self.LIMIT and taken + self.counts[nxt] <= wanted:
                node = nxt
                taken += self.counts[node]
                gathered += self.sums[node]
            step >>= 1
        return gathered + (wanted - taken) * (node + 1)

    def addElement(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.window.append(num)
        self._update(num, 1)
        if len(self.window) > self.m:
            self._update(self.window.popleft(), -1)

    def calculateMKAverage(self):
        """
        :rtype: int
        """
        if len(self.window) < self.m:
            return -1
        smallest = self._sum_of_smallest(self.k)
        largest = self.total - self._sum_of_smallest(self.m - self.k)
        return (self.total - smallest - largest) // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
