# Given an n x n matrix where each of the rows and columns is sorted in ascending order,
# return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example 1:
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13

# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n^2

# Author: Kaustav Ghosh

import bisect

class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]

        def count_le(mid):
            count = 0
            r, c = n - 1, 0
            while r >= 0 and c < n:
                if matrix[r][c] <= mid:
                    count += r + 1
                    c += 1
                else:
                    r -= 1
            return count

        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
