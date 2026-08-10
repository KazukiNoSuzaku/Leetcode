# Author: Kaustav Ghosh
# Problem: Find the Kth Largest Integer in the Array
# Approach: Numeric-string order equals (length, then lexicographic) order for non-negative integers without leading zeros. Sort by that key and pick the kth largest

class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums.sort(key=lambda s: (len(s), s))
        return nums[-k]
