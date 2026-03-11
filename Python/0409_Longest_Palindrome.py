# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        count = Counter(s)
        res = 0
        odd_found = False
        for c in count.values():
            res += c // 2 * 2
            if c % 2 == 1:
                odd_found = True
        return res + (1 if odd_found else 0)
