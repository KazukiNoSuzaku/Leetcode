# Author: Kaustav Ghosh
# Problem 1874: Minimize Product Sum of Two Arrays (Premium)

class Solution(object):
    def minProductSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort(reverse=True)
        total = 0
        for i in range(len(nums1)):
            total += nums1[i] * nums2[i]
        return total
