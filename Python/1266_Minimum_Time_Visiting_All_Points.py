# Author: Kaustav Ghosh
# Chebyshev distance: max of absolute x and y differences

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total = 0
        for i in range(1, len(points)):
            dx = abs(points[i][0] - points[i - 1][0])
            dy = abs(points[i][1] - points[i - 1][1])
            total += max(dx, dy)
        return total
