from math import isqrt

class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        # For each sorted number, extend the chain from its integer square root if present.
        num_set = set(nums)
        dp = {}
        for x in sorted(nums):
            s = isqrt(x)
            dp[x] = dp.get(s, 1) + 1 if s * s == x and s in num_set else 1
        ans = max(dp.values())
        return ans if ans >= 2 else -1
