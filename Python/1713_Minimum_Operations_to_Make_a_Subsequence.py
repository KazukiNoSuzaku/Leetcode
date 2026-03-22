# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

from bisect import bisect_left

class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        # Map target values to their indices
        pos = {}
        for i, val in enumerate(target):
            pos[val] = i
        # Build array of indices from arr that appear in target
        sub = []
        for val in arr:
            if val in pos:
                sub.append(pos[val])
        # Find LIS length of sub using patience sorting
        tails = []
        for x in sub:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(target) - len(tails)
