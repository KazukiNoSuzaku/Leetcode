class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                total = (grid[r-1][c-1] + grid[r-1][c] + grid[r-1][c+1]
                       + grid[r][c]
                       + grid[r+1][c-1] + grid[r+1][c] + grid[r+1][c+1])
                ans = max(ans, total)
        return ans
