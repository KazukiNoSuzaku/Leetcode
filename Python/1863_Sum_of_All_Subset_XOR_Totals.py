# Author: Kaustav Ghosh
# Problem 1863: Sum of All Subset XOR Totals

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Each bit that appears in any number contributes to 2^(n-1) subsets
        or_all = 0
        for x in nums:
            or_all |= x
        return or_all * (1 << (len(nums) - 1))
