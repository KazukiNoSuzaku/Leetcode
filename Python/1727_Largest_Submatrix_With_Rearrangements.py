# Author: Kaustav Ghosh
# Problem: Largest Submatrix With Rearrangements
# Approach: Build column heights of consecutive 1s ending at each row; since columns may be reordered, sort those heights descending and the best rectangle at that row is max(height[i] * (i+1))

class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        best = 0

        for r in range(rows):
            for c in range(cols):
                heights[c] = heights[c] + 1 if matrix[r][c] == 1 else 0
            for i, h in enumerate(sorted(heights, reverse=True)):
                best = max(best, h * (i + 1))

        return best
