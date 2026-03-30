# Author: Kaustav Ghosh
# Problem: 2178. Maximum Split of Positive Even Integers
# URL: https://leetcode.com/problems/maximum-split-of-positive-even-integers/
# Approach: Greedily pick distinct even integers 2, 4, 6, ... until adding the
#           next would exceed the remainder. Add the leftover to the last element.
#           If finalSum is odd, return [].

class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        if finalSum % 2 != 0:
            return []
        result = []
        curr = 2
        remaining = finalSum
        while remaining >= curr:
            result.append(curr)
            remaining -= curr
            curr += 2
        # Add leftover to the last element to keep it even and distinct
        if remaining > 0:
            result[-1] += remaining
        return result
