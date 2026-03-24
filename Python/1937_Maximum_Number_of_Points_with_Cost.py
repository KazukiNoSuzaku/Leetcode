# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m, n = len(points), len(points[0])
        dp = list(points[0])
        for i in range(1, m):
            # Left pass: left[j] = max(dp[k] + k) - j + points[i][j] for k <= j
            left = [0] * n
            left[0] = dp[0]
            for j in range(1, n):
                left[j] = max(left[j - 1], dp[j] + j)
            # Right pass: right[j] = max(dp[k] - k) + j + points[i][j] for k >= j
            right = [0] * n
            right[n - 1] = dp[n - 1] - (n - 1)
            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1], dp[j] - j)
            new_dp = [0] * n
            for j in range(n):
                new_dp[j] = max(left[j] - j, right[j] + j) + points[i][j]
            dp = new_dp
        return max(dp)
