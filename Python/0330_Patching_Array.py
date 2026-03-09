# Given a sorted integer array nums and an integer n, add/patch elements to the array such that
# any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.
# Return the minimum number of patches required.

# Example 1:
# Input: nums = [1,3], n = 6
# Output: 1
# Explanation: Add 2, the combination {1, 2, 3} covers [1,6].

# Example 2:
# Input: nums = [1,5,10], n = 20
# Output: 2
# Explanation: Add 2 and 4. Combinations cover [1,20].

# Constraints:
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^4
# nums is sorted in ascending order.
# 1 <= n <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def minPatches(self, nums, n):
        patches = 0
        reach = 0  # can represent all numbers in [1, reach]
        i = 0
        while reach < n:
            if i < len(nums) and nums[i] <= reach + 1:
                reach += nums[i]
                i += 1
            else:
                reach += reach + 1  # patch with reach+1
                patches += 1
        return patches
