# Author: Kaustav Ghosh
# Problem: Count Substrings That Differ by One Character
# Approach: Instead of enumerating substring pairs and comparing them, I anchor on the single position where they disagree: for every pair of positions whose characters differ, any qualifying pair of substrings must straddle that spot with identical characters on both sides. So the number of pairs contributed by that spot is the number of ways to extend left, which is one more than the length of the common suffix ending just before it, times the number of ways to extend right, which is one more than the length of the common prefix starting just after it. Both of those are filled in by two small tables in one pass each, making the whole count quadratic rather than cubic.

class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n, m = len(s), len(t)
        # suffix[i][j]: length of the common suffix of s[:i] and t[:j]
        suffix = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    suffix[i][j] = suffix[i - 1][j - 1] + 1
        # prefix[i][j]: length of the common prefix of s[i:] and t[j:]
        prefix = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    prefix[i][j] = prefix[i + 1][j + 1] + 1

        total = 0
        for i in range(n):
            for j in range(m):
                if s[i] != t[j]:
                    total += (suffix[i][j] + 1) * (prefix[i + 1][j + 1] + 1)
        return total
