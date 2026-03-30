# Author: Kaustav Ghosh
# Problem: 2172. Maximum AND Sum of Array
# URL: https://leetcode.com/problems/maximum-and-sum-of-array/
# Premium Problem
# Approach: Bitmask DP where each slot (1..numSlots) can hold at most 2 numbers.
#           Represent slot usage with a 3-ary mask (0,1,2 nums per slot).
#           dp[mask] = max AND sum assigning first popcount(mask) nums to slots.
#
# class Solution(object):
#     def maximumANDSum(self, nums, numSlots):
#         """
#         :type nums: List[int]
#         :type numSlots: int
#         :rtype: int
#         """
#         n = len(nums)
#         # Encode state: each slot can hold 0, 1, or 2 items => base-3 mask
#         total_states = 3 ** numSlots
#         dp = [-1] * total_states
#         dp[0] = 0
#         ans = 0
#         for mask in range(total_states):
#             if dp[mask] < 0:
#                 continue
#             # Count how many numbers have been placed so far
#             idx = 0
#             tmp = mask
#             for s in range(numSlots):
#                 idx += tmp % 3
#                 tmp //= 3
#             if idx >= n:
#                 continue
#             num = nums[idx]
#             # Try placing nums[idx] into each slot
#             base = 1
#             for slot in range(1, numSlots + 1):
#                 digit = (mask // base) % 3
#                 if digit < 2:  # slot not full
#                     new_mask = mask + base  # increase this slot's count by 1
#                     val = dp[mask] + (num & slot)
#                     if val > dp[new_mask]:
#                         dp[new_mask] = val
#                     if val > ans:
#                         ans = val
#                 base *= 3
#         return ans

class Solution(object):
    pass
