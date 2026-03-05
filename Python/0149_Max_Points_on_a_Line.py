# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
# return the maximum number of points that lie on the same straight line.

# Example 1:
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3

# Example 2:
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4

# Constraints:
# 1 <= points.length <= 300
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# All the points are unique.

# Author: Kaustav Ghosh

from collections import defaultdict
from math import gcd

class Solution(object):
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n
        result = 2
        for i in range(n):
            slopes = defaultdict(int)
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                g = gcd(abs(dx), abs(dy))
                if g != 0:
                    dx, dy = dx // g, dy // g
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = abs(dy)
                slopes[(dx, dy)] += 1
                result = max(result, slopes[(dx, dy)] + 1)
        return result
