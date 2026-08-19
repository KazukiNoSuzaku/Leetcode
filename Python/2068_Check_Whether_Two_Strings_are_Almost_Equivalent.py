# Author: Kaustav Ghosh
# Problem: Check Whether Two Strings are Almost Equivalent
# Approach: The strings are almost equivalent if, for every letter, the difference in frequency between the two strings is at most 3

from collections import Counter

class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        c1 = Counter(word1)
        c2 = Counter(word2)
        return all(abs(c1[ch] - c2[ch]) <= 3 for ch in set(word1) | set(word2))
