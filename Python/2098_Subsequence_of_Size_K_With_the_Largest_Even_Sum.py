# Author: Kaustav Ghosh
# Problem 2098: Subsequence of Size K With the Largest Even Sum
# Premium Problem
#
# Given an integer array nums and an integer k, return the largest even sum
# of any subsequence of nums with length k, or -1 if not possible.
#
# Solution: Sort descending, take top k. If sum is even, return it.
# If sum is odd, try swapping the smallest odd in top-k with the largest
# even outside, or the smallest even in top-k with the largest odd outside.
#
# class Solution(object):
#     def largestEvenSum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         nums.sort(reverse=True)
#         total = sum(nums[:k])
#         if total % 2 == 0:
#             return total
#         # Separate chosen and remaining into odd/even
#         chosen_odd = []
#         chosen_even = []
#         for i in range(k):
#             if nums[i] % 2 == 0:
#                 chosen_even.append(nums[i])
#             else:
#                 chosen_odd.append(nums[i])
#         remain_odd = []
#         remain_even = []
#         for i in range(k, len(nums)):
#             if nums[i] % 2 == 0:
#                 remain_even.append(nums[i])
#             else:
#                 remain_odd.append(nums[i])
#         best = -1
#         # Swap smallest odd in chosen with largest even in remaining
#         if chosen_odd and remain_even:
#             candidate = total - chosen_odd[-1] + remain_even[0]
#             best = max(best, candidate)
#         # Swap smallest even in chosen with largest odd in remaining
#         if chosen_even and remain_odd:
#             candidate = total - chosen_even[-1] + remain_odd[0]
#             best = max(best, candidate)
#         return best

class Solution(object):
    pass
