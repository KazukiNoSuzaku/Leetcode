# Author: Kaustav Ghosh
# https://leetcode.com/problems/coordinate-with-maximum-network-quality/

class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        import math
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
