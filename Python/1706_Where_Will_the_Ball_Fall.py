# Author: Kaustav Ghosh
# Problem: Where Will the Ball Fall
# Approach: A ball's path depends only on where it currently is, so each one is traced independently row by row with no need to model the grid as a whole. A board sends the ball one column in its own direction, and the ball is stuck in exactly two situations: the board points it off the side of the box, or the neighbouring board in that same row points back, forming a V that traps it. Both are caught by checking the destination column's board in the current row before committing to the move.

class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(grid), len(grid[0])
        answer = []
        for start in range(cols):
            column = start
            for row in range(rows):
                direction = grid[row][column]
                nextColumn = column + direction
                if nextColumn < 0 or nextColumn >= cols or grid[row][nextColumn] != direction:
                    column = -1
                    break
                column = nextColumn
            answer.append(column)
        return answer
