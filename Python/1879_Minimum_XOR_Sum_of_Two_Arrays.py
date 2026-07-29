# Author: Kaustav Ghosh
# Problem: Minimum XOR Sum of Two Arrays
# Approach: Assign nums2 elements to nums1 one index at a time; a bitmask of used nums2 positions memoizes the best XOR sum. The number of used bits equals the current nums1 index

from functools import lru_cache

class Solution(object):
    def minimumXORSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)

        @lru_cache(maxsize=None)
        def dp(mask):
            i = bin(mask).count('1')  # how many nums1 elements already paired
            if i == n:
                return 0
            best = float('inf')
            for j in range(n):
                if not (mask >> j) & 1:
                    best = min(best, (nums1[i] ^ nums2[j]) + dp(mask | (1 << j)))
            return best

        return dp(0)
