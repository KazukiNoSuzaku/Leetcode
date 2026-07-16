# Author: Kaustav Ghosh
# Problem: Palindrome Partitioning IV
# Approach: Precompute pal[i][j] for every substring with the expand-from-inside recurrence, then try all two-cut positions splitting s into three palindromes

class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        for i in range(1, n - 1):        # first piece is s[0:i]
            if not pal[0][i - 1]:
                continue
            for j in range(i, n - 1):    # second piece is s[i:j+1]
                if pal[i][j] and pal[j + 1][n - 1]:
                    return True
        return False
