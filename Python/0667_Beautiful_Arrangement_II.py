# Construct an array of 1..n with exactly k distinct absolute differences between adjacent elements.

# Author: Kaustav Ghosh

class Solution(object):
    def constructArray(self, n, k):
        res = list(range(1, n - k))
        lo, hi = n - k, n
        while lo <= hi:
            res.append(lo)
            if lo != hi: res.append(hi)
            lo += 1
            hi -= 1
        return res
