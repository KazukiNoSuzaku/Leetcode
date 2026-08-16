# Author: Kaustav Ghosh
# Problem: Stock Price Fluctuation
# Approach: Keep the authoritative price per timestamp in a dict and the latest timestamp for current(). For max/min use two heaps with lazy deletion: a heap top is valid only if its price still matches the dict, otherwise pop it

import heapq

class StockPrice(object):
    def __init__(self):
        self.prices = {}
        self.max_heap = []   # (-price, timestamp)
        self.min_heap = []   # (price, timestamp)
        self.latest = 0

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.prices[timestamp] = price
        self.latest = max(self.latest, timestamp)
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self):
        """
        :rtype: int
        """
        return self.prices[self.latest]

    def maximum(self):
        """
        :rtype: int
        """
        while self.prices[self.max_heap[0][1]] != -self.max_heap[0][0]:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]

    def minimum(self):
        """
        :rtype: int
        """
        while self.prices[self.min_heap[0][1]] != self.min_heap[0][0]:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]
