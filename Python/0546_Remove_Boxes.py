# You are given several boxes with different colors represented by different positive numbers.
# You may experience several rounds to remove boxes until there is no box left. Each time you
# can choose some continuous boxes with the same color, remove them and get k*k points.

# Author: Kaustav Ghosh

from functools import lru_cache

class Solution(object):
    def removeBoxes(self, boxes):
        @lru_cache(maxsize=None)
        def dp(l, r, k):
            if l > r: return 0
            # extend k by merging same-colored boxes from left
            while l < r and boxes[l] == boxes[l+1]:
                l += 1; k += 1
            res = (k+1)**2 + dp(l+1, r, 0)
            for m in range(l+1, r+1):
                if boxes[m] == boxes[l]:
                    res = max(res, dp(l+1, m-1, 0) + dp(m, r, k+1))
            return res
        return dp(0, len(boxes)-1, 0)
