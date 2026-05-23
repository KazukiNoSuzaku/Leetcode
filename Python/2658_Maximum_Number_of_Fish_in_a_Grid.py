class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c] or grid[r][c] == 0:
                return 0
            visited[r][c] = True
            return grid[r][c] + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] > 0:
                    ans = max(ans, dfs(i, j))
        return ans
