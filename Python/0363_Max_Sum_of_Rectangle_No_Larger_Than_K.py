# Given an m x n matrix and an integer k, return the max sum of a rectangle in the
# matrix such that its sum is no larger than k.
# It is guaranteed that there will be a rectangle with a sum no larger than k.

# Example 1:
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -100 <= matrix[i][j] <= 100
# -10^5 <= k <= 10^5

# Author: Kaustav Ghosh

import bisect

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(n):
            row_sums = [0] * m
            for right in range(left, n):
                for r in range(m):
                    row_sums[r] += matrix[r][right]
                # find max subarray sum <= k using sorted prefix sums
                sorted_prefix = [0]
                prefix = 0
                for s in row_sums:
                    prefix += s
                    # find smallest prefix in sorted_prefix >= prefix - k
                    idx = bisect.bisect_left(sorted_prefix, prefix - k)
                    if idx < len(sorted_prefix):
                        res = max(res, prefix - sorted_prefix[idx])
                    bisect.insort(sorted_prefix, prefix)
        return res
