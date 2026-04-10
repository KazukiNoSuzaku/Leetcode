# Author: Kaustav Ghosh
# Problem: 2250. Count Number of Rectangles Containing Each Point
# URL: https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/
# Difficulty: Medium
#
# Approach:
# Group rectangle x-coordinates by their y-coordinate (y <= 100). Sort
# each group. For each query point (px, py), binary search in each group
# with y >= py to count rectangles with x >= px.

import bisect

class Solution(object):
    def countRectangles(self, rectangles, points):
        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]
        """
        # Group x values by y height (y ranges from 1 to 100)
        by_y = [[] for _ in range(101)]
        for x, y in rectangles:
            by_y[y].append(x)
        for y in range(101):
            by_y[y].sort()

        result = []
        for px, py in points:
            count = 0
            for y in range(py, 101):
                xs = by_y[y]
                if xs:
                    idx = bisect.bisect_left(xs, px)
                    count += len(xs) - idx
            result.append(count)
        return result
