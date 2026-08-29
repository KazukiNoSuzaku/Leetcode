# Author: Kaustav Ghosh
# Problem: Minimum Number of Steps to Make Two Strings Anagram II
# Approach: Each append adds one character to either string. To make them anagrams, every mismatch in per-character counts must be filled, so the answer is the sum over all characters of the absolute difference of counts between s and t

from collections import Counter


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        cs, ct = Counter(s), Counter(t)
        steps = 0
        for ch in set(cs) | set(ct):
            steps += abs(cs[ch] - ct[ch])
        return steps
