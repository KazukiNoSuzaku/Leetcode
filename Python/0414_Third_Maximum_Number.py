# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.

# Author: Kaustav Ghosh

class Solution(object):
    def thirdMax(self, nums):
        top = sorted(set(nums), reverse=True)
        return top[2] if len(top) >= 3 else top[0]
