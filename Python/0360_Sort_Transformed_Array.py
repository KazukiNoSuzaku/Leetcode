# Given a sorted integer array nums and three integers a, b and c, apply a quadratic
# function of the form f(x) = ax^2 + bx + c to each element nums[i] in the array,
# and return the array in a sorted order.

# Example 1:
# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]

# Example 2:
# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]

# Constraints:
# 1 <= nums.length <= 200
# -100 <= nums[i], a, b, c <= 100
# nums is sorted in ascending order.

# Author: Kaustav Ghosh

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        def f(x):
            return a * x * x + b * x + c

        n = len(nums)
        res = [0] * n
        lo, hi = 0, n - 1
        idx = n - 1 if a >= 0 else 0

        while lo <= hi:
            fl, fh = f(nums[lo]), f(nums[hi])
            if a >= 0:
                if fl >= fh:
                    res[idx] = fl
                    lo += 1
                else:
                    res[idx] = fh
                    hi -= 1
                idx -= 1
            else:
                if fl <= fh:
                    res[idx] = fl
                    lo += 1
                else:
                    res[idx] = fh
                    hi -= 1
                idx += 1
        return res
