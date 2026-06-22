from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [sum(grid[r]) for r in range(m)]
        col = [sum(grid[r][c] for r in range(m)) for c in range(n)]
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    ans += (row[r] - 1) * (col[c] - 1)
        return ans
