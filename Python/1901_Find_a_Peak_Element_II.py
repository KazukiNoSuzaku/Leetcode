# Author: Kaustav Ghosh
# Problem: Find a Peak Element II
# Approach: Take the largest value in the middle row; it already beats both of its horizontal neighbours, so it can only fail to be a peak vertically. If the cell directly below it is larger, then the half of the grid below that row is guaranteed to contain a peak, because climbing from that larger cell can never need to come back up through the row just discarded; otherwise the same argument points upwards. Halving the row range each time and scanning only one row per step costs a logarithmic number of row scans instead of examining the whole grid, and the padding of the border by the problem's framing means the search can never run off the edge.

class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        low, high = 0, len(mat) - 1
        while low < high:
            middle = (low + high) // 2
            column = mat[middle].index(max(mat[middle]))
            if mat[middle][column] < mat[middle + 1][column]:
                low = middle + 1
            else:
                high = middle
        return [low, mat[low].index(max(mat[low]))]
