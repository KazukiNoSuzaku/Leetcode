# Author: Kaustav Ghosh
# Problem: Sum of All Subset XOR Totals
# Approach: Any bit set in some element appears in exactly half the subsets, so the answer is (OR of all elements) * 2^(n-1)

from functools import reduce
from operator import or_

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(or_, nums) << (len(nums) - 1)
