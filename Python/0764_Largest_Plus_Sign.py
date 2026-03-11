# Find the order of largest plus sign in a grid with mines.

# Author: Kaustav Ghosh

class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        grid = [[n] * n for _ in range(n)]
        mine_set = set(map(tuple, mines))
        for r in range(n):
            left = right = up = down = 0
            for c in range(n):
                left = 0 if (r, c) in mine_set else left + 1
                grid[r][c] = min(grid[r][c], left)
            for c in range(n - 1, -1, -1):
                right = 0 if (r, c) in mine_set else right + 1
                grid[r][c] = min(grid[r][c], right)
        for c in range(n):
            up = down = 0
            for r in range(n):
                up = 0 if (r, c) in mine_set else up + 1
                grid[r][c] = min(grid[r][c], up)
            for r in range(n - 1, -1, -1):
                down = 0 if (r, c) in mine_set else down + 1
                grid[r][c] = min(grid[r][c], down)
        return max(grid[r][c] for r in range(n) for c in range(n))
