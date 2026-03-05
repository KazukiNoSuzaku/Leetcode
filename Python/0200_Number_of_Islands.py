# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

# Example 1:
# Input: grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# Output: 1

# Example 2:
# Input: grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
# Output: 3

# Constraints:
# m == grid.length, n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# Author: Kaustav Ghosh

class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(r + dr, c + dc)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count
