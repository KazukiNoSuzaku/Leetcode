# Author: Kaustav Ghosh
# Backtracking DFS from each non-zero cell to collect maximum gold

class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        result = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            gold = grid[r][c]
            grid[r][c] = 0  # mark visited
            max_gold = 0
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                max_gold = max(max_gold, dfs(r + dr, c + dc))
            grid[r][c] = gold  # restore
            return gold + max_gold

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    result = max(result, dfs(i, j))
        return result
