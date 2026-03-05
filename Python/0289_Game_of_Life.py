# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular
# automaton devised by the British mathematician John Horton Conway in 1970."
# The board is made up of an m x n grid of cells, where each cell has an initial state:
# live (represented by a 1) or dead (represented by a 0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following rules:
# 1. Any live cell with fewer than two live neighbors dies.
# 2. Any live cell with two or three live neighbors lives.
# 3. Any live cell with more than three live neighbors dies.
# 4. Any dead cell with exactly three live neighbors becomes a live cell.
# Update the board in-place.

# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

# Constraints:
# m == board.length, n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.

# Author: Kaustav Ghosh

class Solution(object):
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(m):
            for j in range(n):
                live = sum(
                    1 for di, dj in dirs
                    if 0 <= i+di < m and 0 <= j+dj < n and abs(board[i+di][j+dj]) == 1
                )
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and live == 3:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] > 0 else 0
