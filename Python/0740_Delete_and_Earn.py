# Earn points by deleting elements (and removing all equal to selected+-1). Max total.

# Author: Kaustav Ghosh

class Solution(object):
    def deleteAndEarn(self, nums):
        points = [0] * (max(nums) + 1)
        for n in nums: points[n] += n
        prev2 = prev1 = 0
        for p in points:
            prev2, prev1 = prev1, max(prev1, prev2 + p)
        return prev1
