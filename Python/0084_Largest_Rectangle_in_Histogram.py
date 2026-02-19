# Given an array of integers heights representing the histogram's bar height where the width
# of each bar is 1, return the area of the largest rectangle in the histogram.

# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10

# Example 2:
# Input: heights = [2,4]
# Output: 4

# Constraints:
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4

# Author: Kaustav Ghosh

class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []  # (index, height)
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
