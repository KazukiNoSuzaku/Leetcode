# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-matrix-sum/

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total = 0
        min_abs = float('inf')
        neg_count = 0
        for row in matrix:
            for val in row:
                total += abs(val)
                min_abs = min(min_abs, abs(val))
                if val < 0:
                    neg_count += 1
        # If odd number of negatives, we must keep one negative
        if neg_count % 2 == 1:
            total -= 2 * min_abs
        return total
