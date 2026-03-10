# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such
# that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true

# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: false

# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: true

# Constraints:
# 1 <= nums.length <= 5 * 10^5
# -2^31 <= nums[i] <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def increasingTriplet(self, nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
