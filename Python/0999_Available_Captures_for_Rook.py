# Find the white rook on a chessboard. Count pawns it can capture
# (moving in 4 directions until blocked by bishop or board edge).

# Author: Kaustav Ghosh

class Solution(object):
    def numRookCaptures(self, board):
        rx = ry = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rx, ry = i, j
        res = 0
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x, y = rx + dx, ry + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'B': break
                if board[x][y] == 'p':
                    res += 1
                    break
                x += dx
                y += dy
        return res
