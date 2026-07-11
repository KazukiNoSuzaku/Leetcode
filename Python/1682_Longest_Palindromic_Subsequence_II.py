# Author: Kaustav Ghosh
# Problem: Longest Palindromic Subsequence II (Premium)
# Approach: Interval DP carrying the last matched outer character; a "good" pair is added only when s[i]==s[j] and differs from the previously matched char, forcing even length with no equal neighbors

from functools import lru_cache

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        @lru_cache(maxsize=None)
        def dp(i, j, prev):
            if i >= j:
                return 0
            if s[i] == s[j] and s[i] != prev:
                return 2 + dp(i + 1, j - 1, s[i])
            return max(dp(i + 1, j, prev), dp(i, j - 1, prev))

        return dp(0, len(s) - 1, '')
