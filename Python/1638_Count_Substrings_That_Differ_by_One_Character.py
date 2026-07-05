# Author: Kaustav Ghosh
# Problem: Count Substrings That Differ by One Character
# Approach: At every mismatch position (i,j), it can be the sole difference; the count it contributes is (matching run to its left + 1) * (matching run to its right + 1)

class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)

        # left[i][j]: length of equal run ending just before s[i], t[j]
        left = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    left[i][j] = left[i - 1][j - 1] + 1

        # right[i][j]: length of equal run starting at s[i], t[j]
        right = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    right[i][j] = right[i + 1][j + 1] + 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    ans += (left[i][j] + 1) * (right[i + 1][j + 1] + 1)
        return ans
