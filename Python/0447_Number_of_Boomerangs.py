# You are given n points in the plane that are all distinct.
# A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals
# the distance between i and k (the order of the tuple matters).
# Return the number of boomerangs.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def numberOfBoomerangs(self, points):
        res = 0
        for x1, y1 in points:
            dist_count = defaultdict(int)
            for x2, y2 in points:
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                dist_count[d] += 1
            for count in dist_count.values():
                res += count * (count - 1)
        return res
