# Author: Kaustav Ghosh
# Problem 1866: Number of Ways to Rearrange Sticks With K Sticks Visible

class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        # Unsigned Stirling numbers of the first kind
        # dp[i][j] = ways to arrange i sticks with j visible
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                # Place tallest at front (visible) or not (hidden behind one of i-1 positions)
                dp[i][j] = (dp[i - 1][j - 1] + (i - 1) * dp[i - 1][j]) % MOD
        return dp[n][k]
