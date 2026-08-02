# Author: Kaustav Ghosh
# Problem: Largest Magic Square
# Approach: Precompute row and column prefix sums; try squares from largest to smallest and confirm every row, column, and both diagonals share the same sum

class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]

        def is_magic(i, j, k):
            target = row[i][j + k] - row[i][j]
            for r in range(i, i + k):
                if row[r][j + k] - row[r][j] != target:
                    return False
            for c in range(j, j + k):
                if col[i + k][c] - col[i][c] != target:
                    return False
            if sum(grid[i + t][j + t] for t in range(k)) != target:
                return False
            if sum(grid[i + t][j + k - 1 - t] for t in range(k)) != target:
                return False
            return True

        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_magic(i, j, k):
                        return k
        return 1
