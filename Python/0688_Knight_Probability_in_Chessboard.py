# Find probability a knight stays on n x n board after k moves starting at (row, col).

# Author: Kaustav Ghosh

class Solution(object):
    def knightProbability(self, n, k, row, column):
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0
        moves = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
        for _ in range(k):
            ndp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c]:
                        for dr, dc in moves:
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < n and 0 <= nc < n:
                                ndp[nr][nc] += dp[r][c] / 8.0
            dp = ndp
        return sum(dp[r][c] for r in range(n) for c in range(n))
