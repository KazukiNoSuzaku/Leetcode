# Author: Kaustav Ghosh
# Problem: Special Positions in a Binary Matrix
# Approach: Precompute row and column sums; a 1 is special exactly when its row sum and column sum are both 1

class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row_sum = [sum(row) for row in mat]
        col_sum = [sum(col) for col in zip(*mat)]
        return sum(
            1
            for i, row in enumerate(mat)
            for j, v in enumerate(row)
            if v == 1 and row_sum[i] == 1 and col_sum[j] == 1
        )
