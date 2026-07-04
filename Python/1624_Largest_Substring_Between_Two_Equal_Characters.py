# Author: Kaustav Ghosh
# Problem: Largest Substring Between Two Equal Characters
# Approach: Remember the first index of each character; on a repeat, the gap between them is a candidate answer

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = {}
        best = -1
        for i, c in enumerate(s):
            if c in first:
                best = max(best, i - first[c] - 1)
            else:
                first[c] = i
        return best
