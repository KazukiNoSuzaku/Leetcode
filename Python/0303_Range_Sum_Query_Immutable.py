# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive.
# Implement the NumArray class:
# - NumArray(int[] nums) Initializes the object with the integer array nums.
# - int sumRange(int left, int right) Returns the sum of the elements of nums
#   between indices left and right inclusive.

# Example 1:
# Input: ["NumArray","sumRange","sumRange","sumRange"]
#        [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]
# Output: [null,1,-1,-3]

# Constraints:
# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 0 <= left <= right < nums.length
# At most 10^4 calls will be made to sumRange.

# Author: Kaustav Ghosh

class NumArray(object):
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i, n in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + n

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
