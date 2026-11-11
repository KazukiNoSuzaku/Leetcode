# Author: Kaustav Ghosh
# Problem: Count Pairs in Two Arrays
# Approach: Moving each index's own terms to its own side turns the condition into the difference of the two arrays at i plus the difference at j being greater than zero, which depends on nothing but those two per-index differences. Sorting that difference array lets two pointers count the qualifying pairs: for the largest remaining difference, every entry from the smallest one that still clears zero with it onwards also qualifies, so the whole block is counted at once and the pointer closes in. Each pointer crosses the array once after the sort.

class Solution(object):
    def countPairs(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        gaps = sorted(a - b for a, b in zip(nums1, nums2))
        low, high = 0, len(gaps) - 1
        pairs = 0
        while low < high:
            if gaps[low] + gaps[high] > 0:
                pairs += high - low
                high -= 1
            else:
                low += 1
        return pairs
