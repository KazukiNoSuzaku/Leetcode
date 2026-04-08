# Author: Kaustav Ghosh
# Problem: 2233. Maximum Product After K Increments
# URL: https://leetcode.com/problems/maximum-product-after-k-increments/
# Difficulty: Medium
#
# Approach:
# Use a min-heap. For each of the k increments, pop the smallest element,
# add 1, and push it back. After all increments, compute the product of
# all elements modulo 10^9 + 7.

import heapq

class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        heapq.heapify(nums)
        for _ in range(k):
            smallest = heapq.heappop(nums)
            heapq.heappush(nums, smallest + 1)
        result = 1
        for n in nums:
            result = (result * n) % MOD
        return result
