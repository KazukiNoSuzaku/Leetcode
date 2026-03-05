# Given an integer array nums, in which exactly two elements appear only once and all the other
# elements appear exactly twice. Find the two elements that appear only once.
# You must write an algorithm that runs in linear runtime complexity and uses only constant space.

# Example 1:
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]

# Example 2:
# Input: nums = [-1,0]
# Output: [-1,0]

# Constraints:
# 2 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# Each integer in nums will appear twice, only two integers will appear once.

# Author: Kaustav Ghosh

class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for n in nums:
            xor ^= n
        # Get rightmost set bit (differentiates the two unique numbers)
        diff_bit = xor & (-xor)
        a = 0
        for n in nums:
            if n & diff_bit:
                a ^= n
        return [a, xor ^ a]
