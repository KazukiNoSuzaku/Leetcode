# Author: Kaustav Ghosh
# Problem: Coordinate With Maximum Network Quality
# Approach: Coordinates are bounded to 0..50, so scan the whole grid, sum each tower's floor(q/(1+dist)) within radius, and keep the best (lexicographically smallest on ties)

import math

class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        best_quality = 0
        best = [0, 0]
        for x in range(51):
            for y in range(51):
                quality = 0
                for tx, ty, q in towers:
                    d = math.sqrt((x - tx) ** 2 + (y - ty) ** 2)
                    if d <= radius:
                        quality += int(q / (1 + d))
                if quality > best_quality:
                    best_quality = quality
                    best = [x, y]
        return best
