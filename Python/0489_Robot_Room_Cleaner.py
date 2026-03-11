# Given a robot cleaner in a room modeled as a grid. Each cell in the grid can be empty or blocked.
# The robot runs the given clean() API to clean the current cell, move() to move forward, and turn() to turn.
# Design an algorithm to clean the entire room using only the 4 given APIs.

# Author: Kaustav Ghosh

class Solution(object):
    def cleanRoom(self, robot):
        visited = set()
        # Directions: up, right, down, left
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(r, c, d):
            robot.clean()
            visited.add((r, c))
            for i in range(4):
                nd = (d + i) % 4
                nr, nc = r + dirs[nd][0], c + dirs[nd][1]
                if (nr, nc) not in visited and robot.move():
                    dfs(nr, nc, nd)
                    go_back()
                robot.turnRight()

        dfs(0, 0, 0)
