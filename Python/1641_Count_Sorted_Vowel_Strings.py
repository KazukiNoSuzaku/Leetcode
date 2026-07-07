# Author: Kaustav Ghosh
# Problem: Count Sorted Vowel Strings
# Approach: A sorted string is a multiset of 5 vowels of size n, i.e. stars-and-bars, giving C(n+4, 4)

from math import comb

class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        return comb(n + 4, 4)
