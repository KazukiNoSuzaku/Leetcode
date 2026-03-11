# Given a binary array nums, return the maximum length of a contiguous subarray with equal
# number of 0s and 1s.

# Author: Kaustav Ghosh

class Solution(object):
    def findMaxLength(self, nums):
        seen = {0: -1}
        count = res = 0
        for i, n in enumerate(nums):
            count += 1 if n == 1 else -1
            if count in seen:
                res = max(res, i - seen[count])
            else:
                seen[count] = i
        return res
