# Check if an array is monotonically increasing or decreasing.

# Author: Kaustav Ghosh

class Solution(object):
    def isMonotonic(self, nums):
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or \
               all(nums[i] >= nums[i+1] for i in range(len(nums)-1))
