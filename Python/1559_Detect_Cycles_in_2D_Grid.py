# Author: Kaustav Ghosh
# Problem: 1559 - Detect Cycles in 2D Grid
# Approach: DFS checking same-value cycles of length >= 4

class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, pr, pc):
            visited[r][c] = True
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c]:
                    if nr == pr and nc == pc:
                        continue
                    if visited[nr][nc]:
                        return True
                    if dfs(nr, nc, r, c):
                        return True
            return False

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1):
                        return True
        return False
