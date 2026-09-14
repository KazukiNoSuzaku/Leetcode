# Author: Kaustav Ghosh
# Problem: Maximum Number of Pairs in Array
# Approach: Count occurrences of each value; a value seen c times forms c // 2 pairs and leaves c % 2 behind, so sum both over all counts

from collections import Counter


class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pairs = leftover = 0
        for c in Counter(nums).values():
            pairs += c // 2
            leftover += c % 2
        return [pairs, leftover]
