# Find the length of the longest continuous strictly increasing subsequence.

# Author: Kaustav Ghosh

class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums: return 0
        best = cur = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
                best = max(best, cur)
            else:
                cur = 1
        return best
