# Author: Kaustav Ghosh
# Problem: 2287. Rearrange Characters to Make Target String
# URL: https://leetcode.com/problems/rearrange-characters-to-make-target-string/
# Difficulty: Easy
#
# Approach:
# Count character frequencies in s and target. The answer is the minimum
# of s_count[c] // target_count[c] for all characters c in target.

from collections import Counter

class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        s_count = Counter(s)
        t_count = Counter(target)
        result = float('inf')
        for c, cnt in t_count.items():
            result = min(result, s_count[c] // cnt)
        return result
