# Author: Kaustav Ghosh
# Problem: Bitwise XOR of All Pairings
# Approach: Each element of nums1 is paired with every element of nums2, so it appears len(nums2) times in the XOR and cancels out entirely when that count is even. The result is therefore the XOR of nums1 only if nums2 has odd length, combined with the XOR of nums2 only if nums1 has odd length

from functools import reduce
from operator import xor


class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        result = 0
        if len(nums2) % 2:
            result ^= reduce(xor, nums1)
        if len(nums1) % 2:
            result ^= reduce(xor, nums2)
        return result
