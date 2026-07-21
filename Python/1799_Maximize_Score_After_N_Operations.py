# Author: Kaustav Ghosh
# Problem: Maximize Score After N Operations
# Approach: Bitmask DP over which numbers are still available; the operation index is (used bits)//2, and each pair of chosen indices scores that operation number times their gcd

from math import gcd
from functools import lru_cache

class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)

        @lru_cache(maxsize=None)
        def dp(mask):
            used = bin(mask).count('1')
            if used == size:
                return 0
            op = used // 2 + 1
            best = 0
            for i in range(size):
                if mask >> i & 1:
                    continue
                for j in range(i + 1, size):
                    if mask >> j & 1:
                        continue
                    taken = mask | (1 << i) | (1 << j)
                    best = max(best, op * gcd(nums[i], nums[j]) + dp(taken))
            return best

        return dp(0)
