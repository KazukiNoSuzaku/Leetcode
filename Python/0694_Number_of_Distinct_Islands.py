# Count distinct island shapes in a binary grid (up to translation).

# Author: Kaustav Ghosh

class Solution(object):
    def numDistinctIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        shapes = set()
        def dfs(r, c, r0, c0, path):
            grid[r][c] = 0
            path.append((r - r0, c - c0))
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                    dfs(nr, nc, r0, c0, path)
            path.append((None, None))  # backtrack marker
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    path = []
                    dfs(r, c, r, c, path)
                    shapes.add(tuple(path))
        return len(shapes)
