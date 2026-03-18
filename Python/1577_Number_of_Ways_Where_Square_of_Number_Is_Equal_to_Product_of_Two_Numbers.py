# Author: Kaustav Ghosh
# Problem: 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
# Approach: Two-sum style counting for both type 1 and type 2 triplets

from collections import Counter

class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def count_triplets(a, b):
            count = Counter(b)
            result = 0
            for x in a:
                sq = x * x
                for y, freq in count.items():
                    if sq % y == 0:
                        z = sq // y
                        if z != y:
                            result += freq * count.get(z, 0)
                        else:
                            result += freq * (freq - 1)
            return result // 2

        return count_triplets(nums1, nums2) + count_triplets(nums2, nums1)
