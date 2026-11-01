# Author: Kaustav Ghosh
# Problem: Find Nearest Point That Has the Same X or Y Coordinate
# Approach: A point is only valid when it shares a row or a column, and for such a point one of the two coordinate differences is zero, so its Manhattan distance collapses to the single remaining difference. One pass keeps the best distance seen so far and only replaces it on a strict improvement, which naturally returns the smallest index among ties.

class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        best = -1
        closest = 0
        for index, (px, py) in enumerate(points):
            if px != x and py != y:
                continue
            distance = abs(px - x) + abs(py - y)
            if best < 0 or distance < closest:
                best, closest = index, distance
        return best
