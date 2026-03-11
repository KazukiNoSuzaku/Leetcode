# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]),
# return the next greater number for every element in nums.

# Author: Kaustav Ghosh

class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        return res
