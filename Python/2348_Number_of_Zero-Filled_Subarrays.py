# Author: Kaustav Ghosh
# 2348. Number of Zero-Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays/
# Difficulty: Medium
#
# For each run of k consecutive zeros, the number of subarrays is k*(k+1)//2

class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        run = 0
        for n in nums:
            if n == 0:
                run += 1
                ans += run
            else:
                run = 0
        return ans
