# Author: Kaustav Ghosh
# Problem: Number of Good Ways to Split a String
# Approach: Slide a split point; maintain left Counter growing right, right Counter shrinking left; count equal distinct sizes

from collections import Counter

class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = Counter()
        right = Counter(s)
        ans = 0
        for c in s[:-1]:
            left[c] += 1
            right[c] -= 1
            if right[c] == 0:
                del right[c]
            if len(left) == len(right):
                ans += 1
        return ans
