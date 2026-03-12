# Author: Kaustav Ghosh
# Check collinearity using cross product

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]
        for i in range(2, len(coordinates)):
            dx2 = coordinates[i][0] - coordinates[0][0]
            dy2 = coordinates[i][1] - coordinates[0][1]
            if dx * dy2 != dy * dx2:
                return False
        return True
