# Author: Kaustav Ghosh
# Problem: Check if Every Row and Column Contains All Numbers
# Approach: The matrix is valid when every row and every column is exactly the set {1..n}

class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        target = set(range(1, n + 1))
        for row in matrix:
            if set(row) != target:
                return False
        for col in zip(*matrix):
            if set(col) != target:
                return False
        return True
