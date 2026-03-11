# Given two strings s1 and s2, return true if s2 contains a permutation of s1.
# In other words, return true if one of s1's permutations is the substring of s2.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2): return False
        need = Counter(s1)
        window = Counter(s2[:len(s1)])
        if window == need: return True
        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            old = s2[i - len(s1)]
            window[old] -= 1
            if window[old] == 0: del window[old]
            if window == need: return True
        return False
