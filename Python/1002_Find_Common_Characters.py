# Given an array of strings, return a list of all characters that appear in all strings
# (including duplicates if they appear multiple times in all).

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def commonChars(self, words):
        common = Counter(words[0])
        for w in words[1:]:
            common &= Counter(w)
        res = []
        for c, cnt in common.items():
            res.extend([c] * cnt)
        return res
