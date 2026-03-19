# Author: Kaustav Ghosh
# https://leetcode.com/problems/sort-array-by-increasing-frequency/

from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))
