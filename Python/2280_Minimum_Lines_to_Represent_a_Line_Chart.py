# Author: Kaustav Ghosh
# Problem: Minimum Lines to Represent a Line Chart
# Approach: Sort points by day. Consecutive points share a line segment while their direction is unchanged; a new line begins whenever the slope changes. Compare slopes exactly with the cross product of consecutive vectors to avoid floating point. The number of lines is one plus the count of direction changes

class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        if len(stockPrices) <= 1:
            return 0
        pts = sorted(stockPrices)
        lines = 1
        for i in range(2, len(pts)):
            x0, y0 = pts[i - 2]
            x1, y1 = pts[i - 1]
            x2, y2 = pts[i]
            # cross product of (p1-p0) and (p2-p1)
            if (x1 - x0) * (y2 - y1) != (x2 - x1) * (y1 - y0):
                lines += 1
        return lines
