# Author: Kaustav Ghosh
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = {}
        result = -1
        for i, c in enumerate(s):
            if c in first:
                result = max(result, i - first[c] - 1)
            else:
                first[c] = i
        return result
