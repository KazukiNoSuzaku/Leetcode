# Check if number of global inversions equals number of local inversions.

# Author: Kaustav Ghosh

class Solution(object):
    def isIdealPermutation(self, nums):
        max_so_far = 0
        for i in range(len(nums) - 2):
            max_so_far = max(max_so_far, nums[i])
            if max_so_far > nums[i + 2]:
                return False
        return True
