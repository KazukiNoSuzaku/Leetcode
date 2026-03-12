# Author: Kaustav Ghosh
# 1081. Smallest Subsequence of Distinct Characters
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

from collections import Counter

class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and stack[-1] > c and last[stack[-1]] > i:
                seen.discard(stack.pop())
            stack.append(c)
            seen.add(c)
        return ''.join(stack)
