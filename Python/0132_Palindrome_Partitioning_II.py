# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

# Example 2:
# Input: s = "a"
# Output: 0

# Example 3:
# Input: s = "ab"
# Output: 1

# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase English letters only.

# Author: Kaustav Ghosh

class Solution(object):
    def minCut(self, s):
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i+1][j-1]):
                    is_pal[i][j] = True

        dp = list(range(-1, n))
        for i in range(1, n):
            for j in range(i + 1):
                if is_pal[j][i]:
                    dp[i + 1] = min(dp[i + 1], dp[j] + 1)
        return dp[n]
