# Author: Kaustav Ghosh
# Problem: Maximum Number of Darts Inside of a Circular Dartboard
# Approach: For each pair of points, find circles of radius r passing through both

import math

class Solution(object):
    def numPoints(self, darts, r):
        """
        :type darts: List[List[int]]
        :type r: int
        :rtype: int
        """
        n = len(darts)
        if n == 1:
            return 1
        result = 1

        def dist(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        def get_centers(p1, p2, r):
            d = dist(p1, p2)
            if d > 2 * r:
                return []
            mx, my = (p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0
            h = math.sqrt(r * r - (d / 2.0) ** 2)
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            return [
                (mx + h * dy / d, my - h * dx / d),
                (mx - h * dy / d, my + h * dx / d)
            ]

        for i in range(n):
            for j in range(i + 1, n):
                centers = get_centers(darts[i], darts[j], r)
                for cx, cy in centers:
                    count = sum(1 for x, y in darts
                                if (x - cx) ** 2 + (y - cy) ** 2 <= r * r + 1e-6)
                    result = max(result, count)
        return result
