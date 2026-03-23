# Author: Kaustav Ghosh
# Problem 1855: Maximum Distance Between a Pair of Values

class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        result = 0
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                result = max(result, j - i)
                j += 1
        return result
