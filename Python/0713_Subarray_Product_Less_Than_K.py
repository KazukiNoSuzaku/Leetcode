# Count contiguous subarrays where the product is less than k.

# Author: Kaustav Ghosh

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        left = res = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            res += right - left + 1
        return res
