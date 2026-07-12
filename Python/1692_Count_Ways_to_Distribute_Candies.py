# Author: Kaustav Ghosh
# Problem: Count Ways to Distribute Candies (Premium)
# Approach: This counts partitions of n distinct candies into k non-empty unlabeled bags = Stirling numbers of the second kind, built with S(i,j) = j*S(i-1,j) + S(i-1,j-1)

class Solution(object):
    def waysToDistribute(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1  # S(0, 0) = 1
        for _ in range(1, n + 1):
            nxt = [0] * (k + 1)
            for j in range(1, k + 1):
                nxt[j] = (j * dp[j] + dp[j - 1]) % MOD
            dp = nxt
        return dp[k]
