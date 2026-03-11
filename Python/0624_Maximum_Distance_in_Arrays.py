# Given a list of sorted arrays, find the maximum absolute difference
# using elements from two different arrays.

# Author: Kaustav Ghosh

class Solution(object):
    def maxDistance(self, arrays):
        res = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        for arr in arrays[1:]:
            res = max(res, abs(arr[-1] - min_val), abs(max_val - arr[0]))
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
        return res
