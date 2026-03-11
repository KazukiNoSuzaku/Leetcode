# Check if a matrix is Toeplitz (every diagonal has same elements).

# Author: Kaustav Ghosh

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] != matrix[r-1][c-1]:
                    return False
        return True
