# Author: Kaustav Ghosh
# Problem: Check if All Characters Have Equal Number of Occurrences
# Approach: Count each character; the string is good iff every distinct character occurs the same number of times (the set of counts has size 1)

from collections import Counter

class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return len(set(Counter(s).values())) == 1
