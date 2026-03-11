# Find minimum swaps to convert a binary board to a chessboard pattern.

# Author: Kaustav Ghosh

class Solution(object):
    def movesToChessboard(self, board):
        n = len(board)
        for r in range(n):
            for c in range(n):
                if board[0][0] ^ board[r][0] ^ board[0][c] ^ board[r][c]:
                    return -1
        row_sum = sum(board[0])
        col_sum = sum(board[r][0] for r in range(n))
        row_mismatch = sum(board[r][0] != r % 2 for r in range(n))
        col_mismatch = sum(board[0][c] != c % 2 for c in range(n))
        if n % 2 == 1:
            if row_sum * 2 != n: return -1
            if col_sum * 2 != n: return -1
            if row_mismatch % 2: row_mismatch = n - row_mismatch
            if col_mismatch % 2: col_mismatch = n - col_mismatch
        else:
            if abs(row_sum * 2 - n) > 1: return -1
            if abs(col_sum * 2 - n) > 1: return -1
            row_mismatch = min(row_mismatch, n - row_mismatch)
            col_mismatch = min(col_mismatch, n - col_mismatch)
        return (row_mismatch + col_mismatch) // 2
