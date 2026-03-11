# Given an integer array nums of size n, return the minimum number of moves required
# to make all array elements equal. In one move, you can increment or decrement an element by 1.
# The optimal target is the median.

# Author: Kaustav Ghosh

class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(n - median) for n in nums)
