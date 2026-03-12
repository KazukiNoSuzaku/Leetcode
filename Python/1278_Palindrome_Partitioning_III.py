# Author: Kaustav Ghosh
# DP: cost to change s[i..j] to palindrome + partition into k groups

class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        # cost[i][j] = min changes to make s[i..j] a palindrome
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + (0 if s[i] == s[j] else 1)

        # dp[i][j] = min changes to partition s[0..i] into j palindromes
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][1] = cost[0][i]
            for j in range(2, min(i + 2, k + 1)):
                for m in range(j - 1, i + 1):
                    dp[i][j] = min(dp[i][j], dp[m - 1][j - 1] + cost[m][i])
        return dp[n - 1][k]
