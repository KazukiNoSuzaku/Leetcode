# Author: Kaustav Ghosh
# 2341. Maximum Number of Pairs in Array
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/
# Difficulty: Easy
#
# Count frequency of each number; pairs = freq // 2, leftovers = freq % 2

from collections import Counter

class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums)
        pairs = 0
        leftover = 0
        for count in freq.values():
            pairs += count // 2
            leftover += count % 2
        return [pairs, leftover]
