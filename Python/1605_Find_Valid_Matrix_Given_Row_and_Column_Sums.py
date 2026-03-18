# Author: Kaustav Ghosh
# Problem: 1605 - Find Valid Matrix Given Row and Column Sums
# Approach: Greedy: fill min(row_sum, col_sum) at each cell

class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                val = min(rowSum[i], colSum[j])
                matrix[i][j] = val
                rowSum[i] -= val
                colSum[j] -= val

        return matrix
