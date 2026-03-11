# Design a class to find the k-th largest element in a stream of integers.

# Author: Kaustav Ghosh

import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
