# Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves are allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins.
# Implement the TicTacToe class.

# Example 1:
# Input: ["TicTacToe","move","move","move","move","move","move","move"]
#        [[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]
# Output: [null,0,0,0,0,0,0,1]

# Constraints:
# 2 <= n <= 100
# player is 1 or 2.
# 1 <= row, col <= n - 1

# Author: Kaustav Ghosh

class TicTacToe(object):
    def __init__(self, n):
        self.n = n
        self.rows = [[0, 0] for _ in range(n)]
        self.cols = [[0, 0] for _ in range(n)]
        self.diag = [0, 0]
        self.anti = [0, 0]

    def move(self, row, col, player):
        n, p = self.n, player - 1
        self.rows[row][p] += 1
        self.cols[col][p] += 1
        if row == col:
            self.diag[p] += 1
        if row + col == n - 1:
            self.anti[p] += 1
        if (self.rows[row][p] == n or self.cols[col][p] == n or
                self.diag[p] == n or self.anti[p] == n):
            return player
        return 0
