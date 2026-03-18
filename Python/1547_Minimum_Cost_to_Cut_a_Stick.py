# Author: Kaustav Ghosh
# Problem: 1547 - Minimum Cost to Cut a Stick
# Approach: Interval DP on sorted cut positions

class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        cuts = sorted([0] + cuts + [n])
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]

        for length in range(2, m):
            for i in range(m - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])

        return dp[0][m - 1]
