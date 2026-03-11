# Given two strings s and p, return an array of all the start indices of p's anagrams in s.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        p_count = Counter(p)
        window = Counter(s[:len(p)])
        res = [0] if window == p_count else []
        for i in range(len(p), len(s)):
            window[s[i]] += 1
            old = s[i - len(p)]
            window[old] -= 1
            if window[old] == 0:
                del window[old]
            if window == p_count:
                res.append(i - len(p) + 1)
        return res
