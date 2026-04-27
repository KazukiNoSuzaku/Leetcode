class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for r in range(m):
            for c in range(n):
                for rem in range(k):
                    if dp[r][c][rem] == 0:
                        continue
                    for dr, dc in ((0, 1), (1, 0)):
                        nr, nc = r + dr, c + dc
                        if nr < m and nc < n:
                            new_rem = (rem + grid[nr][nc]) % k
                            dp[nr][nc][new_rem] = (dp[nr][nc][new_rem] + dp[r][c][rem]) % MOD
        return dp[m - 1][n - 1][0]
