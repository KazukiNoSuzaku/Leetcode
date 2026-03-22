# Author: Kaustav Ghosh

class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from math import gcd
        n = len(nums)
        memo = {}

        def dp(mask, op):
            if mask in memo:
                return memo[mask]
            res = 0
            for i in range(n):
                if mask & (1 << i):
                    continue
                for j in range(i + 1, n):
                    if mask & (1 << j):
                        continue
                    new_mask = mask | (1 << i) | (1 << j)
                    score = op * gcd(nums[i], nums[j]) + dp(new_mask, op + 1)
                    res = max(res, score)
            memo[mask] = res
            return res

        return dp(0, 1)
