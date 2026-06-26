# Author: Kaustav Ghosh
# Problem: Get the Maximum Score
# Approach: Two pointers merging sorted arrays; at each common node take max accumulated sum from either path

class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        i = j = 0
        s1 = s2 = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                s1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                s2 += nums2[j]
                j += 1
            else:
                best = max(s1, s2) + nums1[i]
                s1 = s2 = best
                i += 1
                j += 1
        while i < len(nums1):
            s1 += nums1[i]
            i += 1
        while j < len(nums2):
            s2 += nums2[j]
            j += 1
        return max(s1, s2) % MOD
