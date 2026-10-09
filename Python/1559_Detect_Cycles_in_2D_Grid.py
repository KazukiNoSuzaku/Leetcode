# Author: Kaustav Ghosh
# Problem: Detect Cycles in 2D Grid
# Approach: Treat equal-valued neighbours as edges of a graph and union them, scanning each cell's right and lower neighbour so every edge is handled once. Finding two already-joined cells means a second route between them exists, which is a cycle; in a grid any such cycle encloses at least four cells, so no shorter false positive is possible

class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        rows, cols = len(grid), len(grid[0])
        parent = list(range(rows * cols))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for r in range(rows):
            for c in range(cols):
                for nr, nc in ((r, c + 1), (r + 1, c)):
                    if nr < rows and nc < cols and grid[nr][nc] == grid[r][c]:
                        a, b = find(r * cols + c), find(nr * cols + nc)
                        if a == b:
                            return True
                        parent[a] = b
        return False
