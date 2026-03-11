# Find the length of the longest mountain subarray.

# Author: Kaustav Ghosh

class Solution(object):
    def longestMountain(self, arr):
        n = len(arr)
        res = 0
        i = 1
        while i < n - 1:
            if arr[i-1] < arr[i] > arr[i+1]:
                lo = hi = i
                while lo > 0 and arr[lo-1] < arr[lo]: lo -= 1
                while hi < n-1 and arr[hi] > arr[hi+1]: hi += 1
                res = max(res, hi - lo + 1)
                i = hi
            else:
                i += 1
        return res
