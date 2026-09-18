# Author: Kaustav Ghosh
# Problem: Find the K-Sum of an Array
# Approach: The largest subsequence sum takes every positive number. Any other subsequence equals that maximum minus a set of absolute values (dropping a positive or adding a negative), so the k-th largest sum is the maximum minus the (k-1)-th smallest subset sum of the sorted absolute values. A min-heap enumerates those subset sums in order: from a subset ending at index i, either append i + 1 or swap i for i + 1

import heapq


class Solution(object):
    def kSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        best = sum(x for x in nums if x > 0)
        vals = sorted(abs(x) for x in nums)
        heap = [(vals[0], 0)]
        removed = 0
        for _ in range(k - 1):
            removed, i = heapq.heappop(heap)
            if i + 1 < len(vals):
                heapq.heappush(heap, (removed + vals[i + 1], i + 1))
                heapq.heappush(heap, (removed - vals[i] + vals[i + 1], i + 1))
        return best - removed
