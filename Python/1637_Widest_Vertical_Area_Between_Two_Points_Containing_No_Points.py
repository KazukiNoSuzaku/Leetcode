# Author: Kaustav Ghosh
# Problem: Widest Vertical Area Between Two Points Containing No Points
# Approach: A vertical strip is bounded only by x coordinates, so the y values are irrelevant and can be discarded outright; once the x values are sorted, an empty strip is exactly a gap between neighbouring values, and the widest one is the largest such difference. Repeated x values simply contribute a gap of zero and need no special handling.

class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        xs = sorted(x for x, _ in points)
        widest = 0
        for i in range(1, len(xs)):
            if xs[i] - xs[i - 1] > widest:
                widest = xs[i] - xs[i - 1]
        return widest
