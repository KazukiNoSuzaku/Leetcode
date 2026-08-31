# Author: Kaustav Ghosh
# Problem: Minimum Operations to Halve Array Sum
# Approach: Each halving removes an amount equal to half the chosen value from the sum, so the greedy choice is always to halve the current largest value (it yields the biggest reduction). Use a max-heap, repeatedly halving the top until the accumulated reduction reaches half the original sum

import heapq


class Solution(object):
    def halveArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = sum(nums) / 2.0
        heap = [-float(x) for x in nums]
        heapq.heapify(heap)
        reduced = 0.0
        ops = 0
        while reduced < target:
            largest = -heapq.heappop(heap)
            half = largest / 2.0
            reduced += half
            heapq.heappush(heap, -half)
            ops += 1
        return ops
