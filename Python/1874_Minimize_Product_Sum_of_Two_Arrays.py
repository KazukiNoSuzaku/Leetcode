# Author: Kaustav Ghosh
# Problem: Minimize Product Sum of Two Arrays (Premium)
# Approach: By the rearrangement inequality, pairing the largest of one array with the smallest of the other minimizes the product sum

class Solution(object):
    def minProductSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort(reverse=True)
        return sum(a * b for a, b in zip(nums1, nums2))
