# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number
# on it represented by an array nums. You are asked to burst all the balloons.
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
# If i - 1 or i + 1 goes out of bounds, treat it as 1.
# Return the maximum coins you can collect by bursting the balloons wisely.

# Example 1:
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
#              coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167

# Constraints:
# n == nums.length
# 1 <= n <= 300
# 0 <= nums[i] <= 100

# Author: Kaustav Ghosh

class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right]
                    )
        return dp[0][n - 1]
