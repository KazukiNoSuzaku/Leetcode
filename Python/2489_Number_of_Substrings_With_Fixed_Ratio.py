# Author: Kaustav Ghosh
# Problem: Number of Substrings With Fixed Ratio
# Approach: A substring has ratio num1 : num2 when its zeros times num2 equals its ones times num1. Writing both counts as differences of prefix counts, that condition says two prefixes share the value num2 * zeros - num1 * ones, so tally how often each such value has appeared and add the matches as the scan goes

from collections import defaultdict


class Solution(object):
    def fixedRatio(self, s, num1, num2):
        """
        :type s: str
        :type num1: int
        :type num2: int
        :rtype: int
        """
        seen = defaultdict(int)
        seen[0] = 1
        zeros = ones = 0
        total = 0
        for ch in s:
            if ch == '0':
                zeros += 1
            else:
                ones += 1
            key = num2 * zeros - num1 * ones
            total += seen[key]
            seen[key] += 1
        return total
