# Author: Kaustav Ghosh
# Problem: Check if There is a Valid Path in a Grid
# Approach: Union-Find or BFS with connector types

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        # Each street type connects certain directions
        # Directions: 0=up, 1=down, 2=left, 3=right
        connects = {
            1: {2, 3},  # left-right
            2: {0, 1},  # up-down
            3: {2, 1},  # left-down
            4: {3, 1},  # right-down
            5: {2, 0},  # left-up
            6: {3, 0},  # right-up
        }
        opposite = {0: 1, 1: 0, 2: 3, 3: 2}
        delta = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

        visited = [[False] * n for _ in range(m)]
        stack = [(0, 0)]
        visited[0][0] = True
        while stack:
            r, c = stack.pop()
            if r == m - 1 and c == n - 1:
                return True
            for d in connects[grid[r][c]]:
                dr, dc = delta[d]
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if opposite[d] in connects[grid[nr][nc]]:
                        visited[nr][nc] = True
                        stack.append((nr, nc))
        return visited[m - 1][n - 1]
