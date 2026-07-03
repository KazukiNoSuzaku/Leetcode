# Author: Kaustav Ghosh
# Problem: Minimum Cost to Connect Two Groups of Points
# Approach: DP over group-1 points with a bitmask of covered group-2 points; each group-1 point picks one edge, leftover group-2 points take their cheapest edge

class Solution(object):
    def connectTwoGroups(self, cost):
        """
        :type cost: List[List[int]]
        :rtype: int
        """
        from functools import lru_cache

        m, n = len(cost), len(cost[0])
        # Cheapest way to cover each group-2 point (used once group-1 is exhausted)
        min2 = [min(cost[i][j] for i in range(m)) for j in range(n)]

        @lru_cache(maxsize=None)
        def dp(i, mask):
            if i == m:
                return sum(min2[j] for j in range(n) if not (mask >> j) & 1)
            best = float('inf')
            for j in range(n):
                best = min(best, cost[i][j] + dp(i + 1, mask | (1 << j)))
            return best

        return dp(0, 0)
