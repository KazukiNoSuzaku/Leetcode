# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

# Example 1:


# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 9

# Author: Kaustav Ghosh

class Solution(object):
    def totalNQueens(self, n):
        def backtrack(row, cols, diagonals, anti_diagonals):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
                    continue
                
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)
                
                count += backtrack(row + 1, cols, diagonals, anti_diagonals)
                
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)
            
            return count
        
        return backtrack(0, set(), set(), set())