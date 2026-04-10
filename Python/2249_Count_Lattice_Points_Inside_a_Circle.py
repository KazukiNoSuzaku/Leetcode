# Author: Kaustav Ghosh
# Problem: 2249. Count Lattice Points Inside a Circle
# URL: https://leetcode.com/problems/count-lattice-points-inside-a-circle/
# Difficulty: Medium
#
# Approach:
# For each lattice point in the bounding box of all circles, check if it
# lies inside or on any circle using the distance squared formula.

class Solution(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        points = set()
        for x, y, r in circles:
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                        points.add((i, j))
        return len(points)
