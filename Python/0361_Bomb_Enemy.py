# Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E'
# or empty '0', return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point
# until it hits the wall since it is too strong to be stopped.
# You can only plant the bomb in an empty cell.

# Example 1:
# Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# Output: 3

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 'W', 'E', or '0'.

# Author: Kaustav Ghosh

class Solution(object):
    def maxKilledEnemies(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        row_hits = 0
        col_hits = [0] * n

        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    row_hits = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        if grid[i][k] == 'E':
                            row_hits += 1
                if i == 0 or grid[i - 1][j] == 'W':
                    col_hits[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        if grid[k][j] == 'E':
                            col_hits[j] += 1
                if grid[i][j] == '0':
                    res = max(res, row_hits + col_hits[j])
        return res
