# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]

# Author: Kaustav Ghosh

class Solution(object):
    def solveNQueens(self, n):
        def backtrack(row, cols, diagonals, anti_diagonals, board):
            if row == n:
                result.append(board[:])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
                    continue
                
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)
                board[row] = '.' * col + 'Q' + '.' * (n - col - 1)
                
                backtrack(row + 1, cols, diagonals, anti_diagonals, board)
                
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)
        
        result = []
        board = ['.' * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return result