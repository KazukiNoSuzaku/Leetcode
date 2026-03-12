# Author: Kaustav Ghosh
# 1099. Two Sum Less Than K
# https://leetcode.com/problems/two-sum-less-than-k/

class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        lo, hi = 0, len(nums) - 1
        result = -1
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s < k:
                result = max(result, s)
                lo += 1
            else:
                hi -= 1
        return result
