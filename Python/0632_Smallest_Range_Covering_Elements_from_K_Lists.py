# Find the smallest range that includes at least one number from each of k sorted lists.

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def smallestRange(self, nums):
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)
        max_val = max(row[0] for row in nums)
        res = [float('-inf'), float('inf')]
        while heap:
            min_val, i, j = heapq.heappop(heap)
            if max_val - min_val < res[1] - res[0]:
                res = [min_val, max_val]
            if j + 1 == len(nums[i]):
                break
            next_val = nums[i][j + 1]
            heapq.heappush(heap, (next_val, i, j + 1))
            max_val = max(max_val, next_val)
        return res
