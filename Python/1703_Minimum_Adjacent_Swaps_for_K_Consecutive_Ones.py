# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

class Solution(object):
    def minMoves(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Collect positions of 1s
        ones = [i for i, v in enumerate(nums) if v == 1]
        # Normalize: ones[i] - i removes gaps
        n = len(ones)
        # Sliding window of size k, minimize cost to move to median
        # prefix[i] = ones[0] + ... + ones[i-1] after normalization
        normalized = [ones[i] - i for i in range(n)]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + normalized[i]

        result = float('inf')
        for i in range(n - k + 1):
            mid = i + k // 2
            median = normalized[mid]
            # Cost = sum of |normalized[j] - median| for j in [i, i+k-1]
            left_cost = median * (mid - i) - (prefix[mid] - prefix[i])
            right_cost = (prefix[i + k] - prefix[mid + 1]) - median * (i + k - mid - 1)
            result = min(result, left_cost + right_cost)
        return result
