# Author: Kaustav Ghosh
# Problem: Widest Vertical Area Between Two Points Containing No Points
# Approach: Only x-coordinates matter; sort them and take the largest gap between consecutive values

class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        xs = sorted(x for x, _ in points)
        return max((xs[i] - xs[i - 1] for i in range(1, len(xs))), default=0)
