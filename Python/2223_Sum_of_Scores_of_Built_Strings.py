# Author: Kaustav Ghosh
# Problem: 2223. Sum of Scores of Built Strings
# URL: https://leetcode.com/problems/sum-of-scores-of-built-strings/
# Difficulty: Hard
#
# Approach:
# Use the Z-function. For a string s, Z[i] is the length of the longest
# substring starting at i that matches a prefix of s. The answer is the
# length of s (score for s itself) plus the sum of all Z[i] values.

class Solution(object):
    def sumScores(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        z = [0] * n
        z[0] = n
        l, r = 0, 0
        for i in range(1, n):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] > r:
                l, r = i, i + z[i]
        return sum(z)
