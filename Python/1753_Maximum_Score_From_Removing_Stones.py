# Author: Kaustav Ghosh
# Problem: Maximum Score From Removing Stones
# Approach: Every move takes one stone from each of two different piles, so two limits apply: the total number of moves can never exceed half the stones, since each move removes two, and it can never exceed the sum of the two smaller piles, because every move must touch at least one of them. Both bounds are simultaneously achievable by always drawing from the two largest piles, which keeps them level, so the answer is whichever bound is tighter.

class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        total = a + b + c
        largest = max(a, b, c)
        return min(total // 2, total - largest)
