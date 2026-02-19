# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
# An interleaving of two strings s and t is a configuration where s and t are divided into
# n and m substrings respectively such that s3 = s1' + t1' + s2' + t2' + ...

# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

# Example 2:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false

# Example 3:
# Input: s1 = "", s2 = "", s3 = ""
# Output: true

# Constraints:
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.

# Author: Kaustav Ghosh

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                            (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[m][n]
