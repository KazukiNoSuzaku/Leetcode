# Sum of (max-min) over all non-empty subsequences of nums.

# Author: Kaustav Ghosh

class Solution(object):
    def sumSubseqWidths(self, nums):
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        res = 0
        pw = 1
        for i in range(n):
            res = (res + (nums[i] - nums[n-1-i]) * pw) % MOD
            pw = pw * 2 % MOD
        return res
