# Find length of longest Fibonacci-like subsequence in a strictly increasing array.

# Author: Kaustav Ghosh

class Solution(object):
    def lenLongestFibSubseq(self, arr):
        index = {x: i for i, x in enumerate(arr)}
        dp = {}
        res = 0
        for k in range(len(arr)):
            for j in range(k):
                i = index.get(arr[k] - arr[j], -1)
                if i >= 0 and i < j:
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    res = max(res, dp[(j, k)])
        return res if res >= 3 else 0
