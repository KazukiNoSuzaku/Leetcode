# Find minimum swaps of corresponding elements to make both arrays strictly increasing.

# Author: Kaustav Ghosh

class Solution(object):
    def minSwap(self, nums1, nums2):
        keep, swap = 0, 1
        for i in range(1, len(nums1)):
            new_keep = new_swap = float('inf')
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                new_keep = min(new_keep, keep)
                new_swap = min(new_swap, swap + 1)
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                new_keep = min(new_keep, swap)
                new_swap = min(new_swap, keep + 1)
            keep, swap = new_keep, new_swap
        return min(keep, swap)
