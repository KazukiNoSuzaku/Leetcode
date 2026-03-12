# Author: Kaustav Ghosh
# BFS with state (row, col, remaining_eliminations)

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        from collections import deque
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0

        # Optimization: if k >= m + n - 3, can go straight
        if k >= m + n - 3:
            return m + n - 2

        visited = {(0, 0, k)}
        queue = deque([(0, 0, k, 0)])

        while queue:
            r, c, remaining, steps = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_k = remaining - grid[nr][nc]
                    if new_k >= 0 and (nr, nc, new_k) not in visited:
                        if nr == m - 1 and nc == n - 1:
                            return steps + 1
                        visited.add((nr, nc, new_k))
                        queue.append((nr, nc, new_k, steps + 1))
        return -1
