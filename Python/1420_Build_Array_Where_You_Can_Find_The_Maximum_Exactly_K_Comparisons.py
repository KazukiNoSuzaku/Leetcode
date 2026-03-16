# Author: Kaustav Ghosh
# Problem: Build Array Where You Can Find The Maximum Exactly K Comparisons (Premium)
# Approach: 3D DP: position, search cost, current max value

class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        # dp[i][j][max_val] = ways to fill i positions with j search cost and max value = max_val
        dp = [[[0] * (m + 1) for _ in range(k + 1)] for _ in range(n + 1)]

        for val in range(1, m + 1):
            dp[1][1][val] = 1

        for i in range(2, n + 1):
            for j in range(1, k + 1):
                for mx in range(1, m + 1):
                    # Place any value 1..mx at position i (doesn't increase search cost)
                    dp[i][j][mx] = (dp[i][j][mx] + dp[i - 1][j][mx] * mx) % MOD
                    # Place value mx at position i (increases search cost)
                    for prev_mx in range(1, mx):
                        dp[i][j][mx] = (dp[i][j][mx] + dp[i - 1][j - 1][prev_mx]) % MOD

        result = 0
        for mx in range(1, m + 1):
            result = (result + dp[n][k][mx]) % MOD
        return result
