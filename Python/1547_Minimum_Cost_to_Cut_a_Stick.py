# Author: Kaustav Ghosh
# Problem: Minimum Cost to Cut a Stick
# Approach: Interval DP over sorted cut positions (with 0 and n as boundaries); dp[i][j] = min cost to make every cut strictly between cuts[i] and cuts[j]

class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        points = [0] + sorted(cuts) + [n]
        m = len(points)
        dp = [[0] * m for _ in range(m)]
        # length = gap between the two boundary indices we are solving for
        for length in range(2, m):
            for i in range(m - length):
                j = i + length
                best = float('inf')
                for k in range(i + 1, j):
                    best = min(best, dp[i][k] + dp[k][j] + points[j] - points[i])
                dp[i][j] = best
        return dp[0][m - 1]
