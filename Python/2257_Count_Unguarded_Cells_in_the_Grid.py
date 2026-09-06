# Author: Kaustav Ghosh
# Problem: Count Unguarded Cells in the Grid
# Approach: Mark guards and walls on the grid. From each guard shoot rays in all four directions, marking empty cells as guarded and stopping only when a wall or another guard blocks the line of sight. Finally count cells that are neither occupied nor guarded

class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        EMPTY, GUARD, WALL, SEEN = 0, 1, 2, 3
        grid = [[EMPTY] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = GUARD
        for r, c in walls:
            grid[r][c] = WALL

        for r, c in guards:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] not in (GUARD, WALL):
                    grid[nr][nc] = SEEN
                    nr += dr
                    nc += dc

        return sum(1 for r in range(m) for c in range(n) if grid[r][c] == EMPTY)
