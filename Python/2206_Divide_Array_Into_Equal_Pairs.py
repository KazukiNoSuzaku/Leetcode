# Author: Kaustav Ghosh
# 2206. Divide Array Into Equal Pairs
# https://leetcode.com/problems/divide-array-into-equal-pairs/
# Difficulty: Easy
#
# Approach: Count the frequency of each number. For pairing to be possible,
# every number must appear an even number of times.

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        freq = Counter(nums)
        for count in freq.values():
            if count % 2 != 0:
                return False
        return True
