# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

# Author: Kaustav Ghosh

class Solution(object):
    def searchRange(self, nums, target):
        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1  # Search on the left side
                    else:
                        left = mid + 1  # Search on the right side
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return bound

        start = findBound(True)
        if start == -1:  # Target not found
            return [-1, -1]
        
        end = findBound(False)
        return [start, end]