# Given an integer array sorted in non-decreasing order,
# return an array of the squares of each number, sorted in non-decreasing order.

# Author: Kaustav Ghosh

class Solution(object):
    def sortedSquares(self, nums):
        res = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l] ** 2)
                l += 1
            else:
                res.append(nums[r] ** 2)
                r -= 1
        return res[::-1]
