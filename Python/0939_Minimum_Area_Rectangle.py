# Find minimum area rectangle with sides parallel to axes from a set of points.

# Author: Kaustav Ghosh

class Solution(object):
    def minAreaRect(self, points):
        point_set = set(map(tuple, points))
        res = float('inf')
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1,y2) in point_set and (x2,y1) in point_set:
                        res = min(res, abs(x2-x1)*abs(y2-y1))
        return res if res < float('inf') else 0
