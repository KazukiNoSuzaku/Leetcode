# Find minimum dice rolls to reach end on a Snakes and Ladders board.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)
        def cell(s):
            r, c = divmod(s - 1, n)
            if r % 2: c = n - 1 - c
            return board[n-1-r][c]
        q = deque([(1, 0)])
        visited = {1}
        while q:
            pos, moves = q.popleft()
            for dice in range(1, 7):
                npos = pos + dice
                if npos > n*n: break
                dest = cell(npos)
                if dest != -1: npos = dest
                if npos == n*n: return moves + 1
                if npos not in visited:
                    visited.add(npos)
                    q.append((npos, moves + 1))
        return -1
