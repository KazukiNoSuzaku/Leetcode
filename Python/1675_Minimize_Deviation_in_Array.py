# Author: Kaustav Ghosh
# Problem: Minimize Deviation in Array
# Approach: Double every odd up front so each value is at its max; keep halving the current maximum via a max-heap, tracking the running minimum, until the max turns odd

import heapq

class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap = []
        low = float('inf')
        for x in nums:
            if x % 2:
                x *= 2  # bring odd numbers to their only reachable even form
            heap.append(-x)
            low = min(low, x)
        heapq.heapify(heap)

        best = float('inf')
        while True:
            high = -heapq.heappop(heap)
            best = min(best, high - low)
            if high % 2:      # cannot halve an odd max any further
                break
            high //= 2
            low = min(low, high)
            heapq.heappush(heap, -high)
        return best
