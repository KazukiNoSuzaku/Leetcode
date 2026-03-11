# Check if an array can be made non-decreasing by modifying at most one element.

# Author: Kaustav Ghosh

class Solution(object):
    def checkPossibility(self, nums):
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
                if count > 1: return False
                if i >= 2 and nums[i] < nums[i-2]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
        return True
