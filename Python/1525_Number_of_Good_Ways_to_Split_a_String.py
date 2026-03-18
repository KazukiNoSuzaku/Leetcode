# Author: Kaustav Ghosh
# Problem: 1525 - Number of Good Ways to Split a String
# Approach: Count distinct chars in prefix and suffix using running sets

class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        right = Counter(s)
        left = set()
        result = 0

        for c in s:
            left.add(c)
            right[c] -= 1
            if right[c] == 0:
                del right[c]
            if len(left) == len(right):
                result += 1

        return result
