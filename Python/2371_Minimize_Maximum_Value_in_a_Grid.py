# Premium problem
# Assign each cell the minimum possible positive integer such that
# values are strictly increasing left-to-right and top-to-bottom.
# Strategy: sort cells by value, assign rank = 1 + max(row_rank, col_rank)

class Solution:
    def minScore(self, grid: list[list[int]]) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        cells = sorted((grid[i][j], i, j) for i in range(m) for j in range(n))
        row_max = [0] * m
        col_max = [0] * n
        ans = [[0] * n for _ in range(m)]
        for _, i, j in cells:
            rank = max(row_max[i], col_max[j]) + 1
            ans[i][j] = rank
            row_max[i] = col_max[j] = rank
        return ans
