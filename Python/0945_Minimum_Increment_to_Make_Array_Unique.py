# Find minimum increments to make all elements unique.

# Author: Kaustav Ghosh

class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                moves += nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1] + 1
        return moves
