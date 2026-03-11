# Given an integer array nums, return the number of triplets chosen from the array
# that can make triangles if we take them as side lengths of a triangle.

# Author: Kaustav Ghosh

class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        count = 0
        for i in range(len(nums) - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count
