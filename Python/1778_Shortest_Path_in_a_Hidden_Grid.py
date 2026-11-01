# Author: Kaustav Ghosh
# Problem: Shortest Path in a Hidden Grid
# Approach: The robot can only feel its way around, so the grid has to be mapped before any distance can be measured: a depth-first walk treats the start as the origin, steps into each unvisited neighbour that canMove allows, and undoes the step on the way back, which reveals every reachable cell and where the target sits. With that map in hand the shortest path is an ordinary breadth-first search over the discovered cells. The walk is driven by an explicit stack of frames, each remembering the direction back to its parent, because a 500 by 500 grid gives a path far deeper than Python's recursion limit.

# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
# class GridMaster(object):
#    def canMove(self, direction):
#        """
#        :type direction: str
#        :rtype bool
#        """
#
#    def move(self, direction):
#        """
#        :type direction: str
#        :rtype void
#        """
#
#    def isTarget(self):
#        """
#        :rtype bool
#        """

class Solution(object):
    def findShortestPath(self, master):
        """
        :type master: GridMaster
        :rtype: int
        """
        from collections import deque

        steps = (("U", -1, 0), ("R", 0, 1), ("D", 1, 0), ("L", 0, -1))
        opposite = {"U": "D", "D": "U", "L": "R", "R": "L"}

        seen = {(0, 0)}
        target = (0, 0) if master.isTarget() else None
        # Each frame is a cell, how many of the four directions it has tried,
        # and the move that returns the robot to the cell above it.
        stack = [[0, 0, 0, None]]
        while stack:
            row, col, tried, back = stack[-1]
            if tried == 4:
                stack.pop()
                if back is not None:
                    master.move(back)
                continue
            stack[-1][2] += 1
            direction, dr, dc = steps[tried]
            cell = (row + dr, col + dc)
            if cell in seen or not master.canMove(direction):
                continue
            seen.add(cell)
            master.move(direction)
            if master.isTarget():
                target = cell
            stack.append([cell[0], cell[1], 0, opposite[direction]])

        if target is None:
            return -1

        distance = {(0, 0): 0}
        queue = deque([(0, 0)])
        while queue:
            row, col = queue.popleft()
            if (row, col) == target:
                return distance[(row, col)]
            for _, dr, dc in steps:
                cell = (row + dr, col + dc)
                if cell in seen and cell not in distance:
                    distance[cell] = distance[(row, col)] + 1
                    queue.append(cell)
        return -1
