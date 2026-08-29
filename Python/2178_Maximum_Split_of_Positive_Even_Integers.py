# Author: Kaustav Ghosh
# Problem: Maximum Split of Positive Even Integers
# Approach: An odd sum cannot be split into even integers. Otherwise greedily take 2, 4, 6, ... while they fit; the leftover (still even and smaller than the next candidate) is added to the last taken value to keep them distinct

class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        if finalSum % 2 == 1:
            return []
        result = []
        cur = 2
        remaining = finalSum
        while cur <= remaining:
            result.append(cur)
            remaining -= cur
            cur += 2
        if remaining > 0:
            result[-1] += remaining
        return result
