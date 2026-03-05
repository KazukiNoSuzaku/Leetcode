# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

# Author: Kaustav Ghosh

class Solution(object):
    def rob(self, nums):
        prev2 = prev1 = 0
        for n in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + n)
        return prev1
