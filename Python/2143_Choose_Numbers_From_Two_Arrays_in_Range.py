# Author: Kaustav Ghosh
# https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

# Premium Problem
# DP with offset for subset sum differences.
# For each index, choose from nums1 (add value) or nums2 (subtract value).
# Count ways where final sum > 0.
#
# class Solution(object):
#     def countSubranges(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: int
#         """
#         MOD = 10**9 + 7
#         # dp[diff] = number of ways to achieve this difference
#         dp = {}
#         result = 0
#         for a, b in zip(nums1, nums2):
#             new_dp = {}
#             # Choose from nums1: +a
#             new_dp[a] = new_dp.get(a, 0) + 1
#             # Choose from nums2: -b
#             new_dp[-b] = new_dp.get(-b, 0) + 1
#             for diff, cnt in dp.items():
#                 new_dp[diff + a] = (new_dp.get(diff + a, 0) + cnt) % MOD
#                 new_dp[diff - b] = (new_dp.get(diff - b, 0) + cnt) % MOD
#             dp = new_dp
#             result = (result + dp.get(0, 0)) % MOD
#         return result

class Solution(object):
    pass
