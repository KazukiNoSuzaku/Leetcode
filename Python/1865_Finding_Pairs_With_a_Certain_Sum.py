# Author: Kaustav Ghosh
# Problem: Finding Pairs With a Certain Sum
# Approach: Keep a frequency counter of nums2; count pairs by summing counts of (tot - x) over nums1. Updates just adjust the counter and the affected element

from collections import Counter

class FindSumPairs(object):
    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        old = self.nums2[index]
        self.freq2[old] -= 1
        self.nums2[index] += val
        self.freq2[self.nums2[index]] += 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        return sum(self.freq2.get(tot - x, 0) for x in self.nums1)
