# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Divide and conquer with hasShips API

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: int
        """
        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1

        mid_x = (topRight.x + bottomLeft.x) // 2
        mid_y = (topRight.y + bottomLeft.y) // 2

        count = 0
        # Bottom-left quadrant
        count += self.countShips(sea, Point(mid_x, mid_y), bottomLeft)
        # Bottom-right quadrant
        count += self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))
        # Top-left quadrant
        count += self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1))
        # Top-right quadrant
        count += self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1))
        return count
