# Given lengths of sticks, return largest perimeter of a triangle, or 0 if impossible.

# Author: Kaustav Ghosh

class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
