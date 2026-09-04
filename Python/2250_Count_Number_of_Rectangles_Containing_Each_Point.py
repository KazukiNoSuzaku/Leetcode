# Author: Kaustav Ghosh
# Problem: Count Number of Rectangles Containing Each Point
# Approach: A rectangle [l, h] contains point (x, y) when l >= x and h >= y. Heights are small (<= 100), so bucket rectangle lengths by height and sort each bucket. For a point, sum over heights >= y the count of lengths >= x using binary search

import bisect


class Solution(object):
    def countRectangles(self, rectangles, points):
        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]
        """
        MAXH = 100
        buckets = [[] for _ in range(MAXH + 1)]
        for l, h in rectangles:
            buckets[h].append(l)
        for h in range(MAXH + 1):
            buckets[h].sort()

        res = []
        for x, y in points:
            count = 0
            for h in range(y, MAXH + 1):
                lst = buckets[h]
                count += len(lst) - bisect.bisect_left(lst, x)
            res.append(count)
        return res
