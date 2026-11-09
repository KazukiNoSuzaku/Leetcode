# Author: Kaustav Ghosh
# Problem: Finding Pairs With a Certain Sum
# Approach: Only the second array is ever modified and only the first is ever iterated, which is the asymmetry the design turns on: the second array is kept as a tally of its values so an update is two constant-time adjustments, and a count walks the much shorter first array looking up the complement it needs. That makes counting proportional to the first array's length rather than to the product of the two, and the tally never has to be rebuilt after an update.

class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        from collections import Counter

        self.nums1 = nums1
        self.nums2 = nums2
        self.tally = Counter(nums2)

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.tally[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.tally[self.nums2[index]] += 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        return sum(self.tally.get(tot - value, 0) for value in self.nums1)


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
