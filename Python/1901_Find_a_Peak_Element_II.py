# Author: Kaustav Ghosh
# https://leetcode.com/problems/find-a-peak-element-ii/

class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(mat), len(mat[0])
        lo, hi = 0, m - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            max_col = 0
            for j in range(n):
                if mat[mid][j] > mat[mid][max_col]:
                    max_col = j
            top = mat[mid - 1][max_col] if mid > 0 else -1
            bot = mat[mid + 1][max_col] if mid < m - 1 else -1
            if mat[mid][max_col] > top and mat[mid][max_col] > bot:
                return [mid, max_col]
            elif top > mat[mid][max_col]:
                hi = mid - 1
            else:
                lo = mid + 1
        return [-1, -1]
