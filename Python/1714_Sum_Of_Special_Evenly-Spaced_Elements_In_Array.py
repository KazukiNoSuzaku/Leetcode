# Author: Kaustav Ghosh
# Problem: Sum Of Special Evenly-Spaced Elements In Array (Premium)
# Approach: Square-root decomposition — precompute suffix sums for every small stride y <= sqrt(n); large strides have few terms so just walk them directly

class Solution(object):
    def solve(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        block = max(1, int(n ** 0.5))

        # dp[y][x] = nums[x] + nums[x+y] + nums[x+2y] + ...  (only for y <= block)
        dp = [[0] * n for _ in range(block + 1)]
        for y in range(1, block + 1):
            for x in range(n - 1, -1, -1):
                dp[y][x] = nums[x]
                if x + y < n:
                    dp[y][x] = (dp[y][x] + dp[y][x + y]) % MOD

        res = []
        for x, y in queries:
            if y <= block:
                res.append(dp[y][x] % MOD)
            else:
                total = 0
                i = x
                while i < n:
                    total = (total + nums[i]) % MOD
                    i += y
                res.append(total)
        return res
