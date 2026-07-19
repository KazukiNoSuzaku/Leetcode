# Author: Kaustav Ghosh
# Problem: Find Nearest Point That Has the Same X or Y Coordinate
# Approach: Among points sharing our x or y (so the distance is a clean Manhattan gap), keep the smallest distance, earliest index breaking ties

class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        best_index = -1
        best_dist = float('inf')
        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                dist = abs(px - x) + abs(py - y)
                if dist < best_dist:
                    best_dist = dist
                    best_index = i
        return best_index
