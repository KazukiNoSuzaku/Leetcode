# Author: Kaustav Ghosh
# Problem: Matrix Diagonal Sum
# Approach: Row i contributes mat[i][i] from the primary diagonal and mat[i][n-1-i] from the secondary one, so a single pass over the rows collects both without touching the rest of the matrix; the only wrinkle is an odd-sized matrix, where the exact centre lies on both diagonals and would otherwise be counted twice, so it is subtracted once at the end.

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
