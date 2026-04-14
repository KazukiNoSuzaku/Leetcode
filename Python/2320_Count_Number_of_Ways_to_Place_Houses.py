# Author: Kaustav Ghosh
# 2320. Count Number of Ways to Place Houses
# DP on one side of the street squared (two sides are independent)

class Solution(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        # For one side: dp where no two adjacent plots have houses
        # Let dp0 = ways ending with no house, dp1 = ways ending with house
        dp0, dp1 = 1, 1  # base case: 1 plot

        for _ in range(n - 1):
            dp0, dp1 = dp0 + dp1, dp0

        one_side = (dp0 + dp1) % MOD

        # Two sides are independent, so multiply
        return (one_side * one_side) % MOD
