# Author: Kaustav Ghosh
# Problem: 1589 - Maximum Sum Obtained of Any Permutation
# Approach: Sort requests by frequency (difference array), sort nums, multiply

class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        freq = [0] * (n + 1)

        for l, r in requests:
            freq[l] += 1
            freq[r + 1] -= 1

        # prefix sum to get frequency per index
        for i in range(1, n):
            freq[i] += freq[i - 1]

        freq = sorted(freq[:n], reverse=True)
        nums.sort(reverse=True)

        result = sum(f * v for f, v in zip(freq, nums))
        return result % MOD
