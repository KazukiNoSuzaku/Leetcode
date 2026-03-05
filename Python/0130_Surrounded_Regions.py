# Given an m x n matrix board containing 'X' and 'O', capture all regions that are
# 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]

# Constraints:
# m == board.length, n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

# Author: Kaustav Ghosh

class Solution(object):
    def solve(self, board):
        if not board:
            return
        m, n = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            board[r][c] = 'S'
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(r + dr, c + dc)

        for r in range(m):
            for c in range(n):
                if (r in (0, m-1) or c in (0, n-1)) and board[r][c] == 'O':
                    dfs(r, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
