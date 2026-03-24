# Author: Kaustav Ghosh
# Problem 2034: Stock Price Fluctuation

import heapq

class StockPrice(object):
    def __init__(self):
        self.timestamps = {}
        self.latest_time = 0
        self.max_heap = []  # (-price, timestamp)
        self.min_heap = []  # (price, timestamp)

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.timestamps[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self):
        """
        :rtype: int
        """
        return self.timestamps[self.latest_time]

    def maximum(self):
        """
        :rtype: int
        """
        while True:
            neg_price, t = self.max_heap[0]
            if self.timestamps[t] == -neg_price:
                return -neg_price
            heapq.heappop(self.max_heap)

    def minimum(self):
        """
        :rtype: int
        """
        while True:
            price, t = self.min_heap[0]
            if self.timestamps[t] == price:
                return price
            heapq.heappop(self.min_heap)
