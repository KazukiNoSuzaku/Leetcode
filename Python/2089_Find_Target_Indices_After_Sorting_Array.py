# Author: Kaustav Ghosh
# Problem: Find Target Indices After Sorting Array
# Approach: After sorting, equal values are contiguous. The first target index equals the count of elements smaller than target; the block spans that count of equal elements

class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less = sum(1 for v in nums if v < target)
        equal = sum(1 for v in nums if v == target)
        return list(range(less, less + equal))
