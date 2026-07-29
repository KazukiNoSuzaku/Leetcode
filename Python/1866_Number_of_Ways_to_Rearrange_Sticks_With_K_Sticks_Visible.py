# Author: Kaustav Ghosh
# Problem: Number of Ways to Rearrange Sticks With K Sticks Visible
# Approach: These are unsigned Stirling numbers of the first kind. Placing the tallest stick either makes it visible at the front (dp[n-1][k-1]) or hides it among the other n-1 positions (dp[n-1][k] * (n-1))

class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        # dp[j] over rows i: ways for i sticks with j visible
        dp = [0] * (k + 1)
        dp[0] = 1  # zero sticks, zero visible
        for i in range(1, n + 1):
            nxt = [0] * (k + 1)
            for j in range(1, min(i, k) + 1):
                nxt[j] = (dp[j - 1] + dp[j] * (i - 1)) % MOD
            dp = nxt
        return dp[k]
