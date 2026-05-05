class Solution:
    def isThereAPath(self, grid: list[list[int]]) -> bool:
        # Path length is always m+n-1; must be even for a 50/50 split.
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False
        target = (m + n - 1) // 2
        INF = float('inf')
        lo = [[INF] * n for _ in range(m)]
        hi = [[-INF] * n for _ in range(m)]
        lo[0][0] = hi[0][0] = 1 - grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                v = 1 - grid[i][j]
                plo, phi = INF, -INF
                if i > 0 and lo[i - 1][j] < INF:
                    plo = min(plo, lo[i - 1][j])
                    phi = max(phi, hi[i - 1][j])
                if j > 0 and lo[i][j - 1] < INF:
                    plo = min(plo, lo[i][j - 1])
                    phi = max(phi, hi[i][j - 1])
                if plo < INF:
                    lo[i][j] = plo + v
                    hi[i][j] = phi + v
        return lo[m - 1][n - 1] <= target <= hi[m - 1][n - 1]
