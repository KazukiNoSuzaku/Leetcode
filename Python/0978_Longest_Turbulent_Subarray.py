# Return the length of the maximum turbulent subarray.
# A subarray is turbulent if comparisons alternate between > and <.

# Author: Kaustav Ghosh

class Solution(object):
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        if n < 2: return n
        res = inc = dec = 1
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                inc = dec + 1
                dec = 1
            elif arr[i] < arr[i-1]:
                dec = inc + 1
                inc = 1
            else:
                inc = dec = 1
            res = max(res, inc, dec)
        return res
