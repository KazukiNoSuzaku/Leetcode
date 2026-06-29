# Author: Kaustav Ghosh
# Problem: Detect Cycles in 2D Grid
# Approach: Union-Find over same-valued neighbors (right and down only); if two cells to be merged already share a root, a cycle exists

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

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[ra] = rb
            return True

        for r in range(rows):
            for c in range(cols):
                idx = r * cols + c
                if c + 1 < cols and grid[r][c] == grid[r][c + 1]:
                    if not union(idx, idx + 1):
                        return True
                if r + 1 < rows and grid[r][c] == grid[r + 1][c]:
                    if not union(idx, idx + cols):
                        return True
        return False
