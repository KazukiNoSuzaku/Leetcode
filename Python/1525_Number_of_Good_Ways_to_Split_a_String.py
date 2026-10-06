# Author: Kaustav Ghosh
# Problem: Number of Good Ways to Split a String
# Approach: Start with every letter counted on the right, then move the split point rightwards one character at a time, transferring that character between the two tallies. The split is good whenever the two tallies hold the same number of distinct letters

from collections import Counter


class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = Counter(s)
        left = Counter()
        good = 0
        for ch in s[:-1]:
            left[ch] += 1
            right[ch] -= 1
            if right[ch] == 0:
                del right[ch]
            if len(left) == len(right):
                good += 1
        return good
