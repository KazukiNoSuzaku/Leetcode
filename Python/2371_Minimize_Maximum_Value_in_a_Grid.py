# Author: Kaustav Ghosh
# Problem: Minimize Maximum Value in a Grid
# Approach: Process the cells in increasing order of their original value, which is a valid order because the values are distinct. Each cell only has to beat whatever is already placed in its row and in its column, so give it max(row_best, col_best) + 1 and update both; assigning every cell the smallest value it can legally take keeps the overall maximum as low as possible

class Solution(object):
    def minScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(grid), len(grid[0])
        row_best = [0] * rows
        col_best = [0] * cols
        result = [[0] * cols for _ in range(rows)]
        cells = sorted((grid[r][c], r, c) for r in range(rows) for c in range(cols))
        for _, r, c in cells:
            value = max(row_best[r], col_best[c]) + 1
            result[r][c] = value
            row_best[r] = value
            col_best[c] = value
        return result
