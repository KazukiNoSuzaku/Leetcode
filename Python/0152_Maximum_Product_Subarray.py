# Given an integer array nums, find a subarray that has the largest product, and return the product.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0

# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

# Author: Kaustav Ghosh

class Solution(object):
    def maxProduct(self, nums):
        max_prod = min_prod = result = nums[0]
        for n in nums[1:]:
            candidates = (n, max_prod * n, min_prod * n)
            max_prod = max(candidates)
            min_prod = min(candidates)
            result = max(result, max_prod)
        return result
