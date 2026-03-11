# You are given an array of points on the X-Y plane points where points[i] = [xi, yi].
# Return true if these points form a convex polygon. The polygon is always valid with at least 3 points.

# Author: Kaustav Ghosh

class Solution(object):
    def isConvex(self, points):
        n = len(points)
        sign = 0
        for i in range(n):
            dx1 = points[(i+1) % n][0] - points[i][0]
            dy1 = points[(i+1) % n][1] - points[i][1]
            dx2 = points[(i+2) % n][0] - points[(i+1) % n][0]
            dy2 = points[(i+2) % n][1] - points[(i+1) % n][1]
            cross = dx1 * dy2 - dy1 * dx2
            if cross != 0:
                if sign == 0:
                    sign = 1 if cross > 0 else -1
                elif cross * sign < 0:
                    return False
        return True
