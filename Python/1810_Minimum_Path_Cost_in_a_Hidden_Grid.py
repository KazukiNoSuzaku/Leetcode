# Author: Kaustav Ghosh
# Problem: Minimum Path Cost in a Hidden Grid
# Approach: Nothing about the grid is known up front, so it has to be mapped before any cost can be compared: a depth-first walk takes the start as the origin, and every successful move hands back the cost of the cell just entered, which is recorded before the move is undone. That reveals both the reachable cells and their costs, after which the cheapest route is an ordinary Dijkstra over the discovered map, each step paying for the cell being moved into and the starting cell charging nothing. The walk is driven by an explicit stack of frames, each holding the direction back to its parent, since a hundred-by-hundred grid gives a path far deeper than Python's recursion limit.

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
#        :rtype int
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
        from heapq import heappop, heappush

        steps = (("U", -1, 0), ("R", 0, 1), ("D", 1, 0), ("L", 0, -1))
        opposite = {"U": "D", "D": "U", "L": "R", "R": "L"}

        cost = {(0, 0): 0}  # the starting cell is never paid for
        target = (0, 0) if master.isTarget() else None
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
            if cell in cost or not master.canMove(direction):
                continue
            cost[cell] = master.move(direction)
            if master.isTarget():
                target = cell
            stack.append([cell[0], cell[1], 0, opposite[direction]])

        if target is None:
            return -1

        best = {(0, 0): 0}
        heap = [(0, 0, 0)]
        while heap:
            spent, row, col = heappop(heap)
            if (row, col) == target:
                return spent
            if spent > best.get((row, col), spent):
                continue
            for _, dr, dc in steps:
                cell = (row + dr, col + dc)
                if cell not in cost:
                    continue
                total = spent + cost[cell]
                if cell not in best or total < best[cell]:
                    best[cell] = total
                    heappush(heap, (total, cell[0], cell[1]))
        return -1
