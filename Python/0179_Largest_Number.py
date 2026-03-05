# Given a list of non-negative integers nums, arrange them such that they form the largest number
# and return it. Since the result may be very large, return a string instead of an integer.

# Example 1:
# Input: nums = [10,2]
# Output: "210"

# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9

# Author: Kaustav Ghosh

from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0
        strs = [str(n) for n in nums]
        strs.sort(key=cmp_to_key(compare))
        result = ''.join(strs)
        return '0' if result[0] == '0' else result
