# Author: Kaustav Ghosh
# Problem: 1595 - Minimum Cost to Connect Two Groups of Points
# Approach: Bitmask DP on second group assignment

from functools import lru_cache

class Solution(object):
    def connectTwoGroups(self, cost):
        """
        :type cost: List[List[int]]
        :rtype: int
        """
        m = len(cost)
        n = len(cost[0])
        # Precompute min cost to connect each j in group2
        min_cost = [min(cost[i][j] for i in range(m)) for j in range(n)]

        @lru_cache(maxsize=None)
        def dp(i, mask):
            if i == m:
                # Cover all uncovered j in group2
                result = 0
                for j in range(n):
                    if not (mask >> j & 1):
                        result += min_cost[j]
                return result
            result = float('inf')
            for j in range(n):
                result = min(result, cost[i][j] + dp(i + 1, mask | (1 << j)))
            return result

        return dp(0, 0)
