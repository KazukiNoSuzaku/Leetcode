from functools import reduce
from operator import xor

class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        # Each nums1[i] appears len(nums2) times; each nums2[j] appears len(nums1) times.
        # XOR of x appearing k times = x if k is odd, else 0.
        ans = 0
        if len(nums2) % 2:
            ans ^= reduce(xor, nums1)
        if len(nums1) % 2:
            ans ^= reduce(xor, nums2)
        return ans
