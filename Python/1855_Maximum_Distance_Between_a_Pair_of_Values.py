# Author: Kaustav Ghosh
# Problem: Maximum Distance Between a Pair of Values
# Approach: Both arrays are non-increasing, so a two-pointer sweep works: advance i when nums1[i] > nums2[j] (invalid), otherwise record j-i and advance j

class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = j = 0
        best = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                best = max(best, j - i)
                j += 1
        return best
