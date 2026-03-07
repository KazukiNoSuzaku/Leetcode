# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]...
# You may assume the input array always has a valid answer.

# Example 1:
# Input: nums = [1,5,1,1,6,4]
# Output: [1,6,1,5,1,4]

# Example 2:
# Input: nums = [1,3,2,2,3,1]
# Output: [2,3,1,3,1,2]

# Constraints:
# 1 <= nums.length <= 5 * 10^4
# 0 <= nums[i] <= 5000
# It is guaranteed that there will be an answer for the given input nums.

# Author: Kaustav Ghosh

class Solution(object):
    def wiggleSort(self, nums):
        s = sorted(nums)
        n = len(nums)
        mid = (n - 1) // 2
        # Place larger half at odd indices (1,3,5,...), smaller half at even indices (0,2,4,...)
        nums[::2] = s[:mid + 1][::-1]
        nums[1::2] = s[mid + 1:][::-1]
