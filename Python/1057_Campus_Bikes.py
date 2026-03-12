# Author: Kaustav Ghosh
# 1057. Campus Bikes
# https://leetcode.com/problems/campus-bikes/

class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        pairs = []
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx - bx) + abs(wy - by)
                pairs.append((dist, i, j))
        pairs.sort()
        result = [-1] * len(workers)
        used_bikes = set()
        for dist, w, b in pairs:
            if result[w] == -1 and b not in used_bikes:
                result[w] = b
                used_bikes.add(b)
        return result
