# Author: Kaustav Ghosh
# Problem: Shortest Path in a Hidden Grid (Premium)
# Approach: DFS with the robot to map every reachable cell into a set of open coordinates and locate the target, then a plain BFS over that discovered grid gives the shortest path

# """
# This is GridMaster's API interface.
# class GridMaster(object):
#     def canMove(self, direction: str) -> bool:
#     def move(self, direction: str) -> None:
#     def isTarget(self) -> bool:
# """

from collections import deque

class Solution(object):
    def findShortestPath(self, master):
        """
        :type master: GridMaster
        :rtype: int
        """
        moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        opposite = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

        open_cells = set()
        target = [None]

        def explore(r, c):
            open_cells.add((r, c))
            if master.isTarget():
                target[0] = (r, c)
            for d, (dr, dc) in moves.items():
                nr, nc = r + dr, c + dc
                if (nr, nc) not in open_cells and master.canMove(d):
                    master.move(d)
                    explore(nr, nc)
                    master.move(opposite[d])  # backtrack

        explore(0, 0)
        if target[0] is None:
            return -1

        queue = deque([(0, 0, 0)])
        seen = {(0, 0)}
        while queue:
            r, c, dist = queue.popleft()
            if (r, c) == target[0]:
                return dist
            for dr, dc in moves.values():
                nr, nc = r + dr, c + dc
                if (nr, nc) in open_cells and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
        return -1
