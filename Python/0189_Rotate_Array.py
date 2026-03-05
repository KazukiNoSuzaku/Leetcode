# Given an integer array nums, rotate the array to the right by k steps,
# where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]

# Constraints:
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5

# Author: Kaustav Ghosh

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        def reverse(lo, hi):
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
