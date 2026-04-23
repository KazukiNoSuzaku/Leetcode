# Premium problem
# Binary search on value: find smallest x where count of elements <= x >= (m*n+1)//2
import bisect

class Solution:
    def matrixMedian(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        target = (m * n + 1) // 2
        lo, hi = grid[0][0], grid[0][-1]
        for row in grid:
            lo = min(lo, row[0])
            hi = max(hi, row[-1])
        while lo < hi:
            mid = (lo + hi) // 2
            count = sum(bisect.bisect_right(row, mid) for row in grid)
            if count >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo
