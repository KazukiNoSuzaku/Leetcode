# Author: Kaustav Ghosh
# Problem: 1537 - Get the Maximum Score
# Approach: Two pointers merging sorted arrays, pick max path at common values

class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        i, j = 0, 0
        sum1, sum2 = 0, 0
        result = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                result += max(sum1, sum2) + nums1[i]
                sum1 = sum2 = 0
                i += 1
                j += 1

        while i < len(nums1):
            sum1 += nums1[i]
            i += 1
        while j < len(nums2):
            sum2 += nums2[j]
            j += 1

        result += max(sum1, sum2)
        return result % MOD
