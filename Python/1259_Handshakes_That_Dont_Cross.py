# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Catalan number - dp[n] = sum(dp[i]*dp[n-2-i]) for i in range(0, n, 2)

class Solution(object):
    def numberOfWays(self, numPeople):
        """
        :type numPeople: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = numPeople
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(2, n + 1, 2):
            for j in range(0, i, 2):
                dp[i] = (dp[i] + dp[j] * dp[i - 2 - j]) % MOD
        return dp[n]
