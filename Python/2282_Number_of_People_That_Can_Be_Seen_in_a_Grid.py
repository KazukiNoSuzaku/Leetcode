# Author: Kaustav Ghosh
# Problem: 2282. Number of People That Can Be Seen in a Grid
# URL: https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/
# Difficulty: Medium
# Premium: True
#
# Approach:
# For each row, use a monotonic stack to determine how many people each person
# can see to their right. A person can see another if no one in between is
# taller or equal. Process right to left with a decreasing stack.
#
# def seePeople(heights):
#     m, n = len(heights), len(heights[0])
#     result = [[0]*n for _ in range(m)]
#     for i in range(m):
#         stack = []
#         for j in range(n-1, -1, -1):
#             count = 0
#             while stack and stack[-1] < heights[i][j]:
#                 stack.pop()
#                 count += 1
#             if stack and stack[-1] == heights[i][j]:
#                 stack.pop()
#                 count += 1
#                 stack.append(heights[i][j])
#             elif stack:
#                 count += 1
#             stack.append(heights[i][j])
#             # Actually need to reconsider; simplified monotonic approach
#             result[i][j] = count
#     # Similarly for columns (looking down)
#     for j in range(n):
#         stack = []
#         for i in range(m-1, -1, -1):
#             count = 0
#             while stack and stack[-1] < heights[i][j]:
#                 stack.pop()
#                 count += 1
#             if stack:
#                 count += 1
#                 if stack[-1] == heights[i][j]:
#                     stack.pop()
#             stack.append(heights[i][j])
#             result[i][j] += count
#     return result

class Solution(object):
    pass
