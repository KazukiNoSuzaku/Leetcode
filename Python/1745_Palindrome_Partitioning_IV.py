# Author: Kaustav Ghosh
# Problem: Palindrome Partitioning IV
# Approach: Splitting into exactly three palindromes means choosing two cut points, so the cost of the search is quadratic and the only thing that must not be quadratic per test is deciding whether a stretch is a palindrome. That is settled once up front by the standard table built over increasing lengths, where a stretch is a palindrome when its ends agree and the stretch inside them is one. Holding that table as byte arrays rather than lists of Python objects keeps four million entries to a few megabytes. The search then fixes the first cut only where the opening stretch is already a palindrome, which skips most of the second loop outright.

class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        palindrome = [bytearray(n) for _ in range(n)]
        for i in range(n):
            palindrome[i][i] = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                palindrome[i][i + 1] = 1
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and palindrome[i + 1][j - 1]:
                    palindrome[i][j] = 1

        first = palindrome[0]
        last_row = n - 1
        for i in range(1, n - 1):
            if not first[i - 1]:
                continue
            middle = palindrome[i]
            for j in range(i, n - 1):
                if middle[j] and palindrome[j + 1][last_row]:
                    return True
        return False
