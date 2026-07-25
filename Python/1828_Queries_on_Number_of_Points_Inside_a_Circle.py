# Author: Kaustav Ghosh
# Problem: Queries on Number of Points Inside a Circle
# Approach: For each circle, count points whose squared distance from the center is within r^2 (integer math avoids sqrt)

class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for x, y, r in queries:
            r2 = r * r
            res.append(sum(1 for px, py in points if (px - x) ** 2 + (py - y) ** 2 <= r2))
        return res
