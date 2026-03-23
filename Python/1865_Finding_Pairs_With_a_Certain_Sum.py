# Author: Kaustav Ghosh
# Problem 1865: Finding Pairs With a Certain Sum

from collections import Counter

class FindSumPairs(object):
    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.count2 = Counter(nums2)

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.count2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.count2[self.nums2[index]] += 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        result = 0
        for x in self.nums1:
            result += self.count2.get(tot - x, 0)
        return result
