# Author: Kaustav Ghosh
# Problem: 1582 - Special Positions in a Binary Matrix
# Approach: Find cells where mat[i][j]==1 and row/col sums are 1

class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows = len(mat)
        cols = len(mat[0])
        row_sum = [sum(mat[i]) for i in range(rows)]
        col_sum = [sum(mat[i][j] for i in range(rows)) for j in range(cols)]

        result = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    result += 1
        return result
