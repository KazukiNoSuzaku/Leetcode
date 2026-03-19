# Author: Kaustav Ghosh
# https://leetcode.com/problems/determine-if-two-strings-are-close/

from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        c1 = Counter(word1)
        c2 = Counter(word2)
        return set(c1.keys()) == set(c2.keys()) and sorted(c1.values()) == sorted(c2.values())
