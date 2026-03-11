# You are given an integer array nums of length n.
# F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n-1) * arrk[n-1]
# where arrk is obtained by rotating nums right by k positions.
# Return the maximum value of F(0), F(1), ..., F(n-1).

# Author: Kaustav Ghosh

class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)
        f = sum(i * v for i, v in enumerate(nums))
        res = f
        for k in range(1, n):
            f = f + total - n * nums[n - k]
            res = max(res, f)
        return res
