# Return the length of the longest arithmetic subsequence in the array.

# Author: Kaustav Ghosh

class Solution(object):
    def longestArithSeqLength(self, nums):
        dp = {}
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
        return max(dp.values())
