# Author: Kaustav Ghosh
# 1064. Fixed Point
# https://leetcode.com/problems/fixed-point/

class Solution(object):
    def fixedPoint(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lo, hi = 0, len(arr) - 1
        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == mid:
                result = mid
                hi = mid - 1
            elif arr[mid] < mid:
                lo = mid + 1
            else:
                hi = mid - 1
        return result
