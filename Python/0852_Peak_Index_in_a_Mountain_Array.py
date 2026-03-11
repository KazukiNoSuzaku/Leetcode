# Find the peak index in a mountain array.

# Author: Kaustav Ghosh

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < arr[mid + 1]: lo = mid + 1
            else: hi = mid
        return lo
