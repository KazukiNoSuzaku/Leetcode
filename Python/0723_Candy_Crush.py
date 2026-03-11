# Simulate Candy Crush: mark groups of 3+, remove them, gravity, repeat.

# Author: Kaustav Ghosh

class Solution(object):
    def candyCrush(self, board):
        rows, cols = len(board), len(board[0])
        changed = True
        while changed:
            changed = False
            to_crush = [[False]*cols for _ in range(rows)]
            for r in range(rows):
                for c in range(cols-2):
                    v = abs(board[r][c])
                    if v and v == abs(board[r][c+1]) == abs(board[r][c+2]):
                        to_crush[r][c] = to_crush[r][c+1] = to_crush[r][c+2] = True
            for r in range(rows-2):
                for c in range(cols):
                    v = abs(board[r][c])
                    if v and v == abs(board[r+1][c]) == abs(board[r+2][c]):
                        to_crush[r][c] = to_crush[r+1][c] = to_crush[r+2][c] = True
            for r in range(rows):
                for c in range(cols):
                    if to_crush[r][c]:
                        board[r][c] = 0
                        changed = True
            for c in range(cols):
                write = rows - 1
                for r in range(rows-1, -1, -1):
                    if board[r][c]:
                        board[write][c] = board[r][c]
                        write -= 1
                for r in range(write, -1, -1):
                    board[r][c] = 0
        return board
