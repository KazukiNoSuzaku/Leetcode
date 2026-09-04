# Author: Kaustav Ghosh
# Problem: Count Lattice Points Inside a Circle
# Approach: Coordinates are small, so scan every lattice point within each circle's bounding box and collect those lying inside or on that circle (dx*dx + dy*dy <= r*r) into a set. The set size is the count of distinct covered lattice points

class Solution(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        points = set()
        for x, y, r in circles:
            for px in range(x - r, x + r + 1):
                for py in range(y - r, y + r + 1):
                    if (px - x) ** 2 + (py - y) ** 2 <= r * r:
                        points.add((px, py))
        return len(points)
