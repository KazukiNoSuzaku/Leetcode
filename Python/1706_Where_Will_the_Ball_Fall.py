# Author: Kaustav Ghosh
# Problem: Where Will the Ball Fall
# Approach: Drop each ball row by row; a board sends it to col+direction, but it gets stuck against a wall or a V-shaped pair (neighbor board tilts the other way)

class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        result = []
        for start in range(n):
            col = start
            for row in range(m):
                direction = grid[row][col]
                nxt = col + direction
                if nxt < 0 or nxt >= n or grid[row][nxt] != direction:
                    col = -1
                    break
                col = nxt
            result.append(col)
        return result
