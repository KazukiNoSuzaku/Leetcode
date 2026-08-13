# Author: Kaustav Ghosh
# Problem: Minimum Number of Operations to Make Array Continuous
# Approach: The final array occupies a window [x, x+n-1] of distinct values. Elements already inside such a window (and distinct) can be kept; the rest are replaced. Over unique sorted values, slide the window and count the most that fit; the answer is n minus that maximum

import bisect

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        uniq = sorted(set(nums))
        best = 0
        for i, low in enumerate(uniq):
            j = bisect.bisect_right(uniq, low + n - 1)
            best = max(best, j - i)
        return n - best
