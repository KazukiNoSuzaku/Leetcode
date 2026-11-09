# Author: Kaustav Ghosh
# Problem: Sum of All Subset XOR Totals
# Approach: Consider one bit at a time. If no element carries that bit it contributes nothing, and if at least one does then the subsets split exactly in half between those whose XOR has the bit set and those whose does not, because toggling membership of one element that carries it flips the bit and pairs the subsets up. So every bit present anywhere contributes its value in half of the subsets, which makes the whole answer the OR of all the elements multiplied by two to the power of one less than the array length, with no subset ever enumerated.

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        combined = 0
        for value in nums:
            combined |= value
        return combined << (len(nums) - 1)
