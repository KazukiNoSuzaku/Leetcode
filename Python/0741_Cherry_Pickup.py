# Find max cherries collectible by going from top-left to bottom-right and back.

# Author: Kaustav Ghosh

class Solution(object):
    def cherryPickup(self, grid):
        n = len(grid)
        memo = {}
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n: return float('-inf')
            if grid[r1][c1] == -1 or grid[r2][c2] == -1: return float('-inf')
            if r1 == n-1 and c1 == n-1: return grid[r1][c1]
            if (r1, c1, r2) in memo: return memo[(r1, c1, r2)]
            cherries = grid[r1][c1] + (grid[r2][c2] if r2 != r1 else 0)
            best = max(dp(r1+1, c1, r2+1), dp(r1, c1+1, r2),
                       dp(r1+1, c1, r2), dp(r1, c1+1, r2+1))
            cherries += best
            memo[(r1, c1, r2)] = cherries
            return cherries
        return max(0, dp(0, 0, 0))
