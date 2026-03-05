# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.

# Example 1:
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]

# Example 2:
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]

# Constraints:
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# All the values of nums are unique.

# Author: Kaustav Ghosh

class Solution(object):
    def summaryRanges(self, nums):
        res = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            if nums[i] == start:
                res.append(str(start))
            else:
                res.append(str(start) + '->' + str(nums[i]))
            i += 1
        return res
