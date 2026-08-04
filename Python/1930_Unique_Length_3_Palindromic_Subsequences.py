# Author: Kaustav Ghosh
# Problem: Unique Length-3 Palindromic Subsequences
# Approach: A length-3 palindrome is x?x. For each letter x, look between its first and last occurrence; the number of distinct characters in that span is the number of distinct palindromes with outer letter x. Sum over all 26 letters

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for c in set(s):
            first = s.index(c)
            last = s.rindex(c)
            if last - first >= 2:
                total += len(set(s[first + 1:last]))
        return total
