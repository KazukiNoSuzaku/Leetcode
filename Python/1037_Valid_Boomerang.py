# Author: Kaustav Ghosh
# 1037. Valid Boomerang
# https://leetcode.com/problems/valid-boomerang/

class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        (x1, y1), (x2, y2), (x3, y3) = points
        # Cross product of vectors (p2-p1) and (p3-p1) != 0
        return (x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1)
