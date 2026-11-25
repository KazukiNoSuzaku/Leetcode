# Author: Kaustav Ghosh
# Problem: Stock Price Fluctuation
# Approach: Corrections mean a timestamp's price can change after the fact, so the authoritative record is a map from timestamp to its current price, and the latest timestamp seen answers the current-price query directly. The extremes cannot be maintained by simply tracking a running best, because a correction can invalidate it, so two heaps hold every price ever recorded alongside its timestamp and stale entries are discarded lazily: the top of a heap is popped while its price disagrees with what the map now says for that timestamp. Each recorded price is pushed once and discarded at most once, so the discarding costs nothing overall.

import heapq


class StockPrice(object):

    def __init__(self):
        self.prices = {}
        self.latest = 0
        self.lowest = []
        self.highest = []

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.prices[timestamp] = price
        if timestamp > self.latest:
            self.latest = timestamp
        heapq.heappush(self.lowest, (price, timestamp))
        heapq.heappush(self.highest, (-price, timestamp))

    def current(self):
        """
        :rtype: int
        """
        return self.prices[self.latest]

    def maximum(self):
        """
        :rtype: int
        """
        while -self.highest[0][0] != self.prices[self.highest[0][1]]:
            heapq.heappop(self.highest)
        return -self.highest[0][0]

    def minimum(self):
        """
        :rtype: int
        """
        while self.lowest[0][0] != self.prices[self.lowest[0][1]]:
            heapq.heappop(self.lowest)
        return self.lowest[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
