# Author: Kaustav Ghosh
# Problem 2068: Check Whether Two Strings are Almost Equivalent

class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        freq = {}
        for c in word1:
            freq[c] = freq.get(c, 0) + 1
        for c in word2:
            freq[c] = freq.get(c, 0) - 1
        for v in freq.values():
            if abs(v) > 3:
                return False
        return True
