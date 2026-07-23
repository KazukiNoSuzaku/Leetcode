# Author: Kaustav Ghosh
# Problem: Determine Color of a Chessboard Square
# Approach: a1 is black; a square is white exactly when its column letter and row number have opposite parity, i.e. their sum is odd

class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        column = ord(coordinates[0]) - ord('a')
        row = int(coordinates[1]) - 1
        return (column + row) % 2 == 1
