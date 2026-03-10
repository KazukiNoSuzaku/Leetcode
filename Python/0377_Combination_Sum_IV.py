# Given an array of distinct integers nums and a target integer target, return the number
# of possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.
# Note: order matters (unlike combination sum).

# Example 1:
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation: (1,1,1,1),(1,1,2),(1,2,1),(1,3),(2,1,1),(2,2),(3,1)

# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000

# Author: Kaustav Ghosh

class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for num in nums:
                if t >= num:
                    dp[t] += dp[t - num]
        return dp[target]
