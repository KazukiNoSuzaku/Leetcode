# Author: Kaustav Ghosh
# Problem: Find Valid Matrix Given Row and Column Sums
# Approach: Walking the cells in order and greedily putting in as much as both its row and its column can still take always works: the amount is the smaller of the two remaining budgets, so whichever budget it exhausts is finished and that whole row or column can be left at zero from then on. Since the totals agree overall, no budget can be left stranded at the end, which is why the greedy never needs to backtrack.

class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        rows, cols = len(rowSum), len(colSum)
        rows_left = list(rowSum)
        cols_left = list(colSum)
        matrix = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                amount = rows_left[r] if rows_left[r] < cols_left[c] else cols_left[c]
                matrix[r][c] = amount
                rows_left[r] -= amount
                cols_left[c] -= amount
        return matrix
