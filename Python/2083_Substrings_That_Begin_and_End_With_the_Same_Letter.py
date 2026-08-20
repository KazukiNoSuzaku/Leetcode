# Author: Kaustav Ghosh
# Problem: Substrings That Begin and End With the Same Letter
# Approach: A qualifying substring is chosen by picking two positions (i <= j) holding the same letter. For a letter occurring c times that is c*(c+1)/2 substrings; sum over letters

from collections import Counter

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        return sum(c * (c + 1) // 2 for c in counts.values())
