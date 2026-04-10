# Author: Kaustav Ghosh
# Problem: 2257. Count Unguarded Cells in the Grid
# URL: https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
# Difficulty: Medium
#
# Approach:
# Mark guard and wall positions on the grid. For each guard, extend in
# all four directions marking cells as guarded until hitting a wall or
# another guard. Count cells that are neither guarded, guard, nor wall.

class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0] * n for _ in range(m)]
        GUARD = 1
        WALL = 2
        GUARDED = 3

        for r, c in guards:
            grid[r][c] = GUARD
        for r, c in walls:
            grid[r][c] = WALL

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r, c in guards:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == GUARD or grid[nr][nc] == WALL:
                        break
                    grid[nr][nc] = GUARDED
                    nr += dr
                    nc += dc

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        return count
