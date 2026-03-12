# Author: Kaustav Ghosh
# BFS with snake state (tail_row, tail_col, direction) where direction 0=horizontal, 1=vertical

class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        n = len(grid)
        # State: (row, col, dir) where (row,col) is tail position, dir=0 horizontal, dir=1 vertical
        start = (0, 0, 0)
        target = (0, n - 2, 0)
        visited = {start}
        queue = deque([(start, 0)])

        while queue:
            (r, c, d), moves = queue.popleft()
            if (r, c, d) == target:
                return moves

            neighbors = []
            if d == 0:  # horizontal: tail at (r,c), head at (r,c+1)
                # Move right
                if c + 2 < n and grid[r][c + 2] == 0:
                    neighbors.append((r, c + 1, 0))
                # Move down
                if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                    neighbors.append((r + 1, c, 0))
                # Rotate clockwise
                if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                    neighbors.append((r, c, 1))
            else:  # vertical: tail at (r,c), head at (r+1,c)
                # Move down
                if r + 2 < n and grid[r + 2][c] == 0:
                    neighbors.append((r + 1, c, 1))
                # Move right
                if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                    neighbors.append((r, c + 1, 1))
                # Rotate counterclockwise
                if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                    neighbors.append((r, c, 0))

            for state in neighbors:
                if state not in visited:
                    visited.add(state)
                    queue.append((state, moves + 1))
        return -1
