# Author: Kaustav Ghosh
# Problem: Circle and Rectangle Overlapping
# Approach: Clamp circle center to nearest point on rectangle, check distance

class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        return dx * dx + dy * dy <= radius * radius
