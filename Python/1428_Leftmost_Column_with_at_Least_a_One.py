# Author: Kaustav Ghosh
# Problem: Leftmost Column with at Least a One (Premium)
# Approach: Start from top-right corner, move left on 1, down on 0

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        rows, cols = binaryMatrix.dimensions()
        r, c = 0, cols - 1
        result = -1
        while r < rows and c >= 0:
            if binaryMatrix.get(r, c) == 1:
                result = c
                c -= 1
            else:
                r += 1
        return result
