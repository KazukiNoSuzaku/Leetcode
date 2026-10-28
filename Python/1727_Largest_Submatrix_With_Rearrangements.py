# Author: Kaustav Ghosh
# Problem: Largest Submatrix With Rearrangements
# Approach: Columns may be reordered freely, so a column is fully described by how far the run of ones above each row extends downward to it; those heights are accumulated row by row, with a zero resetting its column. For a fixed bottom row, any set of columns can be brought together, so sorting that row's heights descending means taking the tallest few: with the heights in descending order, choosing the first w columns gives a rectangle of width w and height equal to the w-th tallest, and scanning w over all widths finds the best rectangle resting on that row. Doing this for every row and keeping the largest covers every rearrangement without enumerating any.

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
            row = matrix[r]
            for c in range(cols):
                heights[c] = heights[c] + 1 if row[c] else 0
            for width, height in enumerate(sorted(heights, reverse=True), 1):
                area = height * width
                if area > best:
                    best = area
        return best
