# Author: Kaustav Ghosh
# Problem: Add Minimum Number of Rungs
# Approach: Walk the rungs in order tracking the last reachable height. For each gap larger than dist, insert ceil(gap/dist) - 1 evenly spaced rungs to bridge it

class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        added = 0
        prev = 0
        for r in rungs:
            gap = r - prev
            if gap > dist:
                added += (gap - 1) // dist
            prev = r
        return added
