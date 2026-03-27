# Author: Kaustav Ghosh
# https://leetcode.com/problems/elements-in-array-after-removing-and-replacing/
# Premium - Simulation with time-based queries
#
# class Solution(object):
#     def elementInNums(self, nums, queries):
#         """
#         :type nums: List[int]
#         :type queries: List[List[int]]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         result = []
#         for t, index in queries:
#             t = t % (2 * n)
#             if t < n:
#                 # Removing phase: first t elements removed
#                 arr = nums[t:]
#             else:
#                 # Replacing phase: first (t - n) elements present
#                 arr = nums[:t - n]
#             if index < len(arr):
#                 result.append(arr[index])
#             else:
#                 result.append(-1)
#         return result

class Solution(object):
    pass
