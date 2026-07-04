# Author: Kaustav Ghosh
# Problem: Find Valid Matrix Given Row and Column Sums
# Approach: Greedily fill each cell with min(remaining row sum, remaining col sum); it always exhausts one of them and stays consistent

class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        m, n = len(rowSum), len(colSum)
        row = rowSum[:]
        col = colSum[:]
        mat = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                v = min(row[i], col[j])
                mat[i][j] = v
                row[i] -= v
                col[j] -= v
        return mat
