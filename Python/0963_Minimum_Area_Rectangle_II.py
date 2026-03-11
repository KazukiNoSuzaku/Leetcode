# Given a set of points, return the minimum area of any rectangle (not necessarily axis-aligned).
# Return 0 if no rectangle can be formed.

# Author: Kaustav Ghosh

import math

class Solution(object):
    def minAreaFreeRect(self, points):
        pts = set(map(tuple, points))
        n = len(points)
        res = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                # Try diagonal from points[i] to points[j]
                cx = points[i][0] + points[j][0]
                cy = points[i][1] + points[j][1]
                # Look for other pairs with same midpoint
                for k in range(j + 1, n):
                    x4 = cx - points[k][0]
                    y4 = cy - points[k][1]
                    if (x4, y4) in pts:
                        # Check right angle: diag1 dot diag2 == 0
                        # vectors from points[k] to points[i] and points[j]
                        d1x = points[i][0] - points[k][0]
                        d1y = points[i][1] - points[k][1]
                        d2x = points[j][0] - points[k][0]
                        d2y = points[j][1] - points[k][1]
                        if d1x * d2x + d1y * d2y == 0:
                            area = math.sqrt(d1x*d1x + d1y*d1y) * math.sqrt(d2x*d2x + d2y*d2y)
                            res = min(res, area)
        return 0 if res == float('inf') else res
