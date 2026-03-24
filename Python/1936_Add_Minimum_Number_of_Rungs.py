# Author: Kaustav Ghosh
# https://leetcode.com/problems/add-minimum-number-of-rungs/

class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        count = 0
        prev = 0
        for r in rungs:
            gap = r - prev
            if gap > dist:
                count += (gap - 1) // dist
            prev = r
        return count
