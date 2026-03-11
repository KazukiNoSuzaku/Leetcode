# Determine if a tic-tac-toe board state is valid.

# Author: Kaustav Ghosh

class Solution(object):
    def validTicTacToe(self, board):
        x = sum(row.count('X') for row in board)
        o = sum(row.count('O') for row in board)
        if x != o and x != o + 1: return False
        def wins(player):
            for r in board:
                if all(c == player for c in r): return True
            for col in range(3):
                if all(board[r][col] == player for r in range(3)): return True
            if all(board[i][i] == player for i in range(3)): return True
            if all(board[i][2-i] == player for i in range(3)): return True
            return False
        if wins('X') and x != o + 1: return False
        if wins('O') and x != o: return False
        return True
