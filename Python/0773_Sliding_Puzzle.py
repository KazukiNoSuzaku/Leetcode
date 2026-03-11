# Find min moves to solve a 2x3 sliding puzzle with BFS.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def slidingPuzzle(self, board):
        start = ''.join(str(n) for row in board for n in row)
        target = '123450'
        neighbors = {0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[1,3,5], 5:[2,4]}
        q = deque([(start, 0)])
        visited = {start}
        while q:
            state, moves = q.popleft()
            if state == target: return moves
            z = state.index('0')
            for nb in neighbors[z]:
                new = list(state)
                new[z], new[nb] = new[nb], new[z]
                ns = ''.join(new)
                if ns not in visited:
                    visited.add(ns)
                    q.append((ns, moves + 1))
        return -1
