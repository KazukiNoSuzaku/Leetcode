# Author: Kaustav Ghosh
# Problem: Add Minimum Number of Rungs
# Approach: The gaps between consecutive rungs are independent: a climb of length gap from one rung to the next needs the gap divided into steps of at most dist, which takes ceil(gap / dist) steps and therefore ceil(gap / dist) - 1 new rungs in between, and no choice made in one gap can help another. Writing that count as (gap - 1) // dist keeps the arithmetic in integers so no floating-point rounding can land on the wrong side of an exact multiple, and summing it over every gap, starting from the floor at height zero, gives the answer in a single pass.

class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        added = 0
        height = 0
        for rung in rungs:
            added += (rung - height - 1) // dist
            height = rung
        return added
