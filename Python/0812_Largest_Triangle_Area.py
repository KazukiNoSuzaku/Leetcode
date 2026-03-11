# Find the largest triangle area from a set of points.

# Author: Kaustav Ghosh

from itertools import combinations

class Solution(object):
    def largestTriangleArea(self, points):
        def area(p1, p2, p3):
            return abs(p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0
        return max(area(*tri) for tri in combinations(points, 3))
