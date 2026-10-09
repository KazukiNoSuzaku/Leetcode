# Author: Kaustav Ghosh
# Problem: Minimum Cost to Cut a Stick
# Approach: Sort the cut positions with the stick's two ends added, so any piece of the stick is a pair of those points. The cost of clearing the cuts strictly inside a piece is the piece's length plus the cost of the two halves made by whichever inside cut goes first, so fill a table over widening pieces and try every first cut

class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        points = sorted([0] + cuts + [n])
        size = len(points)
        dp = [[0] * size for _ in range(size)]
        for width in range(2, size):
            for i in range(size - width):
                j = i + width
                dp[i][j] = points[j] - points[i] + min(dp[i][k] + dp[k][j]
                                                       for k in range(i + 1, j))
        return dp[0][size - 1]
