# Author: Kaustav Ghosh
# Problem: Number of Ways to Reorder Array to Get Same BST
# Approach: The first element is the root; recursively count orderings of the left/right subsets and multiply by the interleavings C(L+R, L); subtract 1 to exclude the original order

from math import comb

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        def ways(seq):
            if len(seq) <= 2:
                return 1
            root = seq[0]
            left = [x for x in seq if x < root]
            right = [x for x in seq if x > root]
            interleave = comb(len(left) + len(right), len(left))
            return interleave * ways(left) % MOD * ways(right) % MOD

        return (ways(nums) - 1) % MOD
