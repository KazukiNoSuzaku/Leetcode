# Author: Kaustav Ghosh
# Problem: Matrix Diagonal Sum
# Approach: Add both diagonals in one pass; if n is odd the center cell is shared, so subtract it once

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i] + mat[i][n - 1 - i]
        if n % 2:
            total -= mat[n // 2][n // 2]
        return total
