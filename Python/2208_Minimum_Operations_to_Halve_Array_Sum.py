# Author: Kaustav Ghosh
# 2208. Minimum Operations to Halve Array Sum
# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
# Difficulty: Medium
#
# Approach: Use a max-heap. Greedily halve the largest element each operation.
# Each halving reduces the total sum by half of the chosen element.
# Keep track of the total reduction and count operations until sum is halved.

import heapq

class Solution(object):
    def halveArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        target = total / 2.0

        # Python only has min-heap, negate values for max-heap
        heap = [-x for x in nums]
        heapq.heapify(heap)

        ops = 0
        reduced = 0.0

        while reduced < target:
            largest = -heapq.heappop(heap)
            half = largest / 2.0
            reduced += half
            heapq.heappush(heap, -half)
            ops += 1

        return ops
