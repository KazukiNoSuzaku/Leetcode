# Author: Kaustav Ghosh
# Problem: Number of Ways to Reach a Position After Exactly k Steps
# Approach: On an infinite line only the counts of left and right steps matter. With gap d = |endPos - startPos|, we need right - left = d and right + left = k, so a way exists only when d <= k and k - d is even, and then the answer is the number of ways to place the (k + d) / 2 steps toward the target among the k steps: C(k, (k + d) / 2) mod 1e9 + 7

from math import comb


class Solution(object):
    def numberOfWays(self, startPos, endPos, k):
        """
        :type startPos: int
        :type endPos: int
        :type k: int
        :rtype: int
        """
        d = abs(endPos - startPos)
        if d > k or (k - d) % 2:
            return 0
        return comb(k, (k + d) // 2) % (10 ** 9 + 7)
