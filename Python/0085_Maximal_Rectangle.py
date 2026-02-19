# Given a rows x cols binary matrix filled with '0's and '1's, find the largest rectangle
# containing only '1's and return its area.

# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6

# Example 2:
# Input: matrix = [["0"]]
# Output: 0

# Constraints:
# rows == matrix.length
# cols == matrix[i].length
# 1 <= rows, cols <= 200
# matrix[i][j] is '0' or '1'.

# Author: Kaustav Ghosh

class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        return max_area
