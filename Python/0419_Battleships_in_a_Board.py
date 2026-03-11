# Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
# return the number of the battleships on board.
# Battleships can only be placed horizontally or vertically on the board.

# Author: Kaustav Ghosh

class Solution(object):
    def countBattleships(self, board):
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if (i == 0 or board[i-1][j] != 'X') and (j == 0 or board[i][j-1] != 'X'):
                        count += 1
        return count
