# Author: Kaustav Ghosh
# Problem: Sort Array by Increasing Frequency
# Approach: Sort by frequency ascending; break ties by value descending

from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))
