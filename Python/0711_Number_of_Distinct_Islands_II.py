# Count distinct island shapes considering rotations and reflections as same.

# Author: Kaustav Ghosh

class Solution(object):
    def numDistinctIslands2(self, grid):
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c, cells):
            grid[r][c] = 0
            cells.append((r, c))
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                    dfs(nr, nc, cells)
        def normalize(cells):
            shapes = []
            for s1, s2 in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                for swap in [False, True]:
                    shape = [(s1*r, s2*c) if not swap else (s1*c, s2*r) for r, c in cells]
                    min_r = min(r for r, c in shape)
                    min_c = min(c for r, c in shape)
                    shapes.append(sorted((r-min_r, c-min_c) for r, c in shape))
            return min(tuple(s) for s in shapes)
        seen = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    cells = []
                    dfs(r, c, cells)
                    seen.add(normalize(cells))
        return len(seen)
