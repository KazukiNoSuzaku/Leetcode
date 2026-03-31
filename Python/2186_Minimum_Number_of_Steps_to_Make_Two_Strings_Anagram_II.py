# Author: Kaustav Ghosh
# 2186. Minimum Number of Steps to Make Two Strings Anagram II
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/
# Difficulty: Medium
#
# Approach: Count character frequencies in both strings. For each character,
# the number of insertions needed is the absolute difference of frequencies.
# Sum over all characters gives the total steps.
# Time: O(n + m), Space: O(26)

from collections import Counter

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        cs = Counter(s)
        ct = Counter(t)
        steps = 0
        all_chars = set(cs.keys()) | set(ct.keys())
        for c in all_chars:
            steps += abs(cs[c] - ct[c])
        return steps
