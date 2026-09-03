# Author: Kaustav Ghosh
# Problem: Maximum Product After K Increments
# Approach: To maximize a product under a fixed budget of +1 increments, always raise the current smallest element (balancing the values). Use a min-heap, apply k increments to the top, then multiply everything modulo 1e9+7

import heapq


class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        heap = nums[:]
        heapq.heapify(heap)
        for _ in range(k):
            smallest = heapq.heappop(heap)
            heapq.heappush(heap, smallest + 1)
        product = 1
        for x in heap:
            product = (product * x) % MOD
        return product
