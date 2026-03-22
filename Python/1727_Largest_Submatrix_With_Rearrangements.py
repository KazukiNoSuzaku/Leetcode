# Author: Kaustav Ghosh
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/

class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])

        # Build consecutive ones height for each column
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        result = 0
        for i in range(m):
            # Sort heights in descending order for this row
            row = sorted(matrix[i], reverse=True)
            for j in range(n):
                if row[j] == 0:
                    break
                result = max(result, row[j] * (j + 1))

        return result
