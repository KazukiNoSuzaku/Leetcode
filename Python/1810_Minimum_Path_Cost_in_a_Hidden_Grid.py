# Author: Kaustav Ghosh
# Problem: Minimum Path Cost in a Hidden Grid (Premium)
# Approach: DFS the robot to record the entry cost of every reachable cell and find the target, backtracking as we go; then run Dijkstra over the discovered cost grid

import heapq

# """
# This is GridMaster's API interface.
# class GridMaster(object):
#     def canMove(self, direction: str) -> bool:
#     def move(self, direction: str) -> int:
#     def isTarget(self) -> bool:
# """

class Solution(object):
    def findShortestPath(self, master):
        """
        :type master: GridMaster
        :rtype: int
        """
        moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        opposite = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

        cost = {}          # cell -> cost to enter it
        target = [None]

        def explore(r, c):
            if master.isTarget():
                target[0] = (r, c)
            for d, (dr, dc) in moves.items():
                nr, nc = r + dr, c + dc
                if (nr, nc) not in cost and master.canMove(d):
                    cost[(nr, nc)] = master.move(d)
                    explore(nr, nc)
                    master.move(opposite[d])  # backtrack

        cost[(0, 0)] = 0
        explore(0, 0)
        if target[0] is None:
            return -1

        # Dijkstra over the discovered grid (entry cost paid when arriving)
        dist = {(0, 0): 0}
        pq = [(0, 0, 0)]
        while pq:
            d, r, c = heapq.heappop(pq)
            if (r, c) == target[0]:
                return d
            if d > dist.get((r, c), float('inf')):
                continue
            for dr, dc in moves.values():
                nr, nc = r + dr, c + dc
                if (nr, nc) in cost:
                    nd = d + cost[(nr, nc)]
                    if nd < dist.get((nr, nc), float('inf')):
                        dist[(nr, nc)] = nd
                        heapq.heappush(pq, (nd, nr, nc))
        return -1
