# Author: Kaustav Ghosh
# Problem: Minimize Product Sum of Two Arrays
# Approach: Pairing the largest value of one array with the smallest of the other minimises the total, because swapping any two pairs that are not arranged that way always lowers the sum: for a < b and c < d the crossed pairing a times d plus b times c is never larger than the aligned one. Sorting one array upwards and the other downwards and multiplying position by position therefore gives the minimum directly. Sorted copies are taken rather than sorting in place so the caller's arrays are left alone.

class Solution(object):
    def minProductSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return sum(x * y for x, y in zip(sorted(nums1), sorted(nums2, reverse=True)))
