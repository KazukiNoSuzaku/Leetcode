# Author: Kaustav Ghosh
# Problem: Determine if Two Strings Are Close
# Approach: Swaps let counts move to any position and relabeling permutes which letter holds which count, so they are close iff same letter set and same multiset of counts

from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        c1, c2 = Counter(word1), Counter(word2)
        return set(c1) == set(c2) and sorted(c1.values()) == sorted(c2.values())
