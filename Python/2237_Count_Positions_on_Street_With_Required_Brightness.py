# Author: Kaustav Ghosh
# Problem: 2237. Count Positions on Street With Required Brightness
# URL: https://leetcode.com/problems/count-positions-on-street-with-required-brightness/
# Difficulty: Medium
# Note: Premium problem
#
# Approach:
# Use a difference array to mark the brightness contribution of each lamp.
# For each lamp at position p with range r, increment diff[max(0, p-r)] and
# decrement diff[min(n, p+r+1)]. Build prefix sums to get brightness at each
# position and count positions where brightness >= requirement[i].
#
# def countBrightPositions(n, lights, requirement):
#     diff = [0] * (n + 1)
#     for p, r in lights:
#         left = max(0, p - r)
#         right = min(n - 1, p + r)
#         diff[left] += 1
#         if right + 1 < n:
#             diff[right + 1] -= 1
#     brightness = 0
#     count = 0
#     for i in range(n):
#         brightness += diff[i]
#         if brightness >= requirement[i]:
#             count += 1
#     return count

class Solution(object):
    pass
