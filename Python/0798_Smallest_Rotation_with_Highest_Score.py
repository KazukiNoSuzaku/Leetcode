# Find rotation k that maximizes score (count of i where A[(i-k)%n] <= i).

# Author: Kaustav Ghosh

class Solution(object):
    def bestRotation(self, nums):
        n = len(nums)
        bad = [0] * n
        for i, x in enumerate(nums):
            lo = (i - x + 1) % n
            hi = (i + 1) % n
            bad[lo] += 1
            if hi != lo: bad[hi] -= 1
            if hi < lo: bad[0] += 1
        best = best_k = 0
        cur = 0
        for k in range(n):
            cur += bad[k]
            if cur > best:
                best = cur
                best_k = k
        return best_k
