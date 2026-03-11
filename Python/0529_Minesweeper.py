# Let's play the minesweeper game! Given a board and a click position, update and return the board.
# 'M' = mine, 'E' = empty unrevealed, 'B' = blank revealed, digit = adjacent mines, 'X' = hit mine.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def updateBoard(self, board, click):
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        m, n = len(board), len(board[0])
        queue = deque([(r, c)])
        while queue:
            r, c = queue.popleft()
            if board[r][c] != 'E':
                continue
            mines = sum(
                1 for dr in [-1,0,1] for dc in [-1,0,1]
                if (dr or dc) and 0 <= r+dr < m and 0 <= c+dc < n and board[r+dr][c+dc] in ('M','X')
            )
            if mines:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if (dr or dc) and 0 <= r+dr < m and 0 <= c+dc < n and board[r+dr][c+dc] == 'E':
                            queue.append((r+dr, c+dc))
        return board
