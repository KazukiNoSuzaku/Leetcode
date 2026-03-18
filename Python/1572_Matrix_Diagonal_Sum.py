# Author: Kaustav Ghosh
# Problem: 1572 - Matrix Diagonal Sum
# Approach: Sum primary and secondary diagonals, subtract center if odd size

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
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]
        return total
