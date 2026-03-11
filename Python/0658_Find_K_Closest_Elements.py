# Find k closest integers to x in a sorted array; return them sorted.

# Author: Kaustav Ghosh

class Solution(object):
    def findClosestElements(self, arr, k, x):
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = (lo + hi) // 2
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo + k]
