# You are given an inclusive range [lower, upper] and a sorted unique integer array nums,
# where all elements are within the inclusive range.
# A number x is considered missing if x is in [lower, upper] and x is not in nums.
# Return the shortest sorted list of ranges that exactly covers all the missing numbers.

# Example 1:
# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: ["2","4->49","51->74","76->99"]

# Example 2:
# Input: nums = [-1], lower = -1, upper = -1
# Output: []

# Constraints:
# -10^9 <= lower <= upper <= 10^9
# 0 <= nums.length <= 100
# lower <= nums[i] <= upper

# Author: Kaustav Ghosh

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        res = []
        prev = lower - 1
        for i, n in enumerate(nums + [upper + 1]):
            if n - prev >= 2:
                lo = prev + 1
                hi = n - 1
                res.append(str(lo) if lo == hi else "{}->{}" .format(lo, hi))
            prev = n
        return res
