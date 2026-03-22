# Author: Kaustav Ghosh

class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        s = word1 + word2
        n = len(s)
        m = len(word1)
        # Longest palindromic subsequence DP
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        res = 0
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    # Check if one char from word1 and one from word2
                    if i < m and j >= m:
                        res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return res
