# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Min-heap, always merge two smallest sticks

import heapq

class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heapq.heapify(sticks)
        total = 0
        while len(sticks) > 1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            cost = a + b
            total += cost
            heapq.heappush(sticks, cost)
        return total
