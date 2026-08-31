# Author: Kaustav Ghosh
# Problem: Divide Array Into Equal Pairs
# Approach: The array can be split into equal pairs exactly when every distinct value occurs an even number of times

from collections import Counter


class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return all(c % 2 == 0 for c in Counter(nums).values())
