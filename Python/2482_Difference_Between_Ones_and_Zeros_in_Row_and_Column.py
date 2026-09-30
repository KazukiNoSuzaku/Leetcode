# Author: Kaustav Ghosh
# Problem: Difference Between Ones and Zeros in Row and Column
# Approach: A row's zeros are its width minus its ones, and likewise for a column, so the whole expression collapses to twice the row's ones minus the width plus twice the column's ones minus the height. Count ones per row and per column once, then fill the answer

class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(grid), len(grid[0])
        row_ones = [sum(row) for row in grid]
        col_ones = [sum(column) for column in zip(*grid)]
        return [[2 * row_ones[i] - cols + 2 * col_ones[j] - rows for j in range(cols)]
                for i in range(rows)]
