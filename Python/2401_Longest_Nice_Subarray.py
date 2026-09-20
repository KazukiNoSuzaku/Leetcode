# Author: Kaustav Ghosh
# Problem: Longest Nice Subarray
# Approach: A subarray is nice exactly when no bit is set in two of its numbers, so keep a running OR of the window: if the incoming number shares a bit with it, drop numbers from the left (clearing their bits with XOR) until the clash is gone, then extend and record the width

class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        used = 0
        left = 0
        best = 0
        for right, x in enumerate(nums):
            while used & x:
                used ^= nums[left]
                left += 1
            used |= x
            best = max(best, right - left + 1)
        return best
