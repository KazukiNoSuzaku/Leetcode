# Author: Kaustav Ghosh
# Problem: 2263. Make Array Non-decreasing or Non-increasing
# URL: https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/
# Difficulty: Hard
# Premium: True
#
# Approach:
# Use a greedy approach with a max-heap for non-decreasing and min-heap for
# non-increasing. For non-decreasing: iterate left to right, if current element
# is smaller than heap top, the cost is the difference; replace top with current.
# Take the minimum of both directions.
#
# def minCost(nums):
#     import heapq
#     def cost_non_decreasing(arr):
#         heap = []
#         total = 0
#         for x in arr:
#             if heap and -heap[0] > x:
#                 total += -heap[0] - x
#                 heapq.heapreplace(heap, -x)
#             heapq.heappush(heap, -x)
#         return total
#     return min(cost_non_decreasing(nums), cost_non_decreasing(nums[::-1]))

class Solution(object):
    pass
