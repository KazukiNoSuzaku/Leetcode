# Author: Kaustav Ghosh
# https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/
# Premium Problem
#
# Given array nums and queries where each query is [x, y],
# return sum of nums[x] + nums[x+y] + nums[x+2y] + ... for valid indices.
# Use suffix sums for small y values (sqrt decomposition) and
# brute force for large y values.
#
# class Solution(object):
#     def solve(self, nums, queries):
#         """
#         :type nums: List[int]
#         :type queries: List[List[int]]
#         :rtype: List[int]
#         """
#         MOD = 10 ** 9 + 7
#         n = len(nums)
#         block = int(n ** 0.5) + 1
#         # Precompute suffix sums for small steps
#         cache = {}
#         for y in range(1, block + 1):
#             suffix = [0] * (n + 1)
#             for i in range(n - 1, -1, -1):
#                 nxt = i + y
#                 suffix[i] = (nums[i] + (suffix[nxt] if nxt < n else 0)) % MOD
#             cache[y] = suffix
#         result = []
#         for x, y in queries:
#             if y <= block:
#                 result.append(cache[y][x])
#             else:
#                 s = 0
#                 while x < n:
#                     s = (s + nums[x]) % MOD
#                     x += y
#                 result.append(s)
#         return result

class Solution(object):
    pass
