# Author: Kaustav Ghosh
# Problem: Stone Game V
# Approach: Interval DP with prefix sums; for each split take the smaller half's value plus its optimal sub-result, or both when halves tie

from functools import lru_cache

class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def total(i, j):
            return prefix[j + 1] - prefix[i]

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0
            best = 0
            for k in range(i, j):
                left = total(i, k)
                right = total(k + 1, j)
                if left < right:
                    best = max(best, left + dp(i, k))
                elif left > right:
                    best = max(best, right + dp(k + 1, j))
                else:
                    best = max(best, left + dp(i, k), right + dp(k + 1, j))
            return best

        return dp(0, n - 1)
