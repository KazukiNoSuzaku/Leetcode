# Count ways to tile 2xn board with dominoes and trominoes. Answer mod 10^9+7.

# Author: Kaustav Ghosh

class Solution(object):
    def numTilings(self, n):
        MOD = 10**9 + 7
        if n == 1: return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD
        return dp[n]
