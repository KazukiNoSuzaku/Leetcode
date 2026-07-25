# Author: Kaustav Ghosh
# Problem: Minimum Operations to Make the Array Increasing
# Approach: Walk left to right; each element must be at least prev+1, so raise it there when needed and count the increments

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                operations += prev + 1 - nums[i]
                prev = prev + 1
            else:
                prev = nums[i]
        return operations
