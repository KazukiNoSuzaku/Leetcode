# Author: Kaustav Ghosh
# Problem: Number of Ways Where Square of Number Is Equal to Product of Two Numbers
# Approach: For each square target, scan the other array once with a running counter, adding pairs whose product equals the target

class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def count(squares, others):
            total = 0
            for x in squares:
                t = x * x
                seen = {}
                for y in others:
                    if t % y == 0:
                        total += seen.get(t // y, 0)
                    seen[y] = seen.get(y, 0) + 1
            return total

        return count(nums1, nums2) + count(nums2, nums1)
