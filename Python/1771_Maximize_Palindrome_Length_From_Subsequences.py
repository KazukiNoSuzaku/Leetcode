# Author: Kaustav Ghosh
# Problem: Maximize Palindrome Length From Subsequences
# Approach: Run longest-palindromic-subsequence DP on word1+word2, but only count answers whose matched pair straddles the join, guaranteeing both parts are non-empty

class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        s = word1 + word2
        n = len(s)
        split = len(word1)

        dp = [[0] * n for _ in range(n)]
        best = 0
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    # valid only if this pair spans the two words
                    if i < split <= j:
                        best = max(best, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return best
