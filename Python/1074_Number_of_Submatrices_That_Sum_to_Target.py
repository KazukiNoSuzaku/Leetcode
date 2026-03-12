# Author: Kaustav Ghosh
# 1074. Number of Submatrices That Sum to Target
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

from collections import defaultdict

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        result = 0
        for r1 in range(m):
            col_sum = [0] * n
            for r2 in range(r1, m):
                for c in range(n):
                    col_sum[c] += matrix[r2][c]
                # Find subarrays of col_sum summing to target
                prefix = defaultdict(int)
                prefix[0] = 1
                cur = 0
                for s in col_sum:
                    cur += s
                    result += prefix[cur - target]
                    prefix[cur] += 1
        return result
