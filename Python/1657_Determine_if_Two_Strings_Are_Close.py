# Author: Kaustav Ghosh
# Problem: Determine if Two Strings Are Close
# Approach: Swapping two characters rearranges letters freely, so position never matters and only the counts do; swapping two whole letters permutes which letter carries which count but can never introduce a letter that was absent or remove one entirely, because a letter with a count of zero has nothing to swap. That leaves exactly two conditions: the two words use the same set of letters, and the multiset of their counts agrees, the latter checked by sorting the counts rather than comparing them letter by letter.

from collections import Counter


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        first = Counter(word1)
        second = Counter(word2)
        return set(first) == set(second) and sorted(first.values()) == sorted(second.values())
