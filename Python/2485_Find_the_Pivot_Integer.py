# Author: Kaustav Ghosh
# Problem: Find the Pivot Integer
# Approach: The two sides overlap only at the pivot x, so the condition 1 + ... + x equals x + ... + n rearranges to x squared being the whole sum n(n + 1) / 2. The pivot therefore exists exactly when that sum is a perfect square

from math import isqrt


class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = n * (n + 1) // 2
        root = isqrt(total)
        return root if root * root == total else -1
