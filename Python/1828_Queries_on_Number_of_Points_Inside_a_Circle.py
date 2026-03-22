# Author: Kaustav Ghosh

class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for xc, yc, r in queries:
            count = 0
            r2 = r * r
            for px, py in points:
                if (px - xc) ** 2 + (py - yc) ** 2 <= r2:
                    count += 1
            res.append(count)
        return res
