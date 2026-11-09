# Author: Kaustav Ghosh
# Problem: Maximum Distance Between a Pair of Values
# Approach: Both arrays are non-increasing, which means that once a position in the first array is too large to pair with a position in the second, moving the second position further right only makes it smaller and cannot help, so that first position can be abandoned for good. Two pointers therefore sweep forward and never back: when the pair is valid the distance is recorded and the second pointer advances to look for a longer one, and when it is not the first pointer advances. Each pointer crosses its array once.

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
                if j - i > best:
                    best = j - i
                j += 1
        return best
