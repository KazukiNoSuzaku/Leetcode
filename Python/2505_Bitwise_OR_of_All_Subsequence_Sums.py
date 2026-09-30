# Author: Kaustav Ghosh
# Problem: Bitwise OR of All Subsequence Sums
# Approach: Walk the array keeping the prefix sum. Every subsequence sum is covered by OR-ing, at each position, that element with the prefix sum up to it: the element contributes its own bits, and the prefix contributes every carry pattern the earlier elements can build below it. OR-ing those pairs over the whole array gives the OR of all subsequence sums

class Solution(object):
    def subsequenceSumOr(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        prefix = 0
        for x in nums:
            prefix += x
            result |= x | prefix
        return result
