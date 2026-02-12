# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

# Author: Kaustav Ghosh

class Solution(object):
    def subsets(self, nums):
        result = []
        self.backtrack(nums, 0, [], result)
        return result

    def backtrack(self, nums, start, path, result):
        result.append(path[:])  # Add a copy of the current path to the result
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i + 1, path, result)
            path.pop()  # Backtrack by removing the last element added