# Author: Kaustav Ghosh

class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        col = ord(coordinates[0]) - ord('a')
        row = int(coordinates[1])
        return (col + row) % 2 == 0
