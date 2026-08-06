# Author: Kaustav Ghosh
# Problem: Maximum Number of Points with Cost
# Approach: DP row by row where dp[c] is the best total ending at column c. Moving to the next row subtracts |c-j|; instead of an O(n^2) scan, compute left-to-right and right-to-left running maxima that fold the column distance penalty, giving O(m*n)

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points[0])
        dp = points[0][:]
        for r in range(1, len(points)):
            left = [0] * n
            right = [0] * n
            left[0] = dp[0]
            for j in range(1, n):
                left[j] = max(dp[j], left[j - 1] - 1)
            right[n - 1] = dp[n - 1]
            for j in range(n - 2, -1, -1):
                right[j] = max(dp[j], right[j + 1] - 1)
            dp = [points[r][j] + max(left[j], right[j]) for j in range(n)]
        return max(dp)
