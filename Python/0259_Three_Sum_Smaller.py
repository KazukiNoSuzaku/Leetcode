# Given an array of n integers nums and an integer target, find the number of index triplets
# i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# Example 1:
# Input: nums = [-2,0,1,3], target = 2
# Output: 2
# Explanation: Because there are two triplets which sums are less than 2:
#              [-2,0,1] and [-2,0,3] — wait that's 1, actually [-2,0,1] and [-2,0,3] > 2... let's see:
#              [-2,0,1]=−1 < 2 ✓, [-2,0,3]=1 < 2 ✓ → Output: 2

# Constraints:
# n == nums.length
# 0 <= n <= 3500
# -100 <= nums[i] <= 100
# -100 <= target <= 100

# Author: Kaustav Ghosh

class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                if nums[i] + nums[lo] + nums[hi] < target:
                    count += hi - lo
                    lo += 1
                else:
                    hi -= 1
        return count
