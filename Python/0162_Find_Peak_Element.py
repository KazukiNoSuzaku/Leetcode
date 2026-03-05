# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -inf.
# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5

# Constraints:
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.

# Author: Kaustav Ghosh

class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
