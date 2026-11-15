# Author: Kaustav Ghosh
# Problem: Unique Length-3 Palindromic Subsequences
# Approach: Such a palindrome is fixed by its outer letter and its middle letter, so there are at most twenty-six times twenty-six of them and the count is over those pairs rather than over subsequences. For a chosen outer letter the widest possible span is between its first and last occurrence, and any middle letter appearing anywhere strictly inside that span can be used, so the distinct letters in that slice are exactly the middles that work. Twenty-six first and last lookups plus twenty-six passes over the slices settle it in linear time per letter.

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for code in range(26):
            letter = chr(97 + code)
            first = s.find(letter)
            if first < 0:
                continue
            last = s.rfind(letter)
            if last - first >= 2:
                total += len(set(s[first + 1:last]))
        return total
