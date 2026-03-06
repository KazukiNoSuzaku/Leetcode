# Given an m x n binary grid grid where each 1 marks the home of one friend, return the
# minimum total travel distance. The total travel distance is the sum of the distances between
# the houses of the friends and the meeting point. The distance is calculated using Manhattan Distance.

# Example 1:
# Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# Output: 6

# Constraints:
# m == grid.length, n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j] is either 0 or 1.

# Author: Kaustav Ghosh

class Solution(object):
    def minTotalDistance(self, grid):
        rows, cols = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        cols.sort()
        mid_r = rows[len(rows) // 2]
        mid_c = cols[len(cols) // 2]
        return sum(abs(r - mid_r) for r in rows) + sum(abs(c - mid_c) for c in cols)
