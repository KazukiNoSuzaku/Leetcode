# Count arrays of 1..n with exactly k inverse pairs. Answer mod 10^9+7.

# Author: Kaustav Ghosh

class Solution(object):
    def kInversePairs(self, n, k):
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(2, n + 1):
            new_dp = [0] * (k + 1)
            prefix = 0
            for j in range(k + 1):
                prefix += dp[j]
                if j >= i:
                    prefix -= dp[j - i]
                new_dp[j] = prefix % MOD
            dp = new_dp
        return dp[k]
