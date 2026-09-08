# Author: Kaustav Ghosh
# Problem: Rearrange Characters to Make Target String
# Approach: Each copy of target consumes a fixed multiset of characters. The number of copies is limited by the scarcest target character: the minimum over target's distinct characters of (available in s) // (needed per copy)

from collections import Counter


class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        have = Counter(s)
        need = Counter(target)
        return min(have[ch] // cnt for ch, cnt in need.items())
