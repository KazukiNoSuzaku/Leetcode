class Solution:
    def isPossibleToCutPath(self, grid: list[list[int]]) -> bool:
        # DFS1 finds one path and marks its cells 0; if DFS2 finds another, two disjoint paths exist.
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return True
            grid[i][j] = 0
            if i + 1 < m and grid[i + 1][j] and dfs(i + 1, j):
                return True
            if j + 1 < n and grid[i][j + 1] and dfs(i, j + 1):
                return True
            return False

        if not dfs(0, 0):
            return True
        grid[0][0] = grid[m - 1][n - 1] = 1
        return not dfs(0, 0)
