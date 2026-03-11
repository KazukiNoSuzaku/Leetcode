# You are given an m x n matrix M initialized with all 0s and an array of operations ops.
# For each op = [a, b], you increment all cells M[i][j] for 0 <= i < a and 0 <= j < b by 1.
# Count and return the number of maximum integers in the matrix after performing all the operations.

# Author: Kaustav Ghosh

class Solution(object):
    def maxCount(self, m, n, ops):
        if not ops: return m * n
        return min(op[0] for op in ops) * min(op[1] for op in ops)
