# Author: Kaustav Ghosh
# Problem: Count Pairs Of Similar Strings
# Approach: Two words are similar exactly when they use the same set of letters, so reduce each word to that set and count how many words share it. A group of c words contributes c * (c - 1) / 2 pairs

from collections import Counter


class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        groups = Counter(frozenset(word) for word in words)
        return sum(c * (c - 1) // 2 for c in groups.values())
