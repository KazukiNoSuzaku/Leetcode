# Author: Kaustav Ghosh
# Problem: Find a Peak Element II
# Approach: Binary search on columns. In the mid column pick the row with the global max of that column; if a horizontal neighbor is larger move toward it, otherwise that cell is a peak. Runs in O(m log n)

class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        lo, hi = 0, len(mat[0]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            best_row = max(range(len(mat)), key=lambda r: mat[r][mid])
            left = mat[best_row][mid - 1] if mid > 0 else -1
            right = mat[best_row][mid + 1] if mid < len(mat[0]) - 1 else -1
            if mat[best_row][mid] > left and mat[best_row][mid] > right:
                return [best_row, mid]
            if right > mat[best_row][mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return [-1, -1]
