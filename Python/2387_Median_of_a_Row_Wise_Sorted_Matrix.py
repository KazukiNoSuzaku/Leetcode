# Author: Kaustav Ghosh
# Problem: Median of a Row Wise Sorted Matrix
# Approach: Binary search on the value instead of the cells. For a candidate x, bisect each sorted row to count the elements <= x; the median is the smallest x for which that count reaches (m * n) // 2 + 1. This is O(m log n log V) rather than touching every cell

from bisect import bisect_right


class Solution(object):
    def matrixMedian(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        need = len(grid) * len(grid[0]) // 2 + 1
        lo = min(row[0] for row in grid)
        hi = max(row[-1] for row in grid)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(bisect_right(row, mid) for row in grid) >= need:
                hi = mid
            else:
                lo = mid + 1
        return lo
