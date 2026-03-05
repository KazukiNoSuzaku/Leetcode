# You are a professional robber planning to rob houses along a street arranged in a circle.
# Each house has a certain amount of money stashed.
# Adjacent houses have security systems, and two adjacent houses cannot both be robbed.
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [2,3,2]
# Output: 3

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

# Author: Kaustav Ghosh

class Solution(object):
    def rob(self, nums):
        def rob_linear(houses):
            prev2 = prev1 = 0
            for n in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + n)
            return prev1

        if len(nums) == 1:
            return nums[0]
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
