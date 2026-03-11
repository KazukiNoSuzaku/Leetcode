# There is an m x n grid with a ball. Given the position of the ball and maxMove moves allowed,
# return the number of paths to move the ball out of the grid boundary. Answer mod 10^9+7.

# Author: Kaustav Ghosh

class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = 10**9 + 7
        dp = [[0]*n for _ in range(m)]
        dp[startRow][startColumn] = 1
        res = 0
        for _ in range(maxMove):
            ndp = [[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if dp[i][j]:
                        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                            ni, nj = i+di, j+dj
                            if 0 <= ni < m and 0 <= nj < n:
                                ndp[ni][nj] = (ndp[ni][nj] + dp[i][j]) % MOD
                            else:
                                res = (res + dp[i][j]) % MOD
            dp = ndp
        return res
