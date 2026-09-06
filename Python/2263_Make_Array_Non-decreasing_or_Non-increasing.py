# Author: Kaustav Ghosh
# Problem: Make Array Non-decreasing or Non-increasing
# Approach: The minimum +/-1 cost to make an array non-decreasing is a classic slope-trick: sweep with a max-heap, and whenever the current element is below the running max, pay the gap and lower that max to the current value. Apply this both to the array and to its reverse (for non-increasing) and take the smaller total

import heapq


class Solution(object):
    def convertArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def cost_non_decreasing(arr):
            heap = []  # max-heap via negation
            cost = 0
            for x in arr:
                heapq.heappush(heap, -x)
                if -heap[0] > x:
                    cost += -heap[0] - x
                    heapq.heappop(heap)
                    heapq.heappush(heap, -x)
            return cost

        return min(cost_non_decreasing(nums), cost_non_decreasing(nums[::-1]))
